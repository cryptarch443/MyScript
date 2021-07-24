vendor = set(['cisco','mikrotik','cisco','juniper','arista'])
hostname = ('R1','R2','R3','R4')
ip_address = ('1.1.1.1/30','1.1.1.2/30','1.1.1.3/30','1.1.1.4/30')
version = ('12.1','13.1','14.1','15.1')

devices = {'vendor': vendor, 'hostname': hostname, 'ip': ip_address, 'version': version}

for key, value in devices.items():
	print(key + ': ' + value)

device = {'vendor': 'cisco', 'hostname': 'Router', 'ip': '192.168.100.147', 'version': 'NX-OS9K'}

for key, value in device.items():
	print(key + ': ' + value)

desc = tuple(['cisco','NX-OS9K'])

hostname = 'CCC'

if hostname == 'NYC':
	print('The hostname is NYC')
elif hostname != 'NYC':
	print('This not NYC')
else:
	print('i don\'t know')

interface = ['fa0/0','fa0/1','fa0/2']
vrf = ['red','green','blue']
for arp in range(len(interface)):
	print('show arp vrf ' + interface[arp] + ' ' + vrf[arp])