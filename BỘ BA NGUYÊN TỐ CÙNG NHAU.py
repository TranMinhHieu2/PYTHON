def ucln(n,m):
    while m!=0:
        x=n%m
        n=m
        m=x
    return n
l,r=[int(i) for i in input().split()]
for i in range(l,r+1):
    for j in range(i+1,r+1):
        if ucln(i, j)==1:
            for k in range(j+1,r+1):
                if ucln(j, k)==1 and ucln(i, k)==1:
                    print("(" + str(i) + ", " + str(j) + ", " + str(k) + ")")