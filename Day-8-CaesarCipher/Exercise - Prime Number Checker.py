"""
Prime numbers are numbers that can only be cleanly divided by themselves and 1.

https://en.wikipedia.org/wiki/Prime_number

You need to write a function that checks whether if the number passed into it is a prime number or not.

"""

#Write your code below this line 👇

def prime_checker(number):
    is_prime = True
    list1 = [2,3,5,7,11]
    if number not in list1:
        if number%2==0:
            is_prime=False
        if number%3==0:
            is_prime=False
        if number%5==0:
            is_prime=False
        if number%7==0:
            is_prime=False
        if number%11==0:
            is_prime=False   
    
    if is_prime:
        print("Its is a prime!")
    else:
        print("It is not a prime!")


#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



####   Angela's Code [prime_checker Function Alone]
'''
def prime_checker(number):
    is_prime=True
    for i in  range(2,number):
        if number%i==0:
            is_prime=False
    if is_prime:
        print("Its is a prime!")
    else:
        print("It is not a prime!")
'''