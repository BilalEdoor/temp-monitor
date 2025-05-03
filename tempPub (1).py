#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32
import random

def temp_publisher():
    pub = rospy.Publisher('room_temp', Float32, queue_size=10)
    rospy.init_node('TempPub', anonymous=True)
    rate = rospy.Rate(5)  # 1 Hz

    while not rospy.is_shutdown():
        temp_celsius = random.uniform(5.0, 30.0)
        rospy.loginfo(f"Publishing Temperature in Celsius: {temp_celsius:.2f}")
        pub.publish(temp_celsius)
        rate.sleep()

if __name__ == '__main__':
    try:
        temp_publisher()
    except rospy.ROSInterruptException:
        pass
