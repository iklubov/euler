
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.
import fractions
import math
import random
from functools import reduce

import time

from utils import reverseNumber, divisorGenerator


def task1():
    ssum = 0
    for i in range(0, 1000):
        if not i%3 or not i%5:
            ssum = ssum + i
    print(ssum)

#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
def task2():
    ssum = 0
    first, second = 1,2
    while second <= 4000000:
        print(first, second)
        if second%2 == 0:
            print( second)
            ssum = ssum + second
        tf = second
        second = second + first
        first = tf
    print(ssum)

#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?
def task3():
    num = 600851475143
    dividers = []
    while num > 2:
        print(num, dividers)
        for i in range(2,int(num)+1):
            if num%i == 0:
                dividers.append(i)
                num = num / i
                break

    print(dividers)

#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.
def task4():
    result = 0
    for i in range(1,1000):
        for j in range(1,1000):
            mul = i*j
            if reverseNumber(mul) == mul and mul > result:
                result = mul
    print(result)

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
def task5():
    numToAchieve = 20
    result = 1
    listRemoved = []
    sqrt = int(math.sqrt(numToAchieve))
    for i in range(2, numToAchieve):
        if i in listRemoved:
            continue
        removei = i
        resulti = i
        counter = 1
        while removei <= numToAchieve:
            if removei not in listRemoved:
                listRemoved.append(removei)
                resulti = removei
            removei *= i
            counter += 1
        result *= resulti
        listRemoved.sort()
        for j in listRemoved:
            for k in listRemoved:
                if k*j <= numToAchieve and k*j not in listRemoved:
                    listRemoved.append(k*j)
        listRemoved.sort()
        #print (listRemoved, i ,resulti )
    print(result)

#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
def task6():
    number = 1000000
    result = 0
    sum = 1
    for i in range(1,number):
        print(sum, i, (i+1)*sum)
        result += (i+1)*sum
        sum += (i+1)
    result *= 2
    print(result)

#What is the 10 001st prime number?
def task7():
    primeNums = [2]
    firstNum = 2
    while len(primeNums) < 10001:
        firstNum += 1
        if any(firstNum%num==0 for num in primeNums):
            continue
        primeNums.append(firstNum)
        print(len(primeNums))
    print (primeNums[0], primeNums[-1])

def task8():
    numStr = '7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'
    maxProd = 1
    adjNum = 13
    offset = 0
    maxProdString = ''
    while (len(numStr) - offset) > adjNum:
        thisProd = numStr[offset:offset+adjNum]
        thisProdValue = reduce(lambda x, y: int(x)*int(y), thisProd)
        if thisProdValue > maxProd:
            maxProd = thisProdValue
            maxProdString = thisProd
        offset = offset + 1
    print(maxProd, maxProdString)

def task9():
    ct = time.time()
    pifSum = 1000
    def brutForce():
        for k in range(1, 999):
            for j in range(1, k):
                for i in range(1, j):
                    if i**2 + j**2 == k**2:
                        #print(i,j,k, sum([i,j,k]))
                        if sum([i,j,k]) == 1000:
                            print(i*j*k, time.time() - ct)
                            return
    for m in divisorGenerator(pifSum/2):
        for k in divisorGenerator(pifSum/(2*m)):
            if k - m < m and k - m > 0 and fractions._gcd(m,k - m) == 1:
                n = k - m
                d = pifSum/(2*m*k)
                print((m**2+n**2)*d, 2*m*n*d, (m**2-n**2)*d)
    print(time.time() - ct)
    brutForce()

#task9
print(divisorGenerator(996))
#for i in divisorGenerator(66666843216849849421321468498498513213213546546565165848784):
# num = 500
# while len(str(num)) < 30:
#     ct = time.time()
#     num *= 10
#     num += random.randint(0,9)
#     print(num, divisorGenerator(num), time.time()-ct)
#print(list(divisorGenerator(565666666666665695899999999999999999999999999956454444444444444444454666666666666843216849849421321468498498513213213546546565165848784)))