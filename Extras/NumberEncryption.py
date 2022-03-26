s=input()
c=input()

s = list(s)

for i in range(len(s)):
    s[i] = int(s[i])

index = 0
for i in range(len(c)):
    if c[i]=='R':
        if index + 1 < len(s):
            index = index+1
    if c[i]=='L':
        if index > 0:
            index = index -1
    if c[i]=='T':
        if s[index] != 9:
            s[index] += 1
    if c[i]=='D':
        if s[index] != 0:
            s[index]-= 1
    if c[i]=='S':
        i+=1
        ind = int(c[i]) - 1
        if(ind<len(s) and ind>=0 and ind<=9):
            num = s[index]
            s[index] = s[ind]
            s[ind] = num

ans = ""
for i in s:
    ans += "{}".format(i)
print(ans,end="")