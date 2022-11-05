s=input()
ss=''
dem=0
for i in range(len(s)-1,-1,-1):
    if dem==3: 
        ss=','+ss
        dem=0
    ss=s[i]+ss
    dem+=1
if ss[0]==',':print(ss[1:])
else: print(ss)