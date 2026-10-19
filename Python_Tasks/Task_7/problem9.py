# Problem 9: Beautiful Binary String
# https://www.hackerrank.com/challenges/beautiful-binary-string/problem

def beautifulBinaryString(b):
    return b.count("010")

n = int(input())
b = input().strip()

print(beautifulBinaryString(b))
