#!/usr/bin/env python3

import rospy 
from std_msgs.msg import String

def node_callback(msg):
 rospy.loginfo(msg)

if __name__ == '__main__':

   rospy.init_node('Node_3')
 
   rospy.loginfo("Node_3 has started .....")

   sub = rospy.Subscriber('Topic_2', String , callback= node_callback)

   rospy.spin()




