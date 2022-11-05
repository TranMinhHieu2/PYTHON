from math import * 
def ktra(n):
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return 0
    return 1

t=int(input())
while t>0:
    n=input()
    check=1
    sum=0
    for i in n:
        sum+=int(i)
        if ktra(int(i))==0:
            check=0
    if check==1 and ktra(sum)==1 and ktra(int(n))==1 and ktra(int(n[-1::-1]))==1:
        print("Yes")
    else: print("No")
    t-=1