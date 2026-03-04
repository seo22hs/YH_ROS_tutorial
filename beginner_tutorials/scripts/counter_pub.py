#!/usr/bin/env python3

import rospy

from std_msgs.msg import Int32

def counter():

    pub = rospy.Publisher('counter', Int32, queue_size=10)

    rospy.init_node('counter_pub')

    rate = rospy.Rate(1)  # 1Hz = 1초에 1번

    count = 0

    while not rospy.is_shutdown():

        rospy.loginfo("발행: %d", count)

        pub.publish(count)

        count += 1

        rate.sleep()

if __name__ == '__main__':

    try:

        counter()

    except rospy.ROSInterruptException:

        pass


# 실행과정
# cd ~/catkin_ws/src/beginner_tutorials
# counter_pub.py - 생성
# chmod +x scripts/counter_pub.py - 실행권한부여
# 터미널 1 - roscore
# 터미널 2 - rosrun beginner_tutorials counter_pub.py
