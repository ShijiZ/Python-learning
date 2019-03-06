f=file('2018SCU_China.txt')
data=f.read()
#print data
f.close()

import re

m = re.findall(r"20\d{2}", data)
if m:
    print m
else:
    print 'not match'

m = re.findall(r"1\d{10}", data)
if m:
    print m
else:
    print 'not match'
