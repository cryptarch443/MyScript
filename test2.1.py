#Get Config
#Python2.7
import getpass
import sys
import telnetlib

#Ask for username and password
user = raw_input("Enter your telnet account: ")
password = getpass.getpass()

#Open a file called
ip_list = open("test2.1")

#Telnet to device and get the running-config
for switch in ip_list:
	print "Getting running-config from Switch " + (switch)
	HOST = switch.strip()
	tn = telnetlib.Telnet(HOST)
	
	tn.read_until("Username: ")
	tn.write(user + "\n")
	if password:
		tn.read_until("Password: ")
		tn.write(password + "\n")
	
	tn.write("enable\n")
	tn.write("cisco\n")
	tn.write("terminal length 0\n")
	tn.write("show running-config\n")
	tn.write("exit\n")
	
readoutput = tn.read_all()
saveoutput = open("Switch" + HOST, "w")
saveoutput.write(readoutput)
saveoutput.close