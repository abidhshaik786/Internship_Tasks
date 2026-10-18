
# Problem 19: Company Logo
# https://www.hackerrank.com/challenges/most-commons/problem

from collections import Counter

s = input().strip()
counts = Counter(s)

result = sorted(counts.items(), key=lambda x: (-x[1], x[0]))

for char, count in result[:3]:
    print(char, count)

