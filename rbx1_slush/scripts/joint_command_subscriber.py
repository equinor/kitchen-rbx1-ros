#!/usr/bin/env python

import rospy

from std_msgs.msg import Float64MultiArray
from rbx1 import RobotSingleton

def callback(data):
    robot = RobotSingleton.getInstance()
    robot.runRobot(data.data)
    rospy.loginfo("I receive %s", data.data)

def joint_command_subscriber():
    rospy.init_node('joint_command_subscriber')
    rospy.Subscriber('/rbx1_joint_controller/command', Float64MultiArray, callback)
    rospy.spin()

if __name__=='__main__':
    joint_command_subscriber()