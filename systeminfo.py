#!/usr/bin/python
#Toying with viewing system info from python

import psutil

CPUP = psutil.cpu_percent(interval=1)
print CPUP

CPUP2 = psutil.cpu_percent(interval=1, percpu=True)
print CPUP2

c_times = psutil.cpu_times()
print c_times

count_me = psutil.cpu_count()
print "The number of logical cpus in the system is: " + str(count_me)
count_me_again = psutil.cpu_count(logical=False)
print "The number of physical cpu cores in the system is: " + str(count_me_again)

memory = psutil.virtual_memory()
print "System memory stats: "
print memory

swap = psutil.swap_memory()
print "Swap memory stuff: "
print swap

disks = psutil.disk_partitions()
print "Disk partition information: "
print disks

disk_use = psutil.disk_usage('/')
print "Disk usage: "
print disk_use

disk_io = psutil.disk_io_counters(perdisk=True)
print "Disk usage per disk information: "
print disk_io
