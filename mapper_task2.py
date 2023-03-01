#!/usr/bin/env python

import re
import sys

usr_inp = sys.argv[1]
hr = int(usr_inp.split('-')[0])
pat = re.compile('(?P<ip>\d+.\d+.\d+.\d+).*?\d{4}:(?P<hour>\d{2}):\d{2}.*? ')
for line in sys.stdin:
    match = pat.search(line)
    if match and int(match.group('hour'))==hr:
        print('%s\t%s'%('['+match.group('hour')+':00'+' to '+str(int(match.group('hour'))+1)+':00'+']',(match.group('ip'),1)))