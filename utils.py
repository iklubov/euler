from functools import reduce

import math


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