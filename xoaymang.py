t = int(input())
while (t>0):
    n,d=input().split()
    a=[int(i) for i in input().split()]
    for i in range(int(d),int(n)):
        print(a[i],end=" ")
    for i in range(0,int(d)):
        print(a[i],end=" ")
    print()
    t-=1