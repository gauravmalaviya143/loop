av = 10
x = int(input("how many candies you want?"))

i = 1
while i<=x:
    if i>av:
        print("out of stock")
        break
    print("candies")
    i+=1
print("bye")