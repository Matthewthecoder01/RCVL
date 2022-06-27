from socket import MsgFlag
import sys #lets us take argument from command line 
import rclpy #provides us API 
import csv




#laserscan topics 
from rclpy.qos import qos_profile_sensor_data, QoSProfile
from sensor_msgs.msg import LaserScan
from rclpy.qos import ReliabilityPolicy, QoSProfile


#tf topics 
import tf2_py
from rclpy.node import Node
from tf2_ros.buffer import Buffer
from tf2_ros.transform_listener import TransformListener

#not sure yet 
from std_msgs.msg import String
from std_msgs.msg import Int16MultiArray
from geometry_msgs.msg import Twist
from ros2topic.api import get_msg_class


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        scann = LaserScan()
        qos = QoSProfile(depth=10,reliability=ReliabilityPolicy.BEST_EFFORT)
        node = rclpy.create_node('scan_listener')
        sub = self.create_subscription(LaserScan,'scan',self.listener_callback,qos_profile=qos_profile_sensor_data)
        message_type = get_msg_class(self, 'scan', include_hidden_topics=True)
        print('Message type:', message_type)
        qos_policy = rclpy.qos.QoSProfile(reliability=rclpy.qos.ReliabilityPolicy.BEST_EFFORT, history=rclpy.qos.HistoryPolicy.KEEP_LAST, depth=1)
        self.subscriber_= self.subscription = self.create_subscription(LaserScan, 'scan', self.listener_callback, qos_profile=qos_policy)
        


        self.subscriber_  # prevent unused variable warning

    def listener_callback(self,msg):
        
        print(msg.ranges[0])

        self.array = Int16MultiArray()
 
   

def main(args=None):
    rclpy.init(args=args) #initalises ros2
    minimal_subscriber = MinimalSubscriber() #class initlizaed 
    rclpy.spin(minimal_subscriber) #process data from node 
    minimal_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    print('Starting scan listener')
    main()
    
