#fall on large nums
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