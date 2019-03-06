import pickle

test_data = ['Save me!', 123.456, True]

f = file('test.data', 'w')
pickle.dump(test_data, f)
f.close()

f = file('test.data')
test_data = pickle.load(f)
f.close()
print test_data

a = 123
b = "hello"
c = 0.618
data = [a, b, c]
f = file('test_2.data', 'w')
pickle.dump(data, f)
f.close()

f = file('test_2.data')
test_data = pickle.load(f)
f.close()
print test_data

