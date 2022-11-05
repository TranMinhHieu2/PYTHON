t=int(input())
while (t>0):
   a,b=input().split()
   res=input().split()
   if len(res)==1:
      x=res[0]
      y=input()
   else :
      x, y=res
   res1= int(x.replace(a, b)) + int(y.replace(a,b))
   res2= int(x.replace(b, a)) + int(y.replace(b, a))
   print(min(res1, res2), max(res1,res2))
   t=t-1
