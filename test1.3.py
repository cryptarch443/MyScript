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

show_interface = connect.send_command('show interface')
template_file = open("test1.3.template")
template = textfsm.TextFSM(template_file)
result = template.ParseText(show_interface)

interface_list = list()

for list in result:
	interface_dict = dict()
	interface_dict['name'] = list[0]
	interface_dict['mac'] = list[1]
	interface_dict['ip'] = list[2]
	interface_dict['mtu'] = list[3]
	interface_dict['bandwith'] = list[4]
	interface_list.append(interface_dict)
pprint(interface_list)