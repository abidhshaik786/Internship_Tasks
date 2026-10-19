# Problem 17: Separate the Numbers
# https://www.hackerrank.com/challenges/separate-the-numbers/problem

def separateNumbers(s):
    for length in range(1, len(s) // 2 + 1):
        first = s[:length]

        if first.startswith("0"):
            continue

        number = int(first)
        current = first

        while len(current) < len(s):
            number += 1
            current += str(number)

        if current == s:
            print("YES", first)
            return

    print("NO")

q = int(input())

for _ in range(q):
    separateNumbers(input().strip())
