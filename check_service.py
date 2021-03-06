#!/usr/bin/python
import psutil
import sys
import re

n_args = len(sys.argv)
if n_args == 2:
    process = sys.argv[1]
else:
    raise Exception("Argument error")

pinfo = '<>'
result = []
for proc in psutil.process_iter():
    try:
        flag = False
        if(re.match('^' + process + '$', proc.name())):
            pinfo = proc.as_dict(attrs=['cmdline', 'status', 'exe'])
            result.append(pinfo)
    except psutil.NoSuchProcess:
        pass


message = ''
index = 0
if len(result):
    for proc in result:
        index = index + 1
        cmdline = proc['cmdline'][0] if (proc['cmdline'] and len(proc['cmdline'])) else ''
        message += "'SOD;name~%s;state~%s;type~%s;desc~%s;EOD'" % (cmdline, proc['status'], 'Linux Process',proc['exe'])
else:
    message = "Failed to open service %s: 1" % (process)

print message
