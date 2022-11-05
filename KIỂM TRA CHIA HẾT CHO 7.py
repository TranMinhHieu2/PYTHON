
t=int(input())
while t>0:
    n=int(input())
    while n%7!=0:
        n=n+int(str(n)[-1::-1])
    print(n)
    t-=1