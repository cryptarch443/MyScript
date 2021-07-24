#Python2.7
from netmiko import ConnectHandler

iosl2 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.100.200',
	'username': 'cisco',
	'password': 'cisco',
}

net_connect = ConnectHandler(**iosl2)
output = net_connect.send_command('show ip interface brief')
print output

config_command = ['interface loopback 0', 'ip address 1.1.1.1 255.255.255.255']
output = net_connect.send_config_set(config_command)
print output

for vlan in range (2,21):
	print "Creating VLAN " + str(vlan)
	config_command = ['vlan ' + str(vlan), 'Name Python_VLAN ' + str(vlan)]
	output = net_connect.send_config_set(config_command)
	print output
