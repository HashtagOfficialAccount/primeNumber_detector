num = int(input("Enter a number to checked for prime: "))
if num <= 1:
    print("Your number is neither prime or composite")
else:
    index = 0
    for i in range(1,num + 1):
        if num % i == 0:
            index += 1
    if index == 2:
        print("Your number is prime")
    else:
        print("Your number is composite")


