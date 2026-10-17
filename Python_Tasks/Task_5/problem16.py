# Problem 16: Collections.Counter()
# https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter

n = int(input())
shoes = Counter(map(int, input().split()))
money = 0

for _ in range(int(input())):
    size, price = map(int, input().split())

    if shoes[size] > 0:
        money += price
        shoes[size] -= 1
print(money)
