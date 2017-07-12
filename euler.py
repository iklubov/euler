
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.
import math

from utils import reverseNumber


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



task7()