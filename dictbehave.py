#!/usr/bin/env python

dictionary = {}
try:
	print dictionary["foo"]
except (KeyError):
	dictionary["foo"] = 4
	print dictionary
