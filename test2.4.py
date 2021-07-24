#Python2.7
from netmiko import ConnectHandler

iosl2_1 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.100.200',
	'username': 'cisco',
	'password': 'cisco',
}
iosl2_2 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.100.201',
	'username': 'cisco',
	'password': 'cisco',
}
iosl2_3 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.100.202',
	'username': 'cisco',
	'password': 'cisco',
}

all_device = [iosl2_1, iosl2_2, iosl2_3]

for device in all_device:
	net_connect = ConnectHandler(**device)
	for vlan in range(2,11):
		print 'Creating VLAN ' + str(vlan):
		config_command = ["vlan " + str(vlan), 'Name Python_VLAN ' + str(vlan)]
		output = net_connect.send_config_set(config_command)
		print output