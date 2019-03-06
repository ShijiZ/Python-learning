data = 'I will be in a file.\nSo cool!'
out = open('output.txt', 'w')
out.write(data)
out.close()

out = open('output.txt', 'r')
print out.read()
out.close()
