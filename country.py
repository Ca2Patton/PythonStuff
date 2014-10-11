#!/usr/bin/env python

from collections import defaultdict

#USA = defaultdict(dict)
#USA["California"]["Antioch"]["5010 Hawxhurst Ct"] = "you"
#USA["Arizona"]["Phoenix"]["123 Main Street"] = "Joe"
#USA["Nevada"]["Las Vegas"]["456 East Street"] = "Bar"

#Cities = ["Antioch", "Phoenix", "Las Vegas"]

#for city in Cities:
#	for state in USA:
#		address = USA[state][city]
#		print address

#country = {} 
#country["state"]["city"] = "Antioch"
#country["State"] = {}
#country["State"]["California"] = {}
#country["State"]["California"]["City"] = {}
#country["State"]["California"]["City"]["ZIP"] = {} 
#country["State"]["California"]["City"]["ZIP"]["94509"] = None
#country["State"]["California"]["City"]["ZIP"]["94531"] = None
#print country

#country = defaultdict(dict)
#country["state"]
#country["state"]["city"]
#country["state"]["city"]["ZIP"]
#country["state"]["city"]["ZIP"]["94509"]
#country["state"]["city"]["ZIP"]["94531"]


x = lambda: defaultdict(x)
country = x()

country["State"]["City"]["ZIP"]["94509"]
country["State"]["City"]["ZIP"]["94531"]
