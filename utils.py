
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

def getKollatzSeq(num):
    counter = 1
    #nums = [str(num)]
    #start = num
    while num > 1:
        num = num / 2 if num % 2 == 0 else 3*num + 1
        counter += 1
        #nums.append(str(int(num)))
    #print(start, counter, "->".join(nums))
    return counter

exists = []

def inttobyte(x):
    n = []
    while x > 0:
        y = x % 2
        n.append(str(y))
        x = int(x/2)
    strt = "".join(reversed(n))
    return strt

def checkforlattice(x, digit, lenInterval, numToReach):
    digits = 0
    notDigits = 0
    while x > 0:
        y = x % 2
        if y == digit: digits += 1
        else: notDigits += 1
        if notDigits > (lenInterval - numToReach):
            return False
        if digits > numToReach:
            return False
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










