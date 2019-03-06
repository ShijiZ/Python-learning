import re

f=file('phone_number.txt')
data=f.read()
f.close()

m=re.findall(r'\(0\d{2,3}\)\d{7,8}|0\d{2,3}[- ]?\d{7,8}',data)
if m:
    print m
else:
    print 'not match'
