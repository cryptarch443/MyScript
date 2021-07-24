#Python and Telnet Configure Switch VLANs, Loopback, and ospf With Looping
#Python 2.7
import getpass
import sys
import telnetlib

HOST = "192.168.100.23"
user = raw_input("Enter your telnet account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")
tn.write(user + "\n")
if password:
	tn.read_until("Password: ")
	tn.write(password + "\n")

tn.write("enable\n")
tn.write("cisco\n")
tn.write("configure terminal\n")
for vlan in range(2,11):
	tn.write("vlan " + "str(vlan)" + "\n")
	tn.write("name Python_VLAN_" + "str(vlan)" + "\n")
for loopback in range(1,11):
	tn.write("interface loopback " + "str(loopback)" + "\n")
	tn.write("ip address 1.1.1." + "str(loopback)" + " 255.255.255.255" + "\n")
tn.write("ip routing\n")
for ospf in range(1,11):
	tn.write("router ospf 1\n")
	tn.write("network 1.1.1." + "str(ospf)" + " 0.0.0.0 area 0" + "\n")
tn.write("end\n")
tn.write("exit\n")

print tn.read_all()