#Python and Telnet Configure Cisco Router
#Python 2.7
import getpass
import sys
import telnetlib

HOST = "192.168.100.50"
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
tn.write("interface loopback 1\n")
tn.write("ip address 1.1.1.1 255.255.255.255\n")
tn.write("router ospf 1\n")
tn.write("router-id 1.1.1.1\n")
tn.write("network 1.1.1.1 0.0.0.0 area 0\n")
tn.write("end\n")
tn.write("exit\n")
tn.write("write\n")

print tn.read_all()