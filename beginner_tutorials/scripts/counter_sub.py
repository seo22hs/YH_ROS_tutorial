#!/usr/bin/env python3

import rospy

from std_msgs.msg import Int32

def callback(msg):

    rospy.loginfo("수신: %d", msg.data)

def listener():

    rospy.init_node('counter_sub')

    rospy.Subscriber('counter', Int32, callback)

    rospy.spin()

if __name__ == '__main__':

    listener()


# 실행과정
# cd ~/catkin_ws/src/beginner_tutorials
# counter_sub.py - 생성
# chmod +x scripts_sub.py - 실행권한부여
# 터미널 1 - roscore
# 터미널 2 - Publisher : rosrun beginner_tutorials counter_pub.py
# 터미널 3 - Subscriber : rosrun beginner_tutorials counter_sub.py
# 터미널 4 - 확인 : rqt_graph