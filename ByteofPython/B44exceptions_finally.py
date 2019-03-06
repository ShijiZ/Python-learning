import sys
import time

f = None
try:
    f = open('poem.txt')
    # Our usual file reading idiom
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print line,
        sys.stdout.flush()
        print 'Press ctrl+C now'
        # To make sure it runs for a while
        time.sleep(2)
except IOError:
    print('Could not find the file "poem.txt".')
except KeyboardInterrupt:
    print('You canceled reading from the file.')
finally:
    if f:
        f.close()
    print('Cleaning up: Close the file.')

