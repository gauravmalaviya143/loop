x = int(input("enter the number"))
if x > 1:
    for i in range(2,x):
        if(x % i == 0):
            print(x,"number is not prime number")
            break
    else:
        print(x,"number is prime number")
else:
    print(x,"number is not prime number")