#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python

class Television:
	def __init__(self):
		vol_value = set(range(51))
		channel_list = {"KTVU" : 2, "Input" : 3, "KRON" : 4, "CBS" : 5, "RAND" : 7, "CCMD" : 8}
		self.volume = vol_value
		self.tv = {'on', 'off'}
		self.channels = channel_list
	def changeVol(self, volume):
		if volume in self.volume:
			print volume
		else:
			print "Invalid Input"
	def tvOn(self, state):
		if state in self.tv:
			print state
		else:
			print "Must be on, or off."
tv = Television()
tv.tvOn('on')
tv.tvOn('off')
tv.changeVol(46)
tv.changeVol(3)
