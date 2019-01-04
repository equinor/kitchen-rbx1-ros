#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64MultiArray
from rbx1_slush.srv import *

def move_joints(positions):
    rospy.wait_for_service('move_joints')
    try:
        move_joints = rospy.ServiceProxy('move_joints', RobotJoints)
        move_joints(positions)
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def callback(data):
    move_joints(data.data)
    rospy.loginfo("I receive %s", data.data)

def joint_command_subscriber():
    rospy.init_node('joint_command_subscriber')
    rospy.Subscriber('/rbx1_joint_controller/command', Float64MultiArray, callback)
    rospy.spin()

if __name__=='__main__':
    joint_command_subscriber()