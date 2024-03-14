a = input('Enter an array(separated by space): ').split()
lst = []
for number in a:
    number = int(number)
    lst.append(number)
    
total = sum(lst)
total_left = 0

for i in range(len(a)):
    total -= int(a[i])
    if total == total_left:
        print(f'YES! The number is in {i} position')
        total_left += int(a[i])
        break
    else:
        print('NO')
