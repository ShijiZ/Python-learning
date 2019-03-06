import sys
import time
f = None

try:
    with open('poem.txt') as f:
        for line in f:
            print line
            sys.stdout.flush()
            print "Press ctrl+c now"
            # To make sure it runs for a while
            time.sleep(2)
except IOError:
    print('Could not find the file "poem.txt".')
except KeyboardInterrupt:
    print('You canceled reading from the file.')
