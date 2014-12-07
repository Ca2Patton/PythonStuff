#!/opt/local/bin/python

import psutil
import datetime

today = datetime.date.today()
template = "%-10s %5s %4s %4s %7s &7s %-13s %5s %7s %s"
attributes = ['pid', 'cpu_percent', 'memory_percent' 'name', 'cpu_times', 'create_time', 'memory_info']

print (template % ("USER", "PID", "%CPU", "%MEM", "VSZ", "RSS", "TTY", "START", "TIME", "COMMAND"))

for p in process_iter():
	try:
		pinfo= p.as_dict(attributes, ad_value='')
	except NoSuchProcess:
		pass
	else:
		if pinfo['create_time']:
			ctime = datetime.datetime.fromtimestamp(pinfo['create_time'])
			if ctime.date() == today_day:
				ctime = ctime.strftime("%H:%M")
			else:
				ctime = ctime.strftime("%b%d")
		else:
			ctime = ''
		cputime = time.strftime("%M:%S", time.localtime(sum(pinfo['cpu_times'])))
		try:
			user = p.username()
		except KeyError:
			if pinfo['uids']:
				user = str(pinfo['uids'].real)
			else:
				user = ''
		except Error:
			user = ''

