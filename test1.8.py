#Python and Telnet Configure Switch VLANs
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
tn.write("vlan10\n")
tn.write("name python_vlan_10\n")
tn.write("vlan20\n")
tn.write("name python_vlan_20\n")
tn.write("vlan30\n")
tn.write("name python_vlan_30\n")