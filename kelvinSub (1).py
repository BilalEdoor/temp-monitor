#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32

def callback(data):
    kelvin = data.data + 273.15
    rospy.loginfo(f"Temperature in Kelvin: {kelvin:.2f}")

def kelvin_subscriber():
    rospy.init_node('KelvinSub', anonymous=True)
    rospy.Subscriber('room_temp', Float32, callback)
    rospy.spin()

if __name__ == '__main__':
    kelvin_subscriber()
