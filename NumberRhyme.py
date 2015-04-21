'''
Created on Apr 20, 2015

@author: Caitlin
'''
import re

def NumberRhyme():
    while True:
        try:
            name = raw_input("What's your name? ")
            rgx = re.sub(r'^[^aeiouAEIOU]+([aeiouAEIOU].*)', r'\1', name)
            print "%s %s bo-b%s, Bonana-Fanna Fo-F%s Fee-Fy mo-m%s, %s!" % (name,name,rgx,rgx,rgx,name)
        except KeyboardInterrupt:
                print "The End"
if __name__ == '__main__':
    NumberRhyme()