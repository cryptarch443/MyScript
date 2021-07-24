import textfsm
from pprint import pprint

string_interface = '''
vIOS-PK-02#show ip int brief 
Interface                  IP-Address      OK? Method Status                Protocol
GigabitEthernet0/0         192.168.100.33  YES DHCP   up                    up      
GigabitEthernet0/1         3.3.3.3         YES manual up                    up      
GigabitEthernet0/2         4.4.4.4         YES manual up                    up      
GigabitEthernet0/3         unassigned      YES NVRAM  administratively down down    
Loopback0                  unassigned      YES manual up                    up      
Loopback2                  unassigned      YES unset  up                    up      
Loopback3                  1.1.1.1         YES manual up                    up      
Loopback4                  unassigned      YES unset  up                    up      
Loopback5                  unassigned      YES unset  up                    up 
'''

path_template = 'interface.template'
template_file = open(path_template)

template = textfsm.TextFSM(template_file)
result_template = template.ParseText(string_interface)

interface_list = list()


for d in result_template:
	interface_dict = dict()

	interface_dict['interface'] = d[0]
	interface_dict['address'] = d[1]
	interface_dict['status'] = d[2]
	interface_dict['protocol'] = d[3]

	interface_list.append(interface_dict)

pprint(interface_list)