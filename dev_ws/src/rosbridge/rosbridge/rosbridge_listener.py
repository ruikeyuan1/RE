#!/usr/bin/env python3
# -*- coding: utf-8 -*-





import rclpy                                     # ROS2 Python接口库
from rclpy.node import Node                    # ROS2 节点类
from std_msgs.msg import String                  # ROS2标准定义的String消息



class SubscriberNode(Node):
    
    def __init__(self, name):
        super().__init__(name) 
        self.sub = self.create_subscription(\
            String, "/button", self.listener_callback, 10)         # Create a subscriber object (message type, topic name, subscriber callback function, queue length)

    def listener_callback(self, msg):                             # Create a callback function to process the data after receiving the topic message
        self.pub = self.create_publisher(String, "ros2pub", 10)   # Create publisher object (message type, topic name, queue length)
        msgp = String()                                            # Create a message object of type String
        msgp.data = 'Ros2 received: "%s"' % msg.data
        self.pub.publish(msgp) 
        self.get_logger().info('Ros2 received: "%s"' % msg.data)     # Output the log info, signing the topic has been published

def main(args=None):                                  # ROS2 node main entry main function
    rclpy.init(args=args)                            # ROS2 Python interface initialization
    node = SubscriberNode("topic_sub")                # Create a ROS2 node object and initialize it
    rclpy.spin(node)                                  # Loop waiting for ROS2 to exit
    node.destroy_node()                               # Destroy node object
    rclpy.shutdown()                                    # Close ROS2 and PythonInterface



           
                           
            
                              
                        
