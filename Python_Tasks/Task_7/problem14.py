# Problem 14: Anagram
# https://www.hackerrank.com/challenges/anagram/problem

from collections import Counter

def anagram(s):
    if len(s) % 2 != 0:
        return -1

    mid = len(s) // 2
    first = Counter(s[:mid])
    second = Counter(s[mid:])

    return sum(max(0, count - second[char]) for char, count in first.items())

q = int(input())

for _ in range(q):
    print(anagram(input().strip()))
