x = int(input("Enter the value of x :"))
y = int(input("Enter the value of y :"))

print("The value of x and y are {} and {} before swapping".format(x,y))
#x,y = y,x or
temp = x
x = y
y = temp

print("The value of x and y are {} and {} before swapping".format(x,y))