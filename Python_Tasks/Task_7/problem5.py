# Problem 5: Alternating Characters
# https://www.hackerrank.com/challenges/alternating-characters/problem

def alternatingCharacters(s):
    deletions = 0

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            deletions += 1

    return deletions

q = int(input())

for _ in range(q):
    print(alternatingCharacters(input().strip()))
