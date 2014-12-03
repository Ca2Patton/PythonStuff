#!/usr/bin/python
#Toying with viewing system info from python

import psutil

CPUP = psutil.cpu_percent(interval=1)
print CPUP

CPUP2 = psutil.cpu_percent(interval=1, percpu=True)
print CPUP2

c_times = psutil.cpu_times()
print c_times
