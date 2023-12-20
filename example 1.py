#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import timeit
from functools import lru_cache


def factorial_recursive(n):  # Рекурсивный факториал
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)


@lru_cache
def factorial_recursive_cached(n):  # Рекурсивный факториал с lru_cache
    if n == 0:
        return 1
    else:
        return n * factorial_recursive_cached(n - 1)


def factorial_iterative(n):  # Итеративный факториал
    product = 1
    while n > 1:
        product *= n
        n -= 1
    return product


def fib_recursive(n):  # Рекурсивный фибоначчи без кэширования
    if n == 0 or n == 1:
        return n
    else:
        return fib_recursive(n - 2) + fib_recursive(n - 1)


@lru_cache
def fib_recursive_cached(n):  # Рекурсивный фибоначчи с lru_cache
    if n == 0 or n == 1:
        return n
    else:
        return fib_recursive_cached(n - 2) + fib_recursive_cached(n - 1)


def fib_iterative(n):  # Итеративный фибоначчи
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


if __name__ == '__main__':
    N = 20  # Число для рассчета

    time_fac_rec = timeit.timeit(
        lambda: factorial_recursive(N), number=1000)
    time_fac_rec_cached = timeit.timeit(
        lambda: factorial_recursive_cached(N), number=1000)
    time_fac_iterative = timeit.timeit(
        lambda: factorial_iterative(N), globals=globals(), number=1000)
    time_fib_rec = timeit.timeit(
        lambda: fib_recursive(N), globals=globals(), number=1000)
    time_fib_iterative = timeit.timeit(
        lambda: fib_iterative(N), globals=globals(), number=1000)
    time_fib_rec_cached = timeit.timeit(
        lambda: fib_recursive_cached(N), globals=globals(), number=1000)

    print(f"Factorial recursive time: {time_fac_rec}"
          f"\nFactorial iterative time: {time_fac_iterative}"
          f"\nFibonacci recursive cached time: {time_fac_rec_cached}"
          f"\nCached {time_fac_rec/time_fac_rec_cached} times faster"
          )

    print(f"Fibonacci recursive time: {time_fib_rec}"
          f"\nFibonacci iterative time: {time_fib_iterative}"
          f"\nFibonacci recursive cached time: {time_fib_rec_cached}"
          f"\nCached {time_fib_rec/time_fib_rec_cached} times faster"
          )
