import re
text='Hi, I am Shirlry Hilton. I am his wife.'
m=re.findall(r'hi',text)
if m:
    print m
else:
    print 'not match'

m=re.findall(r'\bhi',text)
if m:
    print m
else:
    print 'not match'

m=re.findall(r'[Hh]i',text)
if m:
    print m
else:
    print 'not match'

m=re.findall(r'\b[Hh]i',text)
if m:
    print m
else:
    print 'not match'

