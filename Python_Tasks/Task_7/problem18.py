# Problem 18: String Construction
# https://www.hackerrank.com/challenges/string-construction/problem

def stringConstruction(s):
    return len(set(s))

q = int(input())

for _ in range(q):
    print(stringConstruction(input().strip()))
