#!//Library/Frameworks/Python.framework/Versions/2.7/bin/python

import re
from collections import defaultdict

sids = defaultdict(dict)

def setKey(key, value, sids, sledid):
	"""Set key value, or default"""
	for label in ["requestStart", "slotinuse", "progname"]:
		try:
			sids[sledid][label]
		except(KeyError):
			sids[sledid][label] = None
	sids[sledid][key] = value

	

filename = open ("textFile.txt", "r")

for line in filename:
	#Match data in textfile only when data has "entry#n" in front.
	#entry#:0 sledid:0,pid:60331,requestStart:1392656336,slotinuse:1,intransaction:0
	match = re.search(r"entry#:\d+ \w+:(\d{2,}),\w+:\d+,\w+:(\d+),\w+:(\d),\w+:\d", line)
	match2 = re.search(r"sid:(\d+),\w+:\d+,\w+:\d+,\w+:\d+,\w+:\d,\w+:\d,\w+:\d \w+:(\w+)", line)
	#match = re.search(r"entry#:\d+ \w+:\d+",line)
	pass 
	if match:
		sledid = match.group(1)
		requestStart = match.group(2)
		slotinuse = match.group(3)
		#sids[sledid]["requestStart"] = requestStart
		#sids[sledid]["slotinuse"] = slotinuse
		setKey("requestStart", requestStart, sids, sledid)
		setKey("slotinuse", slotinuse, sids, sledid)
		print line,

	elif match2:
		sledid = match2.group(1)
		progname = match2.group(2)
		#sids[sledid]["progname"] = progname
		setKey("progname", progname, sids, sledid)
		print line,
filename.close

#print sids

for sledid in sids:
	print sledid
	for label in sids[sledid]:
		print sledid, label, sids[sledid][label]
