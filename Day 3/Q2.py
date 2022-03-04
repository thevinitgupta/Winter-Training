inp = input("Enter a sentence : ").lower()

words = inp.split(' ')
capital = ''
k=0
for word in words : 
    capital += word[0].upper()+word[1:]+' '

print(capital)