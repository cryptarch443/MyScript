#Python3.6
#NAPALM configure with configuration files
import json
from napalm import get_network_driver

driver = get_network_driver('ios')
iosl2 = driver('192.168.100.200', 'cisco', 'cisco')
iosl2.open()

print ('Accessing 192.168.100.200')
iosl2.load_merge_candidate(filename='test2.8.cfg')
iosl2.commit_config()
iosl2.close()