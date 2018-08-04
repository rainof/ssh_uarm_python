#!/usr/bin/env python3
# Software License Agreement (BSD License)
#
# Copyright (c) 2018, UFactory, Inc.
# All rights reserved.
#
# Author: Vinman <vinman.wen@ufactory.cc> <vinman.cub@gmail.com>

import rospy
from std_msgs.msg import String
import os
import sys
import time
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
from uarm.wrapper import SwiftAPI
from uarm.swift import Pump

swift = SwiftAPI(filters={'hwid': 'USB VID:PID=2341:0042'}, callback_thread_pool_size=1)
grip = Pump()
swift.waiting_ready()
device_info = swift.get_device_info()
print(device_info)

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    
    # ADD CONDITION
        # ADD STATEMENT
        
    if data.data == 'red':
        print("Goto RED")
        swift.set_position(x=300, y=0, z=50)
    elif data.data == 'blue':
        print("Goto BLUE")
        swift.set_position(x=300, y=150, z=50)
    elif data.data == 'yellow':
        print("Goto YELLOW")    
        swift.set_position(x=300, y=-150, z=50)
    else:
        print("Can't move")
        swift.set_position(x=150, y=0, z=50)


def listener():
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('detect_color', String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
