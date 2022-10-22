# sum of natural number upto n
def sum(n):
 if n<0:
  print("Enter a natural number")
  return 0
 elif n==0:
    return 0
 else :
    return n+sum(n-1)

num=int(input("Enter number"))
print("The sum of natural number upto ",num ,"is ",sum(num))   