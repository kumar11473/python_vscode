#Arbitrary arguments
def arbitrarySum(*num):
     sum=0
     for i in num:
        sum=sum+i
     return sum

print(arbitrarySum(300,45))
print(arbitrarySum(10,200))

