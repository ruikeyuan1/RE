# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
import socket
from rclpy.node import Node

from std_msgs.msg import String


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        host = ''
        port = 1236
        iphere = (host, port)
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((iphere))
        server_socket.listen(5)
        while True:
            try:
                conn, address = server_socket.accept()
                output = String()
                output.data = conn.recv(2048).decode()
                if output:
                    if output.data == "FWD":
                        msg = String()
                        msg.data = "FORWARDS"
                        self.publisher_.publish(msg)
                        self.get_logger().info('Publishing: "%s"' % msg.data)
                        conn.send("The robot has moved forwards".encode())
                    elif output.data == "BCK":
                        print('BACK')
                    else:
                        print("")
            finally:
                conn.close()

def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
