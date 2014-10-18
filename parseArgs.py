#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("square", help="Display a square of a given number", type=int)
args = parser.parse_args()

parser.add_argument("-v", "--verbose", action="count", default=0, help="increase output verbosity")
args = parser.parse_args()
answer = args.square**2

if args.verbose >= 2:
	print "The square of {} equals {}".format(args.square, answer)
elif args.verbose >= 1:
	print "{}^2 == {}".format(args.square, answer)
else:
	print answer
