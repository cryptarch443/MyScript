#Python3.6
#NAPALM to compare multiple files and devices
import json
from napalm import get_network_driver

device_list = ['192.168.100.200', '192.168.100.201', '192.168.100.202']

for ip_address in device_list:
	print ('Connecting to ' + str(ip_address))
	driver = get_network_driver('ios')
	devices = driver('device_list', 'cisco', 'cisco')
	devices.open()
	
	devices.load_merge_candidate(filename='test3.0.1.cfg')
	diffs = devices.compare_config()
	if len(diffs) > 0:
		print(diffs)
		devices.commit_config()
	else:
		print('No ACL changes required.')
		devices.discard_config()

	devices.load_merge_candidate(filename='test3.0.2.cfg')
	diffs = devices.compare_config()
	if len(diffs) > 0:
		print(diffs)
		devices.commit_config()
	else:
		print('No BGP changes required.')
		devices.discard_config()

	devices.close()