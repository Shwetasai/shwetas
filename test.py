#(1)Write a Python program that takes a list of numbers as input from the user and arranges them in ascending order
#step1: take an input ,which can be only string
#step2:split the string into individual numbers or substrings(may be say)
#step3:convert each individual no. or substrings into integers
#step4:arrange the numbers into ascending order
#step5:print the sorted list
number_str=input("enter a list of numbers seprated by commas")
number_list=number_str.split(',')
number_list=[int(num)for num in number_list]
number_list.sort()
print("sorted numbers",number_list)
#(2)Write a program that takes a list of integers and removes any duplicates, then prints the list without duplicates
#step1:take a list of integers as input
#step2:split the string into individual no.
#step3:convert each individual no. or substrings into integers
# step4:Remove duplicates by converting the list to a set and back to a list
number_str=input("enter a list of numbers seprated by commas")
number_list=number_str.split(',')
number_list=[int(num)for num in number_list]
new_list=list(set(number_list))
print("list without duplicates:",new_list)
#(3)perform del, pop and clear methods on dict and list
#for dic.
x={"father":48,"mother":45,"brother":23,"sister":27}
del x ["mother"]
print (x)
x.pop("brother")
print(x)
x.clear()
print(x)
#for list
y=["january","february","march","april","may","june","july"]
del y[2]
print(y)
y.pop(1)
print(y)
y.clear()
print(y)
#(4) Write a program to reverse a number entered by the user.
num=int(input("enter a number:"))
reversed_num=int(str(num)[::-1])  
"""use string conversion because int can not be reverse,
 it's easier to manipulate the digits as characters in a string."""
print("reversed_num is:",reversed_num)
#(5)Write a Python program that takes a name input from the user and extracts all vowels from it and also showing count of the vowels.
#step1:take an input
#step2:initializing a string
#step3:initializing count of vowels
#step4:define vowels
#step5:iterate over each alphabet 
#step6:increment in char
#step7:check if any character is a vowel
#step8:increment in vowel count
#step9:print extracted vowels
#step10:print no. of vowels
name_str=input("enter a name:")
extracted_vowels=""
vowels_count=0
vowels="aeiouAEIOU"
for char in name_str:
    extracted_vowels+=char
    if char in vowels:
            vowels_count+=1
print("extracted vowels are:",extracted_vowels)
print("count of vowels is",vowels_count)



