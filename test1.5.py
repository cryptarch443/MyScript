import SecureCRT

def main():
 crt.Screen.WaitForString("#")
 crt.Screen.Send("terminal length 0"+"\r")
 crt.Screen.WaitForString("#")
 crt.Screen.WaitForString("#")
 crt.Screen.Send("show arp vrf MEGA-CAPITAL GigabitEthernet0/1.361"+"\r")
 crt.Screen.WaitForString("#")
 crt.Screen.Send("show arp vrf GRIYA-INDOSAT GigabitEthernet6/0.105"+"\r")
 crt.Screen.WaitForString("#")
 crt.Screen.Send("show arp vrf SATKOMINDO GigabitEthernet6/0.120"+"\r")
 crt.Screen.WaitForString("#")
 crt.Screen.Send("show arp vrf BJB-SYARIAH GigabitEthernet6/0.145"+"\r")
 crt.Screen.WaitForString("#")
 crt.Screen.Send("show arp vrf ICBC GigabitEthernet6/0.171"+"\r")
 crt.Screen.WaitForString("#")
 crt.Screen.Send("show arp vrf NMS-ATI GigabitEthernet6/0.190"+"\r")
 crt.Screen.WaitForString("#")
 crt.Screen.Send("show arp vrf SOHO GigabitEthernet6/0.192"+"\r")
 crt.Screen.WaitForString("#")
 crt.Screen.Send("show arp vrf NMS-SIMONICA GigabitEthernet6/0.193"+"\r")
 crt.Screen.WaitForString("#")
 crt.Screen.Send("show arp vrf NMS-RAISECOM GigabitEthernet6/0.236"+"\r")
 crt.Screen.WaitForString("#")
 crt.Screen.Send("show arp vrf NMS-RL GigabitEthernet6/0.240"+"\r")


main()
