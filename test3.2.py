#Python3.6
#Backup configuration with pyntc
import json
from pyntc import ntc_device as NTC
ios = NTC(host='192.168.100.200', username='cisco', password='cisco', device_type='cisco_ios_ssh')
ios.open()

show_run = ios.running_config

HOST = '192.168.100.200'
saveoutput = open('Router ' + HOST, 'w')
saveoutput.write(show_run)
saveoutput.close