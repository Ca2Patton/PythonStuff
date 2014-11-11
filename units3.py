#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
import unittest

class OutcomesTest(unittest.TestCase):

	def testpass(self):
		return
	
	def testFail(self):
		self.failIf(True, 'Failure msgs are fun')

	def testError(self):
		raise RuntimeError('Test Error!')

if __name__ == '__main__':
	unittest.main()
