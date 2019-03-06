f = file('scores.txt')
lines=f.readlines()
print lines
f.close

results = []

for line in lines:
   #print line
   data = line.split()
   #print data

   sum = 0
   for score in data[2:]:
       sum = sum+int(score)
   result = '%s: %d\n' % (' '.join(data[0:2]), sum)
   print result

   results.append(result)

print results
output = file('result.txt', 'w')
output.writelines(results)
output.close()
