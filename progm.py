print("hello")
#1.which prints odd numbers up to 100
i=1
while i<101:
    print(i)
    i+=2
#2.which prints even number up to 50
for x in range(0,51,2):
    print(x)
#3.Write a program to find the sum of all numbers between 1 and 100 that are divisible by 7

sum=0
for x in range(1,101):
    if x%7==0:
        sum+=x
print ("the sum of all numbers betwen 1 to 100 that are divisible by 7 is:",sum)
#4.Write a program to check if a given number is prime
def prime(num):
    if num<=1:
        return False
    for x in range(2,int(num)+1):
        if num%x==0:
            return False
    return true
num=int(input("enter the number:"))
if prime(num):
    print(num,"is a prime number")
else:
    print(num,"is not a prime number")
#5.Write a program to check if a given year is a leap year.
def leap(year):
    if (year%4==0):
        return True
    if (year%100!=0):
        return True
    if (year%400==0):
        return True
    else:
        return False
year=int(input("enter a year:"))
if leap(year):
    print(year,"is a leap year:")
else:
    print(year,"is not a leap year:")

