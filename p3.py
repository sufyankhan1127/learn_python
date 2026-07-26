# demo=input("Enter 1st  number: ") 

print("Arithmetic operations and data types in python")
# takes input as string whatever the user enters. It does not matter if the user enters a number or a string, it will be treated as a string.











# integer
# a=int(input("Enter 2nd number: "))
# # takes the input as integer after int
# b=int(input("Enter 3rd number: "))


# float and integer
name=input("Enter your name: ")
a=float(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
i=bool(input("Enter boolean value: "))

print("Entered input is",a)
print("Entered input is",b)
print("Entered boolean value is",i)

c= a+b
d= a-b
e= a*b
f= a/b
g= a%b
h=a//b
j= a**b

print("Sum is",c)
print("Difference is",d)
print("Product is",e)
print("Quotient is",f)
print("Remainder is",g)
print("Exponent is",j)
print("Floor division is",h)


# this is unlike java where we have to convert the input into integer or float before performing any arithmetic operation.
# In python, we can directly perform arithmetic operations on the input values as they are treated as strings.