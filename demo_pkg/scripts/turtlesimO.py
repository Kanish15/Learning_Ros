#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

def move_in_circle():
    rospy.init_node('move_in_circle', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
    vel_msg.linear.x = 5.0
    vel_msg.angular.z = 5.0
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        velocity_publisher.publish(vel_msg)
        rate.sleep()

    vel_msg.linear.x = 0.0
    vel_msg.angular.z = 0.0
    velocity_publisher.publish(vel_msg)

if __name__ == '__main__':
    try:
        move_in_circle()
    except rospy.ROSInterruptException:
        pass
