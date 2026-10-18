
# Problem 16: Check Subset
# https://www.hackerrank.com/challenges/py-check-subset/problem

t = int(input())

for _ in range(t):
    n = int(input())
    a = set(map(int, input().split()))

    m = int(input())
    b = set(map(int, input().split()))

    print(a.issubset(b))

