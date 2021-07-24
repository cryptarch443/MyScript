import textfsm
from pprint import pprint
import netmiko

string_interface = """
GigabitEthernet0/0 is up, line protocol is down (disabled)
  Hardware is CN Gigabit Ethernet, address is 0060.2f5b.c401 (bia 0060.2f5b.c401)
  Internet address is 10.10.10.1/24
  MTU 1500 bytes, BW 1000000 Kbit, DLY 10 usec,
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 100Mb/s, media type is RJ45
  output flow-control is unsupported, input flow-control is unsupported
  ARP type: ARPA, ARP Timeout 04:00:00, 
  Last input 00:00:08, output 00:00:05, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/75/0 (size/max/drops); Total output drops: 0
  Queueing strategy: fifo
  Output queue :0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts, 0 runts, 0 giants, 0 throttles
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored, 0 abort
     0 watchdog, 1017 multicast, 0 pause input
     0 input packets with dribble condition detected
     0 packets output, 0 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier
     0 output buffer failures, 0 output buffers swapped out
     """

template_file = open("showinterface.template")
template = textfsm.TextFSM(template_file)
result_template = template.ParseText(string_interface)

interface_list = list()
for list in result_template:
	resultDict = dict()
	resultDict["interface"] = list[0]
	resultDict["mac address"] = list[1]
	resultDict["ip address"] = list[2]
	resultDict["MTU"] = list[3]
	resultDict["bandwith"] = list[4]

	interface_list.append(resultDict)
pprint(interface_list)