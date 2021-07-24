#Python3.6
from netmiko import ConnectHandler

with open('test3.3.1') as file:
	ip_list = file.read().splitlines()
with open('test3.3.2') as file:
	command_file = file.read().splitlines()

for devices in ip_list:
	print 'Connecting to device ' + devices
	ip_address_of_device = devices
	ios_device = {
		'device_type': 'cisco_ios',
		'ip': ip_address_of_device,
		'username': 'cisco',
		'password': 'cisco'
	}

	net_connect = ConnectHandler(**ios_device)
	output = net_connect.send_config_set(command_file)
	print output