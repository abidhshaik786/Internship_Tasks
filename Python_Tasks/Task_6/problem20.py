
# Problem 20: Validating the Phone Number
# https://www.hackerrank.com/challenges/validating-the-phone-number/problem

import re

n = int(input())

for _ in range(n):
    number = input().strip()

    if re.fullmatch(r"[789]\d{9}", number):
        print("YES")
    else:
        print("NO")

