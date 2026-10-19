# Problem 7: Alphabet Rangoli
# https://www.hackerrank.com/challenges/alphabet-rangoli/problem

import string

def print_rangoli(size):
    alphabet = string.ascii_lowercase
    width = 4 * size - 3
    lines = []

    for i in range(size - 1, -1, -1):
        left = alphabet[size - 1:i:-1]
        right = alphabet[i:size]
        line = "-".join(left + right).center(width, "-")
        lines.append(line)

    print("\n".join(lines + lines[-2::-1]))

n = int(input())
print_rangoli(n)
