#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
import pdb; pdb.set_trace()
class MyFamily:
	"""A Family Tree Object"""
	def __init__(self):
		fname = (raw_input("First Name? "))
		lname = (raw_input("Last Name? "))
		movie = []
		while True:
			movielist = raw_input("Favorite Movie? Input 0 to exit ")
			if movielist == '0':
				break
			movie.append(movielist)
		self.tree = {'fname' : fname, 'lname' : lname}
		self.movies = movie
brother = MyFamily()
