#Write a program to find the type of input taken from user.
a = input ("Enter the value of a:")
print (type(a)) 
#Output will be string because input function always takes input as string.
b = int(input ("Enter the value of b:"))
print(type(b))
#Output will be integer because we have type casted the input to integer using int() function.