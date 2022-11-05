def ucln(n,m):
    while m!=0:
        x=n%m
        n=m
        m=x
    return n
n,k=[int(i) for i in input().split()]
cnt=1
for i in range(10**(k-1),10**k):
    if ucln(n, i)==1:
        print(i,end=" ")
        if cnt==10:
            print()
            cnt=1
        else : cnt+=1
