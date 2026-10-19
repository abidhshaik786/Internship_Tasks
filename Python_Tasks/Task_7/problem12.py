# Problem 12: Making Anagrams
# https://www.hackerrank.com/challenges/making-anagrams/problem

from collections import Counter

def makingAnagrams(s1, s2):
    count1 = Counter(s1)
    count2 = Counter(s2)

    return sum(abs(count1[ch] - count2[ch]) for ch in set(s1 + s2))

s1 = input().strip()
s2 = input().strip()

print(makingAnagrams(s1, s2))
