import re
text='Hi, I am Shirlry Hilton. I am his wife.'

print '\bhi'

print r'\bhi'

m=re.findall(r'i.',text)
if m:
    print m
else:
    print 'not match'

m=re.findall(r'.',text)
if m:
    print m
else:
    print 'not match'

m=re.findall(r'\.',text)
if m:
    print m
else:
    print 'not match'

m=re.findall(r'\S',text)
if m:
    print m
else:
    print 'not match'

m=re.findall(r'.*',text)
if m:
    print m
else:
    print 'not match'

m=re.findall(r'I.*e',text)
if m:
    print m
else:
    print 'not match'

m=re.findall(r'.*?',text)
if m:
    print m
else:
    print 'not match'
    
m=re.findall(r'I.*?e',text)
if m:
    print m
else:
    print 'not match'

newtext='site sea sue sweet see case sse ssee loses'
m=re.findall(r'\bs\S*?e\b',newtext)
if m:
    print m
else:
    print 'not match'
