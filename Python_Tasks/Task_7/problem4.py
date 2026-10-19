# Problem 4: Funny String
# https://www.hackerrank.com/challenges/funny-string/problem

def funnyString(s):
    for i in range(1, len(s)):
        if abs(ord(s[i]) - ord(s[i - 1])) != abs(ord(s[-i]) - ord(s[-i - 1])):
            return "Not Funny"

    return "Funny"

q = int(input())

for _ in range(q):
    print(funnyString(input().strip()))
