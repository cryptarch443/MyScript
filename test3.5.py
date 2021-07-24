from getpass import getpass
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException

username = raw_input('Enter your username: ')
password = getpass()

with open('test3.5.1') as file:
	command_file = file.read().splitlines()
with open('test3.5.2') as file:
	ip_list = file.read().splitlines()

for devices in device_list:
	print 'Connecting to ' + devices
	ip_address_of_device = ip_list
	ios_device {
		'device_type': 'cisco_ios',
		'ip': ip_address_of_device,
		'username': username,
		'password': password
	}

	try:
		net_connect = ConnectHandler(**ios_device)
	except (AuthenticationException):
		print 'Authentication Failure: ' + ip_address_of_device
		continue
	except (NetMikoTimeoutException):
		print 'Timeout to device: ' + ip_address_of_device
		continue
	except (EOFError):
		print 'End of file while attempting device ' + ip_address_of_device
		continue
	except (SSHException):
		print 'SSH issue. are you sure SSH is enabled? ' + ip_address_of_device
		continue
	except Exception as unknown_error:
		print 'Some other error: ' + ip_address_of_device
		continue

	output = net_connect.send_config_set(command_file)
	print output