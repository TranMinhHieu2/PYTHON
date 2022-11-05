import re
t=int(input())
while(t>0):
    s=input()
    res=re.findall('\d+', s)
    print(max([int(i) for i in res]))
    t=t-1