t=int(input())
while t>0:
    s=input()
    ok=1
    for i in s:
        if i!="1" and i!="2" and i!="0":
            ok=0
    if ok==1: print("YES")
    else: print("NO")
    t-=1
