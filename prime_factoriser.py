import sys
from math import sqrt, ceil

args = sys.argv
if len(args) != 2:
    print("Expected one argument: integer to be factorised")
    quit()

def gen_primes_under(num: int) -> list[int]:
    """Generates all primes under given integer n"""
    primes = []
    for i in range(2, num):
        if is_prime(i, primes):
            primes.append(i)

    return primes

def is_prime(num: int, primes: list[int]) -> bool: 
    # it's assumed that the primes are less than the number
    for prime in primes:
        if num % prime: # if it has a remainder after division
            continue
        return False
    
    return True

def prime_factors(num: int) -> list[int]:
    primes = gen_primes_under(int(num /2 +1))
    if is_prime(num, primes):
        return num
    prime_factors = []
    i = 0
    while num != 1:
        prime = primes[i]
        if num % prime == 0:
            prime_factors.append(prime)
            num /= prime
        else:
            i += 1
            
    return prime_factors


num = int(args[1])

print(str(prime_factors(num)).replace(",", "\n"))
