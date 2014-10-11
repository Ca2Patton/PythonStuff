#!/usr/bin/env python

string = {}
string["key"] = "This is global"

def scope1(string):
	"""This is where we begin to figure out exactly what our variable scope is."""
	#global string
	print string
	string["Kung"] = "foo"
	print string

if __name__ == "__main__":
	scope1(string)
	print string
