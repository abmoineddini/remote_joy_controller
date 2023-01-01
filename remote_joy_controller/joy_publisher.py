import socket
import time
from sensor_msgs.msg import Joy
import rclpy
from rclpy.node import Node

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip=socket.gethostbyname("192.168.137.200")
port=80
address=(ip,port)
client.connect(address) 

class JoyNode(Node):
    def __init__(self) -> None:
        super().__init__("joy_node")
        client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        ip=socket.gethostbyname("192.168.137.200")
        port=80
        address=(ip,port)
        client.connect(address) 
        self.pub_ = self.create_publisher(Joy, "/joy", 10)
        self.timers_ = self.create_timer(0.02, self.publisher_data)
        self.declare_parameter("device_id", 0)
    

    def publisher_data(self):
        msg = Joy()
        msg.header.stamp = Node.get_clock(self).now().to_msg()
        msg.header.frame_id = "joy"
        data = client.recv(1024)
        data = data.decode()
        try:
            data = data.split(":") 
            data = data[1].split(",")
            Axis = [float(data[0]), float(data[1]), float(data[2]), float(data[3])]
            buttons= [int(data[4]), int(data[5]), int(data[6]), int(data[7])]
            msg.axes = Axis
            msg.buttons = buttons
            self.pub_.publish(msg)
        except:
            pass

def main(arg=None):
    rclpy.init(args=arg)
    node = JoyNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()
