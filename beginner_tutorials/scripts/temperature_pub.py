#!/usr/bin/env python3

import rospy
import random
from std_msgs.msg import Float32

def temperature_publisher():
    rospy.init_node('temperature_pub')

    pub = rospy.Publisher('temperature', Float32, queue_size=10)

    rate = rospy.Rate(1)  # 1Hz

    while not rospy.is_shutdown():
        temp = random.uniform(20.0, 40.0)
        rospy.loginfo("현재 온도: %.2f", temp)
        pub.publish(temp)
        rate.sleep()

if __name__ == '__main__':
    try:
        temperature_publisher()
    except rospy.ROSInterruptException:
        pass