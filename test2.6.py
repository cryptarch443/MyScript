#Python3.6
import json
from napalm import get_network_driver

driver = get_network_driver('ios')
iosl3 = driver('192.168.100.200', 'cisco', 'cisco')
iosl3.open()

ios_output = iosl3.get_facts()
print (json.dumps(ios_output, indent=4))

ios_output = iosl3.get_interfaces()
print (json.dumps(ios_output, sort_keys=True, indent=4))

ios_output = iosl3.get_interfaces_counters()
print (json.dumps(ios_output, sort_keys=True, indent=4))

ios_output = iosl3.get_arp_table()
print (json.dumps(ios_output, indent=4))

ios_output = iosl3.ping('5.5.5.4')
print (json.dumps(ios_output, indent=4))

ios_output = iosl3.traceroute('5.5.5.4')
print (json.dumps(ios_output, indent=4))

bgp_neighbors = iosl3.get_bgp_neighbors()
print (json.dumps(bgp_neighbors, indent=4))