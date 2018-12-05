# RBX1 - ROS
ROS packages for the RBX1 remix

## Getting started
Packages based on ROS Kinetic which targets Ubuntu 16.04. Packages might not work properly with newer releases of ROS.

* Install [ROS](http://wiki.ros.org/kinetic/Installation/Ubuntu)
* Install [Gazebo](http://gazebosim.org/tutorials?tut=install_ubuntu)
* Create a [catkin workspace](http://wiki.ros.org/catkin/Tutorials/create_a_workspace). Typically at `~/catkin_ws`
```sh
mkdir -p ~/catkin_ws/src
```
* Clone repository inside `src` folder
```sh
git clone https://github.com/Statoil/rbx1_ros
```
* Build packages with catkin
```sh
cd ~/catkin_ws
catkin_make
```
* This results in a new build and devel folder. Before continuing you need to source the workspace's `setup.bash` file.
```sh
source devel/setup.bash
catkin_make
```
* ROS should now be able to find and run your packages

## Packages
### rbx1_urdf
URDF description of the rbx1 remix 6. axis robot. Based on [moveo_urdf](https://github.com/jesseweisberg/moveo_ros/tree/master/moveo_urdf)

To view the model in Rviz:
```sh
roslaunch rbx1_urdf display.launch
```

To view the model in Gazebo:
```sh
roslaunch rbx1_urdf gazebo.launch
```

<!-- ## Areas to improve
### URDF model
* Inertia parameters
* Center of mass of some links
* Reduce polygon count of meshes -->