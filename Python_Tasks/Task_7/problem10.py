# Problem 10: CamelCase
# https://www.hackerrank.com/challenges/camelcase/problem

def camelcase(s):
    if not s:
        return 0

    count = 1

    for char in s:
        if char.isupper():
            count += 1

    return count

print(camelcase(input().strip()))
