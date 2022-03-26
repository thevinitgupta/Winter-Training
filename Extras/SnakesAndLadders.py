size = 10

bGame = []
ind=0
while ind <size:
    if ind % 2 == 1: bGame = input().split() + bGame
    else: bGame = input().split()[::-1] + bGame
    ind += 1
bGame = ['0'] + bGame

dp = ['0'] * 101
dic = {'Start': 1, 'End': 100}

for ind, val in enumerate(bGame):
    if (val[0] == 'S' or val[0] == 'L') and val[1] == '(':
        if val[2].isdigit():
            dp[ind] = int(val[2:-1])
        else: dp[ind] = dic[val[2:-1]]
    else:
        dp[ind] = dic.get(val[2:-1], ind)

dies = list(map(int, input().split()))
curr = 0
s, l = 0, 0

for val in dies:
    if curr + val < 101: curr += val
    while dp[curr] != curr: 
        if curr > dp[curr]: s += 1
        else: l += 1
        curr = dp[curr]

if curr == 100:
    print('Possible {} {}'.format(s,l))
else: 
    print(f'Not possible {s} {l} {"Start" if curr == 1 else curr}')