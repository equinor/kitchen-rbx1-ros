# How to run RBX1_ROS on ROS Melodic

This document will focus on the differences for setting up RBX1_ROS on Melodic when following the install guide as provided for Kinetic.

## Prerequisites

- Ubuntu-18.04
- ROS Melodic

## Getting started - Dev

### Install ROS package dependencies

```
sudo apt update
sudo apt install \
  ros-melodic-cv-camera \
  ros-melodic-rosbridge-server
```
The ROS package `timed-roslaunch` has not yet been released for any other distros, but a [release for Melodic is in progress](https://github.com/
MoriKen254/timed_roslaunch/issues/15)  

_Workaround_  
```
cd your_ros_workspace/src
git clone -b melodic-devel https://github.com/MoriKen254/timed_roslaunch.git
```

## Getting started - RPi

Note - Ubiquity use ROS Kinetic.

* Install [Ubiquity](https://downloads.ubiquityrobotics.com) RPi Lubuntu image on a RPi. The image has ROS preinstalled.
* Connect to a network.
* Clone repo in `your_ros_workspace/src`.
* Delete the `rbx1_urdf` folder.
* (Melodic) Delete the `your_ros_workspace\src\timed-roslaunch` folder (as this is just a Melodic workaround for our local dev machine)
* Install SlushEngine:
  ```sh
  sudo wget https://raw.githubusercontent.com/olavvatne/slushengine/master/install.pl -O - | perl
  ```

* Run `catkin_make` and `source devel/setup.bash`.
* Start robot: `roslaunch rbx1_slush slush.launch`