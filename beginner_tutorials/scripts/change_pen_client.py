#!/usr/bin/env python3

import rospy
from turtlesim.srv import SetPen

def change_pen(r, g, b, width):

    rospy.wait_for_service('/turtle1/set_pen')

    try:

        set_pen = rospy.ServiceProxy('/turtle1/set_pen', SetPen)

        set_pen(r, g, b, width, 0)

        rospy.loginfo("펜 변경: R=%d G=%d B=%d 두께=%d", r, g, b, width)

    except rospy.ServiceException as e:

        rospy.logerr("실패: %s", e)

if __name__ == '__main__':

    rospy.init_node('change_pen_client')

    #change_pen(0, 255, 0, 5)
    change_pen(255, 255, 0, 5)


# 코드와 같은 의미 == rosservice call /turtle1/set_pen 255 0 0 5 0

# Python 코드 → 프로그램(노드) 안에서 서비스 호출
# rosservice call → 터미널에서 직접 서비스 호출
# 즉 기능은 같지만 사용 방식이 다릅니다.