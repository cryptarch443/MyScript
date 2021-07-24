#Python2.7
from netmiko import ConnectHandler
ios_R1 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.100.200',
	'username':'cisco',
	'password': 'cisco',
}
ios_R2 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.100.201',
	'username':'cisco',
	'password': 'cisco',
}
ios_R3 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.100.202',
	'username':'cisco',
	'password': 'cisco',
}
ios_R4 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.100.203',
	'username':'cisco',
	'password': 'cisco',
}
ios_R5 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.100.204',
	'username':'cisco',
	'password': 'cisco',
}

with open('test2.5') as config:
	config_lines = config.read().splitlines()

net_connect = ConnectHandler(**ios_R1)
for loopback_R1 in range(0.5):
	config_command = ['interface loopback ' + str(loopback_R1), 'ip address 1.1.1.' + str(loopback_R1) + ' 255.255.255.255']
	config_command = ['router ospf 100', 'network 1.1.1.' + str(loopback_R1) + ' 0.0.0.0 area 0']
	output = net_connect.send_config_set(config_command)
	print output

net_connect = ConnectHandler(**ios_R2)
for loopback_R2 in range(0,5):
	config_command = ['interface loopback ' + str(loopback_R2), 'ip address 2.2.2.' + str(loopback_R2) + ' 255.255.255.255']
	config_command = ['router ospf 100', 'network 2.2.2.' + str(loopback_R2) + ' 0.0.0.0 area 0']
	output = net_connect.send_config_set(config_command)
	print output

net_connect = ConnectHandler(**ios_R3)
for loopback_R3 in range(0,5):
	config_command = ['interface loopback ' + str(loopback_R3), 'ip address 3.3.3.' + str(loopback_R3) + ' 255.255.255.255']
	config_command = ['router ospf 100', 'network 3.3.3.' + str(loopback_R3) + ' 0.0.0.0 area 0']
	output = net_connect.send_config_set(config_command)
	print output

net_connect = ConnectHandler(**ios_R4)
for loopback_R4 in range(0,5):
	config_command = ['interface loopback ' + str(loopback_R4), 'ip address 4.4.4.' + str(loopback_R4) + ' 255.255.255.255']
	config_command = ['router ospf 100', 'network 4.4.4.' + str(loopback_R4) + ' 0.0.0.0 area 0']
	output = net_connect.send_config_set(config_command)
	print output

net_connect = ConnectHandler(**ios_R5)
for loopback_R5 in range(0,5):
	config_command = ['interface loopback ' + str(loopback_R5), 'ip address 5.5.5.' + str(loopback_R5) + ' 255.255.255.255']
	config_command = ['router ospf 100', 'network 5.5.5.' + str(loopback_R5) + ' 0.0.0.0 area 0']
	output = net_connect.send_config_set(config_command)
	print output

all_devices = [ios_R1, ios_R2, ios_R3, ios_R4, ios_R5]

for device in all_devices:
	net_connect = ConnectHandler(**device)
	output = net_connect.send_config_set(config_lines)
	print output