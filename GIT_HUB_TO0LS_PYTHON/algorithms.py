# algorithms.py
from __future__ import annotations


def is_palindrome(text: str) -> bool:
    """Check if a text is a palindrome (ignores spaces and case)."""
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]


def factorial(n: int) -> int:
    """Return n! (factorial). Raises ValueError for negative n."""
    if n < 0:
        raise ValueError("n must be >= 0")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def fibonacci(n: int) -> list[int]:
    """Return the first n Fibonacci numbers. Raises ValueError for n < 0."""
    if n < 0:
        raise ValueError("n must be >= 0")
    seq: list[int] = []
    a, b = 0, 1
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq


def count_vowels(text: str) -> int:
    """Count vowels (a, e, i, o, u) in a string, case-insensitive."""
    vowels = set("aeiou")
    return sum(1 for ch in text.lower() if ch in vowels)


def sum_even_numbers(nums: list[int]) -> int:
    """Sum only even numbers from a list."""
    return sum(n for n in nums if n % 2 == 0)
