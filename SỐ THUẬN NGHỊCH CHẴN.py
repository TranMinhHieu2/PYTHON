t=int(input())
while t>0:
    n=int(input())
    for i in range(2,n,2):
        s=str(i)
        if len(s)%2==0 and s[-1::-1]==s and '1' not in s and '3' not in s and '5' not in s and '7' not in s and '9' not in s:
            print(i,end=" ")
    print()
    t-=1
