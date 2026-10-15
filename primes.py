#!/usr/bin/env python3
"""Generate and print the first 100 prime numbers."""


def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def first_primes(count):
    primes = []
    n = 2
    while len(primes) < count:
        if is_prime(n):
            primes.append(n)
        n += 1
    return primes


if __name__ == "__main__":
    for p in first_primes(100):
        print(p)
