l=[1]*15
for i in range(2,10): l[i]=l[i-1]*i
t= int(input())
while t>0:
    n=input()
    if sum([l[int(i)] for i in n])==int(n):
        print("Yes")
    else: print("No")
    t-=1