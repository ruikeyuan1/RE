# RE

!!Before testing, you need to install ros1 (version:noetic) noetic and ros2 (version:galactic),and you need to know how to use Ros2, No python(ros) file is written in ros1 in this project as ros1 is only used as a way of communicating here.
!!Django has to be installed with the virual environment set up, the complete website(N1HL) is in the master branch.

Steps for connecting website and row:

1.Open one terminal in ubuntu, run the commands below
——source /opt/ros/noetic/setup.bash
——source /opt/ros/galactic/setup.bash
    messages:ROS_DISTRO was set to 'noetic' before. Please make sure that the environment does not mix paths from different distributions.
    messages:ROS_DISTRO was set to 'galactic' before. Please make sure that the environment does not mix paths from different distributions.
——source ~/dev_ws/install/local_setup.sh
——export ROS_MASTER_URL=http://localhost:11311
——ros2 run ros1_bridge dynamic_bridge
   messages: created 2to1 bridge for topic '/rosout' with ROS 2 type 'rcl_interfaces/msg/Log' and ROS 1 type 'rosgraph_msgs/Log'


2.In the second terminal run:
——source /opt/ros/noetic/setup.bash
——roslaunch rosbridge_server rosbridge_websocket.launch

3.In the third terminal run:
——source /opt/ros/galactic/setup.bash
——ros2 run rosbridge  rosbridge_listener

4.In the forth terminal run:
——source /opt/ros/galactic/setup.bash
——ros2 run rosbridge room_directing

5.Open the website in pycharm and run the page
