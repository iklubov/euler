from functools import reduce

import math
from time import time


def reverseNumber(number, reversed=0):
    if number < 10:
        return number + reversed
    lastNum = number % 10
    tailNum = number // 10
    return reverseNumber(tailNum, 10*(lastNum + reversed))

def get_divisors(n):
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


def get_prime_representation(value):
    def search(n):
        if n in primes:
            result[primes.index(n)] += 1
            lastEmpty[0] = primes.index(n)
            return
        newPrimes = [p for p in primes if p <= int(math.sqrt(n) + 1)]

        for i in range(lastEmpty[0], len(newPrimes)):
            pi = newPrimes[i]
            if n % pi == 0:
                result[i] += 1
                break
            elif len(result) <= i:
                lastEmpty[0] = i
        #print(n, result)
        if n/pi > 1:
            search(n/pi)

    primes = get_primes(value)
    result = [0] * len(primes)
    lastEmpty = [0]
    search(value)
    result = result[:lastEmpty[0]+1]
    return result

def get_prime_list(value):
    result = []
    repr = get_prime_representation(value)
    primes = get_primes(value)
    for i in range(len(repr)):
        counter = repr[i]
        if counter == 0:
            continue
        result.extend([primes[i]]*counter)
    return result


def isDegree(number, degree):
    while number > 1:
        if  number % degree > 0:
            return False
        number /= degree
    return True

def isTriangleNum(num):
    sq = math.sqrt(num*2)
    sqr = math.floor(sq)
    if 2*num == sqr*(sqr+1):
        return num
    return 0

def get_permutations(dim, gap):
    mainArr =[]
    appendArray([0]*dim, mainArr, dim, range(gap), lambda array:len(array) == len(set(array)))
    return mainArr

def get_array_permutations(value):
    mainArr = []
    appendArray([0] * len(value), mainArr, len(value), value, lambda array: sorted(array) == sorted(value) and array not in mainArr)
    return mainArr


def appendArray(array, mainArray, dim, iterator, filterFunction, recurseDepth=0):
    for i in iterator:
        #print(recurseDepth, dim, array, i, iterator)
        array[recurseDepth] = i
        if recurseDepth < dim - 1:
            appendArray(array, mainArray, dim, iterator, filterFunction, recurseDepth+1)
        elif filterFunction(array):
            mainArray.append(array.copy())










