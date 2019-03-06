try:
    text = raw_input('Enter something --> ')
except EOFError:
    print 'Why did you do an EOF to me?'
except KeyboardInterrupt:
    print 'You canceled the operation.'
else:
    print 'You entered {}.'.format(text)
