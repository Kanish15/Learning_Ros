#!/usr/bin/env python3
import rospy 
from std_msgs.msg import String

def node_pub():
    pub = rospy.Publisher('Topic_2', String, queue_size=10)
    rate = rospy.Rate(10)
    
    while not rospy.is_shutdown():
        msg = "Node_2 is sending data on Topic_2"
        pub.publish(msg)
        rospy.loginfo(msg)
        rate.sleep()

def node_callback(msg):
    rospy.loginfo(msg)

if __name__ == '__main__':
    rospy.init_node('Node_2')
    rospy.loginfo("NODE 2 has started .....")
    
    node = rospy.Subscriber('Topic_1', String, callback=node_callback)
    
    
    node_pub()

    rospy.spin()
