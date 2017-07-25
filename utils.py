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
            #print('curN', curN)
            #divisor = search(curN)
            #print('divisor', newDivisor)
            divisors.append(curN)
            divisors.append(n / curN)
            #print(curN)
            curN = curN/newDivisor
            newDivisor = search(curN)
            # if not newDivisor:
            #     divisors.append(int(curN))
            #     divisors.append(int(n / curN))
            #     break
    return sorted(divisors)


# def divisorGenerator(n):
#     large_divisors = [],
#     for i in range(1, int(math.sqrt(n) + 1)):
#         if n % i == 0:
#             yield i
#             if i*i != n:
#                 large_divisors.append(n / i)
#     for divisor in reversed(large_divisors):
#         yield divisor