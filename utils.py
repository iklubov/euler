from functools import reduce

import math


def reverseNumber(number, reversed=0):
    if number < 10:
        return number + reversed
    lastNum = number % 10
    tailNum = number // 10
    return reverseNumber(tailNum, 10*(lastNum + reversed))

def get_divisors(num):
    result = []
    for i in range(1, math.floor(math.sqrt(num))+1):
        if num%i == 0:
            result.append(i)
            if i * i == num:
                continue
            result.append(num/i)
    return result

def isDegree(number, degree):
    while number > 1:
        if  number % degree > 0:
            return False
        number /= degree
    return True



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










