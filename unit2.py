#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
import unittest

class SimplisticTest(unittest.TestCase):

	def test(self):
		self.failUnless(True)

if __name__ == '__main__':
	unittest.main()
