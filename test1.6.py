import re
import textfsm
import openpyxl
import json
from pprint import pprint

show_bgp_summary = """
BGP router identifier 3.3.3.3, local AS number 1
BGP table version is 9, main routing table version 9
8 network entries using 1248 bytes of memory
8 path entries using 640 bytes of memory
5/5 BGP path/bestpath attribute entries using 720 bytes of memory
5 BGP extended community entries using 136 bytes of memory
0 BGP route-map cache entries using 0 bytes of memory
0 BGP filter-list cache entries using 0 bytes of memory
BGP using 2744 total bytes of memory
BGP activity 8/0 prefixes, 8/0 paths, scan interval 60 secs

Neighbor        V           AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
1.1.1.1         4            1      38      40        9    0    0 00:28:35        3
2.2.2.2         4            1      37      44        9    0    0 00:28:35        2
4.4.4.4         4            1      40      41        9    0    0 00:27:09        1
5.5.5.5         4            1      16      25        9    0    0 00:11:26        0
6.6.6.6         4            1      16      24        9    0    0 00:10:14        2
"""

template_file = open("test1.6.template")
template = textfsm.TextFSM(template_file)
result_bgp = template.ParseText(show_bgp_summary)

bgp_list = list()

for list in result_bgp:
	bgp_dict = dict()
	bgp_dict['Neighbor'] = list[0]
	bgp_dict['AS'] = list[1]
	bgp_dict['Status'] = list[2]
	bgp_dict['Prefix'] = list[3]
	bgp_list.append(bgp_dict)
print(json.dumps(bgp_list, indent=4))