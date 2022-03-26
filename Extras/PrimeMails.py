n=int(input())
prime = [True for i in range(n + 1)]
p = 2
while(p * p <= n):
  if (prime[p] == True):
    for i in range(p ** 2, n + 1, p):
      prime[i] = False
  p += 1
        
prime[0]=False
prime[1]=False
count = [0 for i in range(n)]
for i in range (n):
  if(prime[i]==True):
    count[i]=1+count[i-1]
           
  else:
    count[i]=count[i-1]


res=0
c = n-1
while(c>1):
  res= res+ 1
  c = c-count[c]
   
print(res+1)