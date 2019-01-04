#!/usr/bin/env python

import rospy
from rbx1_slush.srv import *
from rbx1 import RobotSingleton

robot = RobotSingleton.getInstance()

def handle_get_status(req):
    status = robot.getStatus()
    return RobotStatusResponse(status['currentPos'])

def handle_joint_command(req):
    robot.runRobot(req.joints)
    return RobotJointsResponse()

def handle_gripper_command(req):
    robot.runGripper(req.gripper)
    return RobotGripperResponse()

def robot_server():
    rospy.init_node('robot_server')
    rospy.Service('get_status', RobotStatus, handle_get_status)
    rospy.Service('move_joints', RobotJoints, handle_joint_command)
    rospy.Service('move_gripper', RobotGripper, handle_gripper_command)
    print "Robot service is ready to engage!"
    rospy.spin()

if __name__ == "__main__":
    robot_server()