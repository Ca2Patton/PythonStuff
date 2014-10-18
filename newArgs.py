#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
#import pdb; pdb.set_trace()

import argparse

parser = argparse.ArgumentParser(description='Getting to Know argparse')

parser.add_argument('first', help='the first argument')
parser.add_argument('second', help='the second argument')
parser.add_argument('third', help='the third argument')

args = parser.parse_args()
print args
