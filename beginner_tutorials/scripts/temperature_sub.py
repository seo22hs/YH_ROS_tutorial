#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float32

def callback(data):
    temp = data.data
    rospy.loginfo("수신 온도: %.2f", temp)

    if temp >= 35.0:
        rospy.logwarn("⚠ 경고! 고온 감지: %.2f", temp)

def temperature_subscriber():
    rospy.init_node('temperature_sub')

    rospy.Subscriber('temperature', Float32, callback)

    rospy.spin()

if __name__ == '__main__':
    temperature_subscriber()