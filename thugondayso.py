n=int(input())
a=[int(i) for i in input().split()]
i=0;
while(i+1<n):
    if((a[i]+a[i+1])%2==0):
        a.pop(i)
        a.pop(i)
        n=n-2
        if(i>0):
            i=i-1
    else: i=i+1
print(len(a))