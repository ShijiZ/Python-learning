import math

print math.pi

print math.e

print math.ceil(1.5)

print math.floor(1.5)

print math.pow(2,4)

print math.log(10)

print math.log(10,10)

print math.sqrt(81)

print math.fabs(-3)

def root_quadratic(a,b,c):
    r1= (-b+math.sqrt(math.pow(b,2)-4*a*c))/(2*a)
    r2= (-b-math.sqrt(math.pow(b,2)-4*a*c))/(2*a)
    return (r1,r2)

print root_quadratic(2,7,4)
