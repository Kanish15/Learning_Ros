#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg  import Pose

def pose_callback(msg):
    rospy.loginfo(msg)

    
def draw():
   

    node = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(2)

    move = Twist()
    move.linear.x = 5.0

    rotate = Twist()
    rotate.angular.z = 1.57

    for _ in range(5):
        node.publish(move)
        rospy.sleep(4)
        node.publish(rotate)
        rospy.sleep(4)

    rospy.spin()


if __name__ == '__main__':
  rospy.init_node('square')
rospy.loginfo('Node has started .....')
rospy.loginfo('Node has started .....')
sub = rospy.Subscriber("/turtle1/pose", Pose, callback=pose_callback)
draw()
