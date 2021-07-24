#Python3.6
#NAPALM to connecting multiple devices
import json
from napalm import get_network_driver

neighbor_list = ['192.168.100.200','192.168.100.201']

for ip_address in neighbor_list:
	print ('Connecting to ' + str(ip_address))
	driver = get_network_driver('ios')
	ios_router = driver(ip_address, 'cisco', 'cisco')
	ios_router.open()
	neighbor = ios_router.get_bgp_neighbors()
	print (json.dumps(neighbor, indent=4))
	ios_router.close()