from functools import reduce

import math
from time import time


def reverseNumber(number, reversed=0):
    if number < 10:
        return number + reversed
    lastNum = number % 10
    tailNum = number // 10
    return reverseNumber(tailNum, 10*(lastNum + reversed))

def divisorGenerator(n):
    divisors = []
    def search(n):
        for i in range(2, int(math.sqrt(n) + 1)):
            if n % i == 0:
                return i
    curN = n
    newDivisor = search(curN)
    while newDivisor:
            divisors.append(curN)
            divisors.append(n / curN)
            curN = curN/newDivisor
            newDivisor = search(curN)

    return sorted(divisors)

def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes



