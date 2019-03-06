from random import choice
direction = ['left', 'center', 'right']

score_you=0
score_computer=0

for i in range(1,6):
   print 'Round %d You shoot'%i
   print 'Choose one side to shoot:'
   print 'left, center, right'
   you = raw_input()
   print 'You kicked ' + you
   com = choice(direction)
   print 'Computer saved ' + com
   if you != com:
      print 'Goal!'
      score_you +=1
   else:
      print 'Oops...'
   print 'Your score: %d, Computer\'s score: %d' %(score_you,score_computer)
   print '------------------------------------------------'

   print 'Round %d You save'%i
   print 'Choose one side to save:'
   print 'left, center, right'
   you = raw_input()
   print 'You saved ' + you
   com = choice(direction)
   print 'Computer shot ' + com
   if you != com:
      print 'Oops...'
      score_computer +=1
   else:
      print 'Saved!'  
   print 'Your score: %d, Computer\'s score: %d' %(score_you,score_computer)
   print '------------------------------------------------'

print "Final score: You %d, Computer %d"%(score_you,score_computer)
if score_you>score_computer:
   print "You win!"
elif score_you<score_computer:
   print "You lose..."
else:
   print "Tie"
