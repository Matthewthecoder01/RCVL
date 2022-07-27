#!/usr/bin/env python
"""
Script to move Turtlesim in a circle
"""

import rclpy 
from rclpy.node import Node
from geometry_msgs.msg import Twist



class publisher_vel(Node):

    def __init__(self):
        super().__init__('cmd_vel_subscriber')
        self.publisher = self.create_publisher(Twist,'cmd_vel', 10)
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = Twist()
        msg.linear.x=0.1
        msg.angular.z= 0.5 
        self.publisher.publish(msg)



def main(args=None):
    rclpy.init(args=args)

    publisher_obj= publisher_vel()

    rclpy.spin(publisher_obj)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    publisher_obj.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
