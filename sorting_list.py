
from typing import Counter
sen='Let it snow let it snow let it snow'
x=input("Enter the word to know its frequency :")
count=0
list =sen.split(' ')
for i in range(len(list)):
    if list[i]==x:
        count=count+1        
if count==0:
    print(x,"not found in the sentence")
print("Frequency of ",x,"is ",count)       
