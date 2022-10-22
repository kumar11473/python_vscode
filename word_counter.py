from typing import List
line='my name is sushant is kumar pandey my name is sushant kumar is my name is sushant kumar kumar pandey'
list1= []
list1=line.split(' ')
list2=list(set(list1))  # using set function to remove all duplicate from given sentence and converting set again to list type
print("Number of words in the sentence is",len(list1))
for i in range(len(list2)):   
    count=0
    for j in range(len(list1)):
        if list2[i]==list1[j] :
            count=count+1
    print("The frequency of",list2[i],"is",count)        
