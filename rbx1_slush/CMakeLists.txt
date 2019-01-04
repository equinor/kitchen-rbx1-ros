cmake_minimum_required(VERSION 2.8.3)
project(rbx1_slush)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  sensor_msgs
  std_msgs
  message_generation
)

add_service_files(DIRECTORY srv FILES RobotStatus.srv RobotJoints.srv RobotGripper.srv)
generate_messages(DEPENDENCIES std_msgs)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES rbx1_slush
#  CATKIN_DEPENDS roscpp rospy std_msgs message_runtime
#  DEPENDS system_lib
)

#catkin_python_setup()

install(PROGRAMS
     scripts/joint_command_subscriber.py
     scripts/joint_command_subscriber.py
     scripts/joint_states_publisher.py
     scripts/robot_server.py
     DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)
