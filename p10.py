# use of for loops in different ways in python



# # range function in python is used to generate a sequence of numbers. It takes three arguments, the first argument is the starting number, 
# # the second argument is the ending number and the third argument is the step value. 
# # The range function returns a range object which can be converted into a list using the list() function.
# for i in range(1,10):
#     print(i)



# #program to print tables for any number using for loop in python
# num=int(input("Enter the number for which you want to print the table: "))

# count=1

# for tables in range(num,(num*10)+1,num):
#     print(num,"X",count,"=",tables)
#     count+=1



# #program to print the sum of first n natural numbers using for loop in python
# n=int(input("Enter the number of natural numbers you want to sum: "))
# sum=0
# for i in range(1,n+1):
#     sum=sum+i
# print("The sum of first",n,"natural numbers is",sum)


# factorial of n natural numbers using for loop in python
no=int(input("Enter the number for which you want to find the factorial: "))
fact=1
for i in range(1,no+1):
    fact=fact*i
print("The factorial of",no,"is",fact)