"""
Sieve of Eratosthenes
"""

def sieve_of_eratosthenes(n):
    """
    Generate primes numbers <= n
    """
    sieve = [True for i in range(n)]
    p = 2
    while 2*p <= n:
        for m in range(2*p, n+1, p):
            sieve[m-1] = False
        for i in range(p+1, n+1):
            if sieve[i-1]:
                p = i
                break
    primes = []
    for i in range(2, n+1):
        if sieve[i-1]:
            primes.append(i)
    return primes

def goldbach_conjecture(n):
    """
    Goldbach's conjecture states that every
    even number greater than 2 can be expressed
    as sum of two prime numbers
    """
    # Check if n is even
    if not n&1:
        primes = sieve_of_eratosthenes(n)
        hashmap = set(primes)
        for elem in primes:
            if (remaining := n - elem) in hashmap:
                return elem, remaining
        

print(goldbach_conjecture(30))