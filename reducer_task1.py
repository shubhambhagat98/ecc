#!/usr/bin/env python


import re
import sys
import ast
from operator import itemgetter


dict_ip_count = {}
for line in sys.stdin:
    line = line.strip()
    time,str_ip_count = line.split('\t')
    try:
        ip_count = ast.literal_eval(str_ip_count)
        ip,count = ip_count
        if time in dict_ip_count.keys():
            if ip in dict_ip_count[time].keys():
                dict_ip_count[time][ip]+=count
            else:
                dict_ip_count[time][ip]=count
        else:
            dict_ip_count[time]={ip:count}

    except ValueError:
        pass

for d in dict_ip_count.keys():
    counter=3
    sorted_dict_ip_count = sorted(dict_ip_count[d].items(),key=itemgetter(1),reverse=True)
    # sorted_dict_ip_count = sorted(dict_ip_count.items(),key=itemgetter(0))
    for ip,count in sorted_dict_ip_count:
        if counter!=0:
            print('%s\t%s\t%s'%(d,ip,count))
            counter-=1
        else:
            break