cmake_minimum_required(VERSION 2.8.3)
project(rbx1_urdf)

find_package(catkin REQUIRED)

catkin_package()

find_package(roslaunch)

install(DIRECTORY meshes launch rviz urdf
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})
