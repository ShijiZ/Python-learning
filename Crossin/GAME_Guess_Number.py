from random import randint

name=raw_input('Your first name:')

f=open('game.txt')
lines=f.readlines()
f.close()

scores={}
for l in lines:
    s=l.split()
    scores[s[0]]=s[1:]
score=scores.get(name)
#print score
if score is None:
    score=[0,0,0]

game_times=int(score[0])
min_times=int(score[1])
total_times=int(score[2])
if game_times>0:
    avg_times=float(total_times)/game_times
else:
    avg_times=0

print '%s, You have played %d times, get correct answer with \
minimum %d times, and on average %.2f times'%(name, game_times, min_times, avg_times)

num=randint(1,100)
times=0
print 'Guess what I think?'
a=0

while a==0:
    times+=1
    answer=input()

    if answer<num:
        print'%d is too small!'%answer

    if answer>num:
        print'%d is too big!'%answer

    if answer==num:
        print'Bingo! %s is correct!'%answer
        a=1

if game_times==0 or times<min_times:
    min_times=times
total_times+=times
game_times+=1

scores[name]=[str(game_times),str(min_times),str(total_times)]
result=''
for n in scores:
    line=n+' '+' '.join(scores[n])+'\n'
    result+=line

f=open('game.txt','w')
f.write(result)
f.close()

raw_input('press <enter>')
