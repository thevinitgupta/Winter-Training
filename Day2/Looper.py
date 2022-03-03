from audioop import mul


val = int(input('Enter value for table\n'))

multiplier =1;
while multiplier<=10 :
    print(val,"X",multiplier,"=",val*multiplier)
    multiplier += 1


for multiplier in range(1,11):
    print(val,"X",multiplier,"=",val*multiplier)

for multiplier in range(1,11,2):
    print(val,"X",multiplier,"=",val*multiplier)

for multiplier in range(11,0,-2):
    print(val,"X",multiplier,"=",val*multiplier)

for ch in 'haldia':
    print(ch)