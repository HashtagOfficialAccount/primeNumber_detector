#user gets the opportunity enter a number (prime or composite)
num = int(input('Enter your number: '))

#all the even numbers except 2 
if num % 2 == 0 and num != 2: 
    print('Your number is NOT a prime number')  
    exit()

if num % 3 == 0 and num != 3:  
    print('Your number is NOT a prime number')  
    exit()


if num % 5 == 0 and num != 5:  
    print('Your number is NOT a prime number')  
    exit()


if num % 7 == 0 and num != 7:  
    print('Your number is NOT a prime number')  
    exit()


if num % 9 == 0 and num != 9:  
    print('Your number is NOT a prime number')  
    exit()

print('Your number IS a prime number')
