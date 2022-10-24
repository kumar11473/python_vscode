#2. Write a generic program to find the roots of a quadratic equation. 
import math
print("code for finding root of a equation")
a=int(input("enter a: "))
b=int(input("enter b: "))
c=int(input("enter c: "))
x1=(((-b)+math.sqrt(pow(b,2)-4*a*c))/2*a)
print("first root =",x1)
x2=(((-b)-math.sqrt(pow(b,2)-4*a*c))/2*a)
print("second root" ,x2)