import textfsm
from pprint import pprint
import netmiko

cisco_vios = {
    'device_type': 'cisco_ios',
    'ip':   '192.168.100.39',
    'username': 'cisco',
    'password': 'cisco',
}


net_connect = netmiko.ConnectHandler(**cisco_vios)

string_interface = net_connect.send_command('show interface')

template_file = open("C:/Users/Ryuga/Automation/showinterface.template")
template = textfsm.TextFSM(template_file)
result_template = template.ParseText(string_interface)

interface_list = list()

print(string_interface)