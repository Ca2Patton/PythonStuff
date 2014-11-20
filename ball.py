#!/opt/local/bin/python

class Ball(object):
	"""
	This creates a ball
	"""
	def __init__(self, diameter = 1, color = (255, 254, 4)):
		self.maxDiameter = 20
		
		assert isinstance(diameter, int), "Not a number"
		assert diameter <= self.maxDiameter, "Diameter must be less than 20"
		for c in color:
			assert c <= 255, "Out of bounds, RGB color 0 - 255"
			assert c >= 0, "Out of bounds, RGB color 0 - 255"

		self.diameter = diameter
		self.color = color
		self.circumference = 3.14159265 * diameter

	def getDiameter(self):
		"""
		Returns diameter
		"""

		return self.diameter

	def getColors(self):
		#returns colors
		return self.color

if __name__ == '__main__':
	x = Ball(diameter = 10)
	print x.getDiameter()
	print x.getColors()
	pass
