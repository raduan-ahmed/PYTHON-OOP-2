num = int(input("Enter a number: "))

# Prime numbers are greater than 1
if num > 1:
    # Check for factors
    for i in range(2, int(num**0.5) + 1):
        if (num % i) == 0:
            print("{0} is not a prime number".format(num))
            break
    else:
        print("{0} is a prime number".format(num))
else:
    print("{0} is not a prime number".format(num))
