# Problem 7: Symmetric Difference
# https://www.hackerrank.com/challenges/symmetric-difference/problem

m = int(input())
a = set(map(int, input().split()))
n = int(input())
b = set(map(int, input().split()))

for num in sorted(a.symmetric_difference(b)):
    print(num)
