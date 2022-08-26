'''This module is having
- variable 'name'
- functions like is_even_odd(), factorial(), is_prime()
'''

name= 'Aditya Tripathi'

def is_even_odd(num):
    if num%2 == 0:
        return f'{num} is even no.'
    else:
        return f'{num} is odd no.'

def factorial(num):
    f=1
    for i in range(num,0,-1):
        f *= i
    return f'factorial of {num} is {f}.'

def is_prime(num):
    count = 0
    if (num == 1):
        return '1 is neither prime nor composite'
    else:
        for i in range (2, (num//2)+1):
            if (num % i == 0):
                count += 1
        if (count == 0):
            return f'{num} is prime number'
        else:
            return f'{num} is not a prime number'


if __name__=='__main__':
    print(name)
    print(is_prime(45))
    print(factorial(3))




