#!/usr/bin/env python3
"""Generate and print the first 100 prime numbers."""

from collections.abc import Iterator


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def first_primes(count: int) -> Iterator[int]:
    found = 0
    n = 2
    while found < count:
        if is_prime(n):
            yield n
            found += 1
        n += 1


if __name__ == "__main__":
    for p in first_primes(100):
        print(p)
