import netmiko
import textfsm
from pprint import pprint

cisco = {
	'device_type': 'cisco_ios',
	'ip': '192.168.100.49',
	'username': 'jawdat',
	'password': 'jawdat',
}

connect = netmiko.ConnectHandler(**cisco)

show_interface = connect.send_command('show ip interface brief')
template_file = open("path_interfaces.template")
template = textfsm.TextFSM(template_file)
result = template.ParseText(show_interface)

interface_list = list()

for list in result:
	interface_dict = dict()
	interface_dict['interface'] = list[0],
	interface_dict['ip address'] = list[1],
	interface_dict['status'] = list[2],
	interface_dict['protocol'] = list[3]
	interface_list.append(interface_dict)
pprint(interface_list)