# Problem 15: Game of Thrones - I
# https://www.hackerrank.com/challenges/game-of-thrones/problem

from collections import Counter

def gameOfThrones(s):
    odd_count = sum(1 for count in Counter(s).values() if count % 2 != 0)

    if odd_count <= 1:
        return "YES"

    return "NO"

print(gameOfThrones(input().strip()))
