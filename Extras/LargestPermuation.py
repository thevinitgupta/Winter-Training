n = input("")
li = list(n)
count = 0
for i in range(len(li)):
    if li[i]=='0':
        count += 1
    li[i]= int(li[i])
    
li.sort(reverse=True)

ans = ""
for i in range(len(li)):
    ans = ans + str(li[i])
    
if count==len(li):
    print(0)
else:
    print(ans)