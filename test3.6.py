from getpass import getpass
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException

username = raw_input('Enter your username: ')
password = getpass()

with open('test3.6.1') as file:
	command_switch = file.read().splitlines()
with open('test3.6.2') as file:
	command_router = file.read().splitlines()
with open('test3.6.3') as file:
	ip_list = file.read().splitlines()

for devices in all_device:
	print ('Connecting to ') + devices
	ip_address_of_device = ip_list
	ios_device = {
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

	#Version of devices
	list_version = ['ver1',
					'ver2',
					]

	#Check software versions
	for software_version in list_version:
		print 'Checking for ' + software_version
		output_version = net_connect.send_command('show version')
		int_version = 0 #Reset integer value
		int_version = output_version.find(software_version) #Check software version
		if int_version > 0:
			print 'Software version found: ' + software_version
			break
		else:
			print 'Did no find ' + software_version

		if software_version == 'ver1':
			print 'Running ' + software_version + 'command'
			output = net_connect.send_config_set(command_switch)
		elif software_version == 'ver2'
			print 'Running ' + software_version + 'command'
			output = net_connect.send_config_set(command_router)
		print output