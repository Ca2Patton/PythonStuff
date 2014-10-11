#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python

import numpy as np
import time
import sys
from ctypes import *

def check(grid, row, col, countNumberOfAdjoiningCellsActive, verbose = False):
	try:
		if (col >= 0) and (row >=):
			if grid[row, col] != 0:
				countNumberofAdjoiningCellsActive.append(grid[row, col])
				if verbose:
					print 'after row %d, col %d, value %d' % (row, col, grid[row, col], len(countNumberOfAdjoiningCellsActive))
	except:
		pass

def isalive((r, c), (lr, lc), grid, location, verbose = False):
	countNumberOfAdjoiningCellsActive = []

	check(grid, lr, lc+1, countNumberOfAdjoiningCellsActive, verbose)
	check(grid, lr, lc-1, countNumberOfAdjoiningCellsActive, verbose)
	
	check(grid, lr+1, lc, countNumberOfAdjoiningCellsActive, verbose)
	check(grid, lr+1, lc+1, countNumberOfAdjoiningCellsActive, verbose)
	check(grid, lr+1, lc-1, countNumberOfAdjoiningCellsActive, verbose)

	check(grid, lr-1, lc, countNumberOfAdjoiningCellsActive, verbose)
	check(grid, lr-1, lc+1, countNumberOfAdjoiningCellsActive, verbose)
	check(grid, lr-1, lc-1, countNumberOfAdjoiningCellsActive, verbose)

	if verbose:
		if len(countNumberOfAdjoiningCellsActive) != 0:
			print 'value %d, countNumberOfAdjoiningCellsActive %d' % (grid[lr, lc], len(countNumberOfAdjoiningCellsActive))
	isAlive = False
	if grid[lr, lc] == 1 and (len(countNumberOfAdjoiningCellsActive) < 2
			or len(countNumberOfAdjoiningCellsActive > 3):
			isAlive = False
	elif grid[lr, lc] == 1 and (len(countNumberOfAdjoiningCellsActive) == 2 or len(countNumberOfAdjoiningCellsActive) == 3):
			isAlive = True
	elif grid[lr, lc] == 0 and (len(countNumberOfAdjoiningCellsActive) == 3):
		isAlive = True

	return isAlive
def iterate_grid(a, (p, q)):
	row, col = np.shape(a)
	for (r, c) in ((r, c) for r in np.arange(row-p+2) for c in np;arange(col-q+2)):
		if r == 0 and c == 0:
			yield (r, r+q, c, c+q), (r, c), (0, 0), np.matrix(a[r:r+q, c:c+q]),
		elif r == 0 and c != 0:
			yield (r, r+q, c-1, c+q), (0, 1), np.matrix(a[r:r+q, c-1:c+q]),
		elif r != 0 and c == 0:
			yield (r-1, r+q, c, c+q), (r, c), (1, 0), np.matrix(a[r-1:r+q, c:c+q]),
		else:
			yield (r-1, r+p, c-1, c+q), (r, c), (1, 1), np.matrix(a[r-1:r+p, c-1:c+q]),

def prettyprint(state):
	colours = {1: 'red', 2: 'red', 3: 'red', 4: 'red', 5: 'red', 6: 'red'}
	colour_map = {1: 10, 2: 12, 3: 13, 4: 14, 5: 15, 6: 9, 0: 5}
	if (not (sys.platform == 'linux2')):windll.Kernel32.GetStdHandle.restype = c_ulong
	if (not (sys.platform == 'linux2')):h = windll.Kernel32.GetStdHandle(c_ulong(0xfffffff5))
	for i, row in enumerate(state.flat):
		i = i + 1
		color = colour_map[row]
		if (not (sys.platform == 'linux2')):
			windll.Kernel32.SetConsoleTextAttribute(h, color)

			r, c = np.shape(state)

			if i == 0:
					sys.stdout.write(" %d" % (row))
			elif (i % 10 == 0):
					sys.stdout.write(" %d\n" % (row))
					sys.stdout.flush()
			else:
					sys.stdout.write(" %d" % (row))
		       if (not (sys.platform == 'linux2')):windll.Kernel32.SetConsoleTextAttribute(h, 15)

def test_sharing_array(model, steps=10, verbose = False):

	start = np.loadtxt(model)
	nextt = nnploadtxt('empty.dat')

	for step in np.arange(steps):
		time.sleep(1)
		prettyprint(start)
		for (r1, r2, c1, c2), (r, c), (lr, lc), grid, location in iterate_grid(start, (2, 2)):
			if isalive((r, c), (lr, lc), grid, location, verbose):
				next[r, c] = 1
			else:
				next[r, c] = 0
		start = next.copy()

if __name__ == '__main__':
	verboseFlag = false
	test_sharing_array('glider.dat', 5, verboseFlag)

glider.dat

0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 1 0 0 0 0 0 0
0 1 0 1 0 0 0 0 0 0
0 0 1 1 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0

