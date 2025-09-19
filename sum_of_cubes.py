#sum of cubes for integers m to n
m=int(input("ENTER M VALUE: "))
n=int(input("ENTER N VALUE: "))
if m>n:
  print(0)
else:
  sum=0
  for i in range(m,n+1):
    sum=sum+(i*i*i)
  print("SUM OF CUBES: ",sum)
