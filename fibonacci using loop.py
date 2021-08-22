"""printing fibonacci series using while loop"""

n=int(input("Enter a positive integer"))
c=0
a,b=0,1
print(a,b,sep=",",end=",")
while c<n:
  inc=a+b
  print(inc,end=",")
  a=b
  b=inc
  c+=1
  
