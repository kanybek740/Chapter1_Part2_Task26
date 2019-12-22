numbers = input('vvedi chislo: ')
num = list(numbers.split(','))
chetnye = []
nechetnye = []
for number in (num):
    if int(number) % 2 == 0:
        chetnye.append(num)
   
    else: 
        nechetnye.append(num)
print(len(chetnye), len(nechetnye))