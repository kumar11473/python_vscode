list=[12,4,35,60,45]
l=list[0]                   # l->largest  sl-> second largest
sl=list[0]                #lp->largest position slp->second largest position
for i in range(1,len(list)):
    if list[i]>l:
        sl=l
        l=list[i]
        lp=list.index(l)
        slp=list.index(sl)
    elif list[i]>sl :
        sl=list[i]
        slp=list.index(sl)
print("Smallest number is :",l," and at the position",lp)
print("Second Smallest number is :",sl," and at the position",slp)

s=list[0]             #s->smallest ss->second smallest
ss=list[0]             #sp->smallest position ssp-> second smallest position
for i in range(1,len(list)):
    if list[i]<s:
        ss=s
        s=list[i]
        sp=list.index(s)
        ssp=list.index(ss)
    elif list[i]<ss :
        ss=list[i]
        ssp=list.index(ss)
print("Largest number is :",s," and at the position",sp)
print("Second Largest number is :",ss," and at the position",ssp)

     

