import math  
a = float(input('Enter a: '))  
b = float(input('Enter b: '))  
c = float(input('Enter c: '))  
  
# calculate the delta 
#delta = (b**2) - (4*a*c)  ,or
delta = math.pow(b,2) - (4*a*c)

  
if delta > 0:
    #number of roots are 2
    x1 = ((-b) + math.sqrt(delta) /(2*a))
    x2 = ((-b) - math.sqrt(delta) /(2*a))
    print("There are 2 roots : %f and %f" %(x1,x2))
elif delta == 0:
    #number of root 1, rational and equal
    x = (-b)/ 2*a
    print("There is one root:",x)
else:
    print("Np roots ,delta < 0")

