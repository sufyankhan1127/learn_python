# # find largest of two numbers

# a=(int(input("Enter the 1st value:")))
# b=(int(input("Enter the 2nd value:")))
# if a>b:
#     print("a is the largest",a)
# else :
#     print("b is the largest",b)





# # check even or odd number

# a=(int(input("Enter the 1st value: ")))
# b=(int(input("Enter the 2nd value: ")))

# if a%2==0:
#     print("a is even number",a)
# else:
#     print("a is odd number",a)

# if b%2==0:
#     print("b is even number",b)
# else:
#     print("b is odd number",b)




# # check positive negative or zero
# a=(int(input("Enter the value: ")))
# if a>0:
#     print("a is positive number",a)
# elif a<0:
#     print("a is negative")
# else :
#     print("a is 0")


# #check largest among three numbers
# a=int(input("Enter the first number:"))
# b=int(input("Enter the second number:"))
# c=int(input("Enter the third number:"))

# if a>b and a>c:
#     print("a is the greatest of three numbers")
# elif b>a and b>c:
#     print('b is the greatest of three numbers')
# elif c>a and c>b:
#     print('c is the greatest of three numbers')

# else:
#     print("All numbers are equal")


# #number divisible by 5 and 11
# a=int(input("Enter the first value:"))

# if(a%55==0):
#     print("a is divisible by 5 and 11")
# elif(a%5==0 and a%11!=0):
#     print("a is divisible by 5 but not by 11")
# elif(a%11==0 and a%5!=0):
#     print("a is divisible by 11 but not by 5")
# else:
#     print("a is not divisible by 5 and 11")




# #check vowel or consonant
# a=input("Enter the character: ")
# if a in 'aeiouAEIOU':
#     print("a is vowel")
# else:
#     print("a is consonant")


# #check alphabet or number or float or special character
# a=input("Enter the character: ")

# if (a.isdigit()):
#     print("a is number")
# elif(a.isdecimal()):
#     print("a is decimal")
# elif(a.isalpha()):
#     print("a is alphabet")
# else:
#     print("a is special character")

#check leap year or not
year=int(input("Enter the year: "))
if (year%4==0 and year%100!=0) or (year%400==0):
    print("year is leap year")
else:
    print("year is not leap year")