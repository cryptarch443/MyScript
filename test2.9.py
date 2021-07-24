#Python3.6
#NAPALM to compare configuration
import json
from napalm import get_network_driver

driver = get_network_driver('ios')
iosR1 = driver('192.168.100.200', 'cisco', 'cisco')
iosR1.open()

print ('Accessing 192.168.100.200')
iosR1.load_merge_candidate(filename='test2.9.cfg')

diffs = iosR1.compare_config()
if len(diffs) > 0:
	print(diffs)
	iosR1.commit_config()
else:
	print('No Change required.')
	iosR1.discard_config()

iosR1.close()