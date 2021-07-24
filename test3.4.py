from getpass import getpass
from netmiko import ConnectHandler

username = raw_input('Enter your SSH username: ')
password = getpass()

with open('test3.4.1') as file:
	command_list = file.read().splitlines()
with open('test3.4.2') as file:
	ip_list = file.read().splitlines()

for devices in device_list:
	print 'Connecting to ' + devices
	ip_address_device = devices
	ios_device = {
		'device_type': 'cisco_ios',
		'ip': ip_address_device,
		'username': username,
		'password': password
	}

	net_connect = ConnectHandler(**ios_device)
	output = net_connect.send_config_set(command_list)
	print output