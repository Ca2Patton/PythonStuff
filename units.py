#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
import unittest

def IsOdd(num):
	return num % 2 == 1

class IsOddTests(unittest.TestCase):

	def testOne(self):
		self.failUnless(IsOdd(1))

	def testTwo(self):
		self.failIf(IsOdd(2))

def main():
	unittest.main()

if __name__ == '__main__':
	main()
