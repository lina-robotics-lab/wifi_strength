#!/usr/bin/env python3
import rospy
import sys
from std_msgs.msg import Float32

def get_curr_wifi_strength():
	with open('/proc/net/wireless') as f:
		t=f.read()
		lines = t.split('\n')
		return float(lines[2].split()[3])

if __name__ == '__main__':
	robot_namespace='pc'
	if len(sys.argv)>1:
		robot_namespace=sys.argv[1]
	else:
		print('Using empty robot_namespace')
	rospy.init_node('{}_wifi'.format(robot_namespace),anonymous=False)
	pub = rospy.Publisher('/{}/wifi_strength'.format(robot_namespace),Float32,queue_size=10)
	rate=rospy.Rate(10)
	
	while not rospy.is_shutdown():
		pub.publish(get_curr_wifi_strength())
		rate.sleep()
		

