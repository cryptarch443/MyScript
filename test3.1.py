#Python3.6
import json
from pyntc import ntc_device as NTC
ios = NTC(host='192.168.100.200', username='cisco', password='cisco', device_type='cisco_ios_ssh')
ios.config_list(['hostname R1',
				 'router ospf 1',
				 'network 0.0.0.0 area 0'])