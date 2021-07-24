#send command from file
import netmiko

cisco = {
	'device_type':'cisco_ios',
	'ip':'192.168.100.49',
	'username':'jawdat',
	'password':'jawdat',
}

connect = netmiko.ConnectHandler(**cisco)
connect.send_config_from_file(config_file = 'config.txt')
show_ip_interface = connect.send_command ("show ip interface brief")
show_routing_table = connect.send_command("show ip route")
show_protocol = connect.send_command("show ip protocol")

print (show_ip_interface)
print (show_routing_table)
print (show_protocol)