li=[]

re=0
n=int(input("len(x) : "))
for x in range(0,n):
    lis=float(input("cost : "))
    li.append(lis)
nb=sum(li)
print("cost 모두 합 : ",nb)
for i in range(0,n):
    re+=abs(li[i]-nb/n)**2
print("(x-x_bar)^2 is : ",re)
    
