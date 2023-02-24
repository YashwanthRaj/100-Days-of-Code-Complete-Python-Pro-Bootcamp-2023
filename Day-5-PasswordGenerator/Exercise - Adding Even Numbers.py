"""
You are going to write a program that calculates the sum of all the even numbers from 1 to 100. Thus, the first even number would be 2 and the last one is 100:

"""
sum1 = 0
for i in range(0,101,2):
    sum1+=i
print(sum1)