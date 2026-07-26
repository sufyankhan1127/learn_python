# difference between == and is in Python

a = [1, 2]
b = [1, 2]
c = a

print(a == b)   # True  (same contents)
print(a is b)   # False (different list objects)
print(a is c)   # True  (c refers to the same object as a)



# use of and and or operators in python
d=int(input("Enter 1st number: "))
e=int(input("Enter 2nd number: "))

print(d and e) #returns the first falsy value or the last value if all are truthy in short return smallest value
print(d or e) #returns the first truthy value or the last value if all are falsy in short return largest value


# use of not operator in python
f=int(input("Enter 1st number: "))
print(not f) #returns True if f is falsy and False if f is truthy in short returns opposite of f

# not simply reverses the truth value.

# Value	    TruthValue	not Result
# 5	        True	    False
# -10	    True	    False
# 100	    True	    False
# 0	        False	    True
# ""	    False	    True
# "Hello"	True	    False


# use of bitwise operators in python
g=int(input("Enter 1st number: "))
h=int(input("Enter 2nd number: "))
print(g&h) #bitwise and
# 101 --> 5
# 011 --> 3
# ---
# 001 --> 1

print(g|h) #bitwise or
# 101 --> 5
# 011 --> 3
# ---
# 111 --> 7

print(g^h) #bitwise xor

# same bits 1 ,different bits 0
# 101 --> 5
# 011 --> 3
# ---
# 110 --> 6


# shift operators in python

k=int(input("Enter the number: "))
l=int(input("Enter shift value: "))
print(k<<l) #left shift
# 101 --> 5

# 101000 --> 40

print(k>>l) #right shift
# 101 --> 5
# 001 --> 1
