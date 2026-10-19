# Problem 13: Sherlock and the Valid String
# https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem

from collections import Counter

def isValid(s):
    frequencies = Counter(Counter(s).values())

    if len(frequencies) == 1:
        return "YES"

    if len(frequencies) != 2:
        return "NO"

    (freq1, count1), (freq2, count2) = frequencies.items()

    if count1 == 1 and (freq1 == 1 or freq1 - 1 == freq2):
        return "YES"

    if count2 == 1 and (freq2 == 1 or freq2 - 1 == freq1):
        return "YES"

    return "NO"

print(isValid(input().strip()))
