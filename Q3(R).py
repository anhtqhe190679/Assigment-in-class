import random
n = random.randint(0,101)
print(n)
x = int(input('Guess the number: '))
while True:
    if n == x:
        print('EXACTLY!')
        break
    elif n < x:
        print('n < x (guess lower)')
        x = int(input('Guess the number: '))
    elif n > x:
        print('n > x (guess higher)')
        x = int(input('Guess the number: '))
        
