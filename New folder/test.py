import netmiko
cisco_vios = {
    'device_type': 'cisco_ios',
    'ip':   '192.168.100.39',
    'username': 'cisco',
    'password': 'cisco',
}

net_connect = netmiko.ConnectHandler(**cisco_vios)
net_connect.config_mode()
net_connect.send_command('int gig 0/1')
net_connect.send_command('ip add 10.12.13.32 255.255.255.252')
net_connect.send_command('no sh')
net_connect.exit_config_mode()
output = net_connect.send_command('show ip int br')

print(output)