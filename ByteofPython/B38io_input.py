def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return text == reverse(text)

something = raw_input('Enter text: ')

print is_palindrome(something)

if is_palindrome(something):
    print 'Yes, this is a palindrome.'
else:
    print 'No, this is not a palindrome'
