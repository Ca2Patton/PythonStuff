#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python

import re

string = "The theatre tithe is the bomb."

bark = re.sub(r'(?<!\w)the(?=\w)','happy', string, flags=re.IGNORECASE)
print bark
