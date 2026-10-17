# Problem 17: No Idea!
# https://www.hackerrank.com/challenges/no-idea/problem

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
happy = set(map(int, input().split()))
sad = set(map(int, input().split()))

score = 0

for num in numbers:
    if num in happy:
        score += 1
    elif num in sad:
        score -= 1
print(score)
