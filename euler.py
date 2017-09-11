
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.
import fractions
import math
import time
from functools import reduce

from garbage import get_primes
from utils import reverseNumber, get_divisors


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
    pifSum = 1000
    def brutForce():
        ct = time.time()
        for k in range(1, 999):
            for j in range(1, k):
                for i in range(1, j):
                    if i**2 + j**2 == k**2:
                        #print(i,j,k, sum([i,j,k]))
                        if sum([i,j,k]) == 1000:
                            print('brutForce', i,j,k, time.time() - ct)
                            return
    def cleverWay():
        ct = time.time()
        for m in get_divisors(pifSum/2):
            for k in get_divisors(pifSum/(2*m)):
                if k - m < m and k - m > 0 and fractions._gcd(m,k - m) == 1:
                    n = k - m
                    d = pifSum/(2*m*k)
                    print('cleverWay', (m**2+n**2)*d, 2*m*n*d, (m**2-n**2)*d, time.time() - ct)
    brutForce()
    cleverWay()

def task10():
    NUM = 2000000
    print(sum(get_primes(NUM)))


def task11():
    grid = "08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08 \
            49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00 \
            81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65 \
            52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91 \
            22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80 \
            24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50 \
            32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70 \
            67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21 \
            24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72 \
            21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95 \
            78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92 \
            16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57 \
            86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58 \
            19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40 \
            04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66 \
            88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69 \
            04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36 \
            20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16 \
            20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54 \
            01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"

    adjacentNum = 4
    data = [int(i) for i in grid.split(' ') if len(i)]
    dimensionNum = int(math.sqrt(len(data)))
    currentIndex = 0
    maxNums = 0, 0, 0, 0

    def getNextIndexes(horiz, vert, shift):
        return ((horiz + shift)%dimensionNum, vert) , (horiz, (vert + shift)%dimensionNum), ((horiz + shift)%dimensionNum,(vert + shift)%dimensionNum), ((horiz + shift)%dimensionNum,(vert - shift + dimensionNum)%dimensionNum)
    def getCoord(t):
        return t[1]*dimensionNum + t[0]

    while currentIndex < len(data):
        counter = 0
        horizCoord = currentIndex % dimensionNum
        vertCoord = math.floor(currentIndex / dimensionNum)
        horizMult, vertMult, diagMultud, diagMultdu  = 1,1,1,1
        while counter < adjacentNum:
            h, v, dud, ddu  = getNextIndexes(horizCoord, vertCoord, counter)
            horizMult *= data[getCoord(h)]
            vertMult *= data[getCoord(v)]
            diagMultud *= data[getCoord(dud)]
            diagMultdu *= data[getCoord(ddu)]
            counter += 1
        maxNums = max(maxNums[0], horizMult), max(maxNums[1], vertMult),max(maxNums[2], diagMultud), max(maxNums[3], diagMultdu)
        currentIndex += 1
    print(maxNums)

def task12(maxNum):
    i = 0
    nextLen = []
    maxLen = []
    while maxNum > i:
        #j = (i + 1)
        #i += j
        i += 1
        nextLen = get_divisors(i)
        if len(maxLen) < len(nextLen):
            maxLen = nextLen
        if True:#j % 128 == 0:
            print(i, len(nextLen))
    print('RESULT', i, maxLen)

task12(50000)
