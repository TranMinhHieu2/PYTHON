from math import *
t=int(input())
while t>0:
    s=input()
    tong=0
    check=0
    for i in range(0,len(s)-1):
        if abs(int(s[i])-int(s[i+1]))!=2:
            check=1
            break
        tong+=int(s[i])
    tong+=int(s[-1]) 
    # in ra phan tu cuoi cung trong string [-1]
    if check==0 and tong%10==0:
        print('YES')
    else: print("NO")
    t-=1