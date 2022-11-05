t=int(input())
while t>0:
    s=input()
    check=1
    for i in s[2::2]:
        if i!=s[0]:
            check=0
            break
    for i in s[3::2]:
        if i!=s[1]:
            check=0
            break
    if check==1:
        print("YES")
    else: print("NO")
    t-=1
    