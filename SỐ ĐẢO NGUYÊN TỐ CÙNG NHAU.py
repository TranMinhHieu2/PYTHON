def ucln(n,m):
    while m!=0:
        x=n%m
        n=m
        m=x
    return n
t=int(input())
while t>0:
    n=input()
    m=n[-1::-1]
    if ucln(int(n), int(m))==1:
        print("YES")
    else: print("NO")
    t-=1