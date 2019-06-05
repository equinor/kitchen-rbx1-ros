# How to run RBX1_ROS on ROS Melodic

## Packages

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
