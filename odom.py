import sys #lets us take argument from command line 
import rclpy #provides us API 
from rclpy.node import Node
from std_msgs.msg import String
from std_msgs.msg import Int16MultiArray
from nav_msgs.msg import Odometry
import array 
import numpy as np
import numpy as argsort
from geometry_msgs.msg import Twist
from ros2topic.api import get_msg_class


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('py_sub_spiral_node')
        message_type = get_msg_class(self, 'odom', include_hidden_topics=True)
        print('Message type:', message_type)
        self.subscriber_ = self.create_subscription(Odometry, '/odom',self.listener_callback, 10)
        self.subscriber_  # prevent unused variable warning

    def listener_callback(self,msg):
        """
        Callback function.
        """
        #dtype = [('xcoords', np.float64), ('ycoords', np.float64), ('zcoords', np.float64), ('Axcoords', np.float64), ('Aycoords', np.float64), ('Azcoords', np.float64),('sec', np.int32), ('nanosec', np.int32)]

        #structuredArr= np.array([(msg.Twist.Twist.linear.x), (msg.Twist.Twist.linear.y),(msg.Twist.Twist.linear.z), (msg.Twist.Twist.angular.x),(msg.Twist.Twist.angular.y),(msg.Twist.Twist.angular.z),(msg.header.stamp.sec),(msg.header.stamp.nanosec)], dtype=dtype)
        #np.savetxt('struc_array.csv', structuredArr, delimiter=',', fmt=['%f' , '%f', '%f','%f','%f','%f','%d','%d'], header='Xcoords,Ycoords,Zcoords,AXcoords,AYcoords,AZcoords,seconds,nanoseconds', comments='')
        
        x=msg.linear.x
        y=msg.linear.y
        z=msg.linear.z 
        a=msg.angular.x
        b=msg.angular.y
        c=msg.angular.z

        
        print(x,y,z,a,b,c)

        self.array = Int16MultiArray()

 

def main(args=None):
    rclpy.init(args=args) #initalises ros2
    minimal_subscriber = MinimalSubscriber() #class initlizaed 
    rclpy.spin(minimal_subscriber) #process data from node 
    minimal_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
    