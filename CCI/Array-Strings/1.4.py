"""Given a string, write a function to check if it is a permutation of a palindrome."""

from collections import Counter


def palindrome_permutation(string):
    """time: O(n) space: O(n)"""
    counter = Counter(string.lower())
    odds = [letter for letter in counter
            if letter.isalpha() and counter[letter] % 2 == 1]
    return len(odds) <= 1
