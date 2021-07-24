#Python2.7
import paramiko
import time

ip_address = "192.168.100.200"
username = "cisco"
password = "cisco"

ssh_client = paramiko.SSHClietn()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddpolicy())
ssh_client.connect(hostname=ip_address,username=username,password=password)

print "Succesfull Connection", ip_address

remote_connection = ssh_client.invoke_shell()

remote_connection.send("configure terminal\n")
remote_connection.send("router ospf 100\n")
remote_connection.send("network 0.0.0.0 0.0.0.0 area 0\n")

for vlan in range (2,21):
	print "Creating Vlan " + str(vlan)
	remote_connection.send("vlan " + str(vlan) + "\n")
	remote_connection.send("Name Python Vlan " + str(vlan) + "\n")
	time.sleep(0.5)

remote_connection.send("end\n")

time.sleep(1)
output = remote_connection.recv(65535)
print output

ssh_client.close