#product of all odds from m to n
m=int(input("ENTER M VALUE: "))
n=int(input("ENTER N VALUE: "))
if m>n:
  print(0)
else:
  x=1
  for i in range(m,n+1):
    if i%2!=0:
      x=x*i
  print("PRODUCT: ",x)
