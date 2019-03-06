import re

def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return text == reverse(text)

input = raw_input('Enter text: ')
input = input.lower()
inputlist = re.findall(r'.', input)
print inputlist

forbidden = ('.', '?', '!', ':', ';', '-', '_', '(', ')', '[', ']', '...'\
             '\'', '"', '/', ',', '\\', ' ')
for i in inputlist:
    if i in forbidden:
        n = inputlist.index(i)
        #print n
        inputlist[n] = ''

something = ''.join(inputlist)
print something

print is_palindrome(something)

if is_palindrome(something):
    print 'Yes, this is a palindrome.'
else:
    print 'No, this is not a palindrome'
