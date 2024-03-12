import random

c = 0
a = int(input('Input the range for guessed number: '))
b = random.randint(c, a+1)

while True:
    answer = input(f'Is {b} too high(h), too low(l), or correct(r): ')
    if answer == 'h':
        b = random.randint(c, b)
    elif answer == 'l':
        b = random.randint(b, a)
    else:   
        print(f'Welldone! The computer guessed your number {b} correctly!')
        break