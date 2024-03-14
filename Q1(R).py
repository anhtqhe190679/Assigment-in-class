import math
a = input('Enter a sequence of positive integers: ').split(' ')
while True:
    for i in a:
        if int(i) <= 0:
            a = input('Enter a sequence of positive integers: ').split(' ')
        else:
            break    
    break

lst_prime_numbers = []
def prime_number(a):
    for number in a:
        number = int(number)
        for i in range(1, round(math.sqrt(number))):
            if number % i ==0:
                continue
            else:
                lst_prime_numbers.append(number)
    print(lst_prime_numbers)
    print('Largest prime number: ',max(lst_prime_numbers))
prime_number(a)
    
            
    