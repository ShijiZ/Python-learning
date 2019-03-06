score = {
   'Xiaofeng': 95,
   'Duanyu': 97,
   'Xuzhu': 89
}

print score['Duanyu']

print score

for name in score:
   print score[name]

score['Xuzhu'] = 91

score['Murongfu'] = 88

del score['Xiaofeng']

print score
