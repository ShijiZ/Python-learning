def Quadrant(x,y):
    if x>0:
        if y>0:
            return 1
        elif y<0:
            return 4
        else:
            return "positive x-axies"
    elif x<0:
        if y>0:
            return 2
        elif y<0:
            return 3
        else:
            return "negative x-axies"
    else:
        if y>0:
            return "positive y-axies"
        elif y<0:
            return "negative y-axies"
        else:
            return "origin"

print "Give me your x"
x=input()
print "Give me your y"
y=input()
quadrant=Quadrant(x,y)
print quadrant
