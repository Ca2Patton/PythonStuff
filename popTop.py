#!/opt/local/bin/python

import psutil
import sys
import os

print "{0:<8}{1:<40}{2:<10}{3:<20}{4:<10}{5:<10}{6:<10}{7:<10}".format("PID", "Name", "User", "Uid", "TTY", "CPU %", "Memory %", "Status")
for pids in psutil.process_iter():
	try:
		pinfo = pids.as_dict(attrs=['pid','name', 'username','uids','terminal','cpu_percent','memory_percent', 'status'])
	except psutil.NoSuchProcess:
		pass
	else:
		print "{0:<8}{1:<40}{2:<10}{3:<50}{4:<10}{5:<10}{6:<10}{7:<10}".format(pinfo['pid'], pinfo['name'], pinfo['username'], pinfo['uids'],pinfo['terminal'], pinfo['cpu_percent'], pinfo['memory_percent'], pinfo['status'])
