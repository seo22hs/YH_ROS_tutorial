#!/usr/bin/env python3
import rospy
import math
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

# ===== 파라미터 =====
LINEAR_SPEED = 0.08
ANGULAR_SPEED = 0.4
DESIRED_DISTANCE = 0.45  # 벽에서 유지할 거리 (m)

class WallFollowerPID:
    def __init__(self):
        rospy.init_node('wall_follower_pid')
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        self.sub = rospy.Subscriber('/scan', LaserScan, self.scan_callback)

        # PID 게인
        self.kp = 0.7
        self.ki = 0.0
        self.kd = 0.12

        # PID 상태
        self.integral = 0.0
        self.prev_error = 0.0
        self.dt = 0.1  # 10Hz

        # 주행 모드
        self.mode = "follow_wall"

        self.rate = rospy.Rate(10)

    def get_range(self, scan, angle):
        index = int((angle - scan.angle_min) / scan.angle_increment)
        index = max(0, min(index, len(scan.ranges) - 1))
        distance = scan.ranges[index]
        if math.isnan(distance) or math.isinf(distance):
            distance = 10.0
        return distance

    def get_error(self, scan, desired_distance):
        theta = math.radians(45)
        a = self.get_range(scan, -math.radians(45))
        b = self.get_range(scan, -math.radians(90))
        alpha = math.atan2(a * math.cos(theta) - b, a * math.sin(theta))
        wall_distance = b * math.cos(alpha)
        return desired_distance - wall_distance

    def pid_control(self, error):
        p_term = self.kp * error

        self.integral += error * self.dt
        self.integral = max(min(self.integral, 1.0), -1.0)
        i_term = self.ki * self.integral

        d_term = self.kd * (error - self.prev_error) / self.dt
        self.prev_error = error

        angular_z = p_term + i_term + d_term
        angular_z = max(min(angular_z, 0.5), -0.5)

        twist = Twist()
        twist.linear.x = LINEAR_SPEED
        twist.angular.z = angular_z
        self.pub.publish(twist)

    def scan_callback(self, scan):
        front = self.get_range(scan, 0.0)
        front_right = self.get_range(scan, -math.radians(45))
        right = self.get_range(scan, -math.radians(90))
        error = self.get_error(scan, DESIRED_DISTANCE)

        # 문처럼 오른쪽이 갑자기 열리는 구간은 따라가지 않고 직진 유지
        if self.mode == "follow_wall" and right > 1.0 and front_right > 1.0 and front > 0.8:
            self.mode = "skip_gap"

        # 문 구간을 지나 앞벽이 보이면 코너 회전 시작
        if self.mode == "skip_gap" and front < 0.7:
            self.mode = "turn_corner"

        # 코너를 돌고 다시 오른쪽 벽이 가까워지면 일반 추종 복귀
        if self.mode == "turn_corner" and right < 0.7 and front > 0.7:
            self.mode = "follow_wall"

        if self.mode == "skip_gap":
            twist = Twist()
            twist.linear.x = LINEAR_SPEED
            twist.angular.z = -0.05
            self.pub.publish(twist)
            rospy.loginfo("문 무시 직진 | front=%.2f front_right=%.2f right=%.2f",
                          front, front_right, right)

        elif self.mode == "turn_corner":
            twist = Twist()
            twist.linear.x = 0.05
            twist.angular.z = ANGULAR_SPEED
            self.pub.publish(twist)
            rospy.loginfo("코너 좌회전 | front=%.2f front_right=%.2f right=%.2f",
                          front, front_right, right)

        elif front < 0.5:
            twist = Twist()
            twist.linear.x = 0.0
            twist.angular.z = ANGULAR_SPEED
            self.pub.publish(twist)
            rospy.loginfo("전방 벽 - 좌회전 | front=%.2f", front)

        else:
            self.mode = "follow_wall"
            self.pid_control(error)
            rospy.loginfo("PID 벽 따라가기 | error=%.3f | front=%.2f | front_right=%.2f | right=%.2f",
                          error, front, front_right, right)

if __name__ == '__main__':
    try:
        wf = WallFollowerPID()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
