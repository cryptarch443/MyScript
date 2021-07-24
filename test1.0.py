#send configuration & Reguler Expresion
import netmiko
import re

cisco = {
	'device_type': 'cisco_ios',
	'ip': '192.168.100.40',
	'username': 'jawdat',
	'password': 'jawdat',
}

net_connect = netmiko.ConnectHandler(**cisco)
#net_connect.config_mode()
net_connect.send_config_set("interface loopback 0\n ip address 123.45.67.8 255.255.255.255\n no shutdown")
#net_connect.send_command("ip address 123.45.67.8 255.255.255.255")
#net_connect.send_command("no shutdown")
#net_connect.exit_config_mode()
interface = net_connect.send_command("show ip interface brief")
show_interface = net_connect.send_command("show interface loopback 0")
version = net_connect.send_command("show version")
version_re = re.compile(r'Version \S[^,]+')
ver = version_re.search(version)

print (interface)
print (show_interface)

if ver:
	print(ver.group())