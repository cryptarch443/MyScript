import SecureCRT



with open('test0.3.1') as file:
	interface_list = file.read().splitlines()

for check_interface in interface_list:
	crt.Screen.WaitForString('#')
	crt.Screen.send('show interface ' + interface_list)

