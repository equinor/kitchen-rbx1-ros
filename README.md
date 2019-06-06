# RBX1 - ROS
ROS packages for the RBX1 remix.
![Gazebo simulator](../assets/gazebo.png?raw=true)

## User Guide
* Have rbx1_ros installed on a RPi (Raspberry Pi) connected to RBX1. Follow guide, *Getting started - RPi*, if no RPi has been set up yet.
* Power up RPi. Log in.
* Open a terminal window and get ip address with command, `ifconfig`.
* Initalize ROS by running commands: 
  ```sh
  cd ~/catkin_ws
  source devel/setup.bash
  roslaunch rbx1_slush slush.launch
  ```
* You can verify that ROS runs correctly by opening a new terminal window and using command `rostopic list`, which returns a list of topics. For instance, */joint_states*, and */rbx1_joint_controller/command*.
* Download and run [rbx1_unity](https://github.com/equinor/rbx1_unity/releases) on a computer connected to the same network as the RPi.
* Enter ip address.


## Getting started - Dev
Packages based on ROS Kinetic which targets Ubuntu 16.04. Packages might not work properly with newer releases of ROS.

* Install [ROS](http://wiki.ros.org/kinetic/Installation/Ubuntu)

* Install [Gazebo](http://gazebosim.org/tutorials?tut=install_ubuntu)

* Install ros package dependencies, [timed_roslaunch](http://wiki.ros.org/timed_roslaunch), [cv_camera](http://wiki.ros.org/cv_camera), and [rosbridge_suite](http://wiki.ros.org/rosbridge_suite):
```sh
sudo apt update
sudo apt install \
  ros-kinetic-timed-roslaunch \
  ros-kinetic-cv-camera \
  ros-kinetic-rosbridge-server
```

* Create a [catkin workspace](http://wiki.ros.org/catkin/Tutorials/create_a_workspace). Typically at `~/catkin_ws`:
```sh
mkdir -p ~/catkin_ws/src
```

* Clone repository inside `src` folder:
```sh
git clone https://github.com/equinor/rbx1_ros
```

* Also clone `git clone https://github.com/roboticsgroup/roboticsgroup_gazebo_plugins.git` to the src folder.
* Build packages with catkin:
```sh
cd ~/catkin_ws
catkin_make
```

* This results in a new build and devel folder. Before continuing you need to source the workspace's `setup.bash` file:
```sh
source devel/setup.bash
```

* ROS should now be able to find and run your packages.



## Getting started - RPi
* Install [Ubiquity](https://downloads.ubiquityrobotics.com) RPi Lubuntu image on a RPi. The image has ROS preinstalled.
* Connect to a [network](./pi-network-configuraton.md)
* Clone repo in `catkin_ws/src`.
* Delete the `rbx1_urdf` folder.
* Install SlushEngine:
  ```sh
  sudo wget https://raw.githubusercontent.com/olavvatne/slushengine/master/install.pl -O - | perl
  ```

* Run `catkin_make` and `source devel/setup.bash`.
* Start robot: `roslaunch rbx1_slush slush.launch`



## Packages
### rbx1_urdf
URDF description of the RBX1 remix 6 axis robot. Based on [moveo_urdf](https://github.com/jesseweisberg/moveo_ros/tree/master/moveo_urdf).

To view the model in Rviz:
```sh
roslaunch rbx1_urdf display.launch
```

To view the model in Gazebo:
```sh
roslaunch rbx1_urdf gazebo.launch
```

### rbx1_slush
Ros wrapper for SlushEngine and the physical robot. If run on a RPi, SlushEngine will be used to communicate with the board. On a dev machine a mock robot implementation will be started instead.


### rbx1_control
Package contains everything related to robot control. Contains config files for joints and gripper and launch files for both real and simulated RBX1.

To launch the model with ROS controllers:
```sh
roslaunch rbx1_urdf rbx1.launch
```

Move the robot by publishing to the `/rbx1_joint_controller/command` topic:
```sh
rostopic pub  /rbx1_joint_controller/command std_msgs/Float64MultiArray "layout:
  dim:
  - label: ''
    size: 6
    stride: 1
  data_offset: 0
data: [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]"
```

To move gripper use this command:
```sh
rostopic pub  /rbx1_gripper_controller/command std_msgs/Float64MultiArray "layout:
  dim:
  - label: ''
    size: 2
    stride: 1
  data_offset: 0
data: [1.0, -1.0]"
```