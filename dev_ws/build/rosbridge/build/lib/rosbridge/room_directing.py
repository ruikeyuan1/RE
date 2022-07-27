#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@说明: ROS2话题示例-订阅“Hello World”话题消息
"""



import rclpy  # ROS2 Python interface library
from rclpy.node import Node  # ROS2 node class
from std_msgs.msg import String  # String message defined by the ROS2 standard

"""
创建一个订阅者节点
"""



class SubscriberNode(Node):
    
    def __init__(self, name):
        super().__init__(name) 
        self.sub = self.create_subscription(\
            String, "/room", self.listener_callback, 10)        # Create a subscriber object (message type, topic name, subscriber callback function, queue length)

        

    def listener_callback(self, msg):                  # Create a callback function to process the data after receiving the topic message
        self.pub = self.create_publisher(String, "roomFeedback", 10)    # Create publisher object (message type, topic name, queue length)
        msgr = String()                                        # Create a message object of type String
        msgr.data = 'Room directing...roomNumber: "%s"' % msg.data
        self.pub.publish(msgr) 
        self.get_logger().info('Ros2 received roomNumber: "%s"' % msg.data) 

        arrived = True
        if arrived == True:
            msga = String()                                        # Create a message object of type String
            msga.data = 'Arrived at room: "%s"' % msg.data
            self.pub.publish(msga) 
            self.get_logger().info('Arrived at room: "%s"' % msg.data) 
            
            

def main(args=None):                                 # ROS2 node main entry main function
    rclpy.init(args=args)                            # ROS2 Python interface initialization
    node = SubscriberNode("ros_feed")               # Create a ROS2 node object and initialize it
    rclpy.spin(node)                                 # Loop waiting for ROS2 to exit
    node.destroy_node()                              # Destroy node object
    rclpy.shutdown()                                 # Close ROS2 and PythonInterface
    
    
    
    
    
    
    
    
    
    
    
                    
    
    
    
    
    
    
