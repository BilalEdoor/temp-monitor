#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32

def callback(data):
    fahrenheit = (data.data * 9.0 / 5.0) + 32.0
    rospy.loginfo(f"Temperature in Fahrenheit: {fahrenheit:.2f}")

def fehre_subscriber():
    rospy.init_node('FehreSub', anonymous=True)
    rospy.Subscriber('room_temp', Float32, callback)
    rospy.spin()

if __name__ == '__main__':
    fehre_subscriber()
