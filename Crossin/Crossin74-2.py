import urllib, time, thread

def get_content(i):
    id = 1764796 + i
    url = 'https://api.douban.com/v2/movie/subject/%d' % id
    d = urllib.urlopen(url).read()
    data.append(d)

time_start = time.time()
data = []
for i in range(30):
    print 'request movie:', i
    thread.start_new_thread(get_content, (i,))
    print i, time.time() - time_start
time.sleep(3)
print 'data:', len(data)
raw_input('press ENTER to exit...\n')
