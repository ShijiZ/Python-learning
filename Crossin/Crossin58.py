import re

f=file('phone_number.txt')
data=f.read()
f.close()

m=re.findall(r'\(?0\d{2,3}[) -]?.*\d\b',data)
if m:
    print m
else:
    print 'not match'
