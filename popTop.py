#!/opt/local/bin/python

import psutil
import sys
import os

for pids in psutil.process_iter():
	try:
		pinfo = pids.as_dict(attrs=['pid','name', 'username','uids','terminal','cpu_percent','memory_percent', 'status'])
	except psutil.NoSuchProcess:
		pass
	else:
		print(pinfo)
