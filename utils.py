def reverseNumber(number, reversed=0):
    if number < 10:
        return number + reversed
    lastNum = number % 10
    tailNum = number // 10
    return reverseNumber(tailNum, 10*(lastNum + reversed))