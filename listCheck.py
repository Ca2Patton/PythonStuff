#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python

l1 = set(map(str.strip, open('raFile1.txt', 'r')))
l2 = set(map(str.strip, open('raFile2.txt', 'r')))
print l1
print l2

print "Similarities:"
print list(l1.intersection(l2))
print "Differences:"
print list(l1.symmetric_difference(l2))
