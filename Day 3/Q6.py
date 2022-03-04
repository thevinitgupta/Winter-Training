from re import I


inp = "Dil mera machal machal jaye, haye"

inp = inp.split(' ')
d1={}

for word in inp :
    curr = 1
    if word in d1.keys():
        curr = d1[word]
        curr += 1
    d1[word]=curr

ma = max(d1.values())
word = ''
for i in d1.keys():
    if d1[i]== ma:
        word=i

print(word)
