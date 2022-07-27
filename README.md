# RE
!The python code for ros2 is in dev_ws folder<br />
!!Before testing, you need to install ros1 (version:noetic) noetic and ros2 (version:galactic),and you need to know how to use Ros2.<br />No python(ros) file is written in ros1 in this project as ros1 is only used as a way of communicating here.<br />
!!Django has to be installed with the virual environment set up, the complete website(N1HL) is in the master branch.<br />
!The communication between ros1 and ros2 is through rosBridge web socket, more information about this can be found here:
https://wiki.ros.org/rosbridge_suite<br />
This web socket has to be installed after the ros1 is installed.


# Steps for connecting website and ros:

## 1.Open one terminal in ubuntu, run the commands below
- source /opt/ros/noetic/setup.bash
- source /opt/ros/galactic/setup.bash<br /><br />
    *messages:ROS_DISTRO was set to 'noetic' before. Please make sure that the environment does not mix paths from different distributions.*<br />
    *messages:ROS_DISTRO was set to 'galactic' before. Please make sure that the environment does not mix paths from different distributions.*<br /><br/>
- source ~/dev_ws/install/local_setup.sh
- export ROS_MASTER_URL=http://localhost:11311
- ros2 run ros1_bridge dynamic_bridge
   messages: created 2to1 bridge for topic '/rosout' with ROS 2 type 'rcl_interfaces/msg/Log' and ROS 1 type 'rosgraph_msgs/Log'


## 2.In the second terminal run:
- source /opt/ros/noetic/setup.bash
— roslaunch rosbridge_server rosbridge_websocket.launch

## 3.In the third terminal run:

- source /opt/ros/galactic/setup.bash
- ros2 run rosbridge  rosbridge_listener

## 4.In the forth terminal run:

- source /opt/ros/galactic/setup.bash
- ros2 run rosbridge room_directing

## 5.Open the website in pycharm and run the page
