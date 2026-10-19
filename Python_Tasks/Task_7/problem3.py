# Problem 3: Mars Exploration
# https://www.hackerrank.com/challenges/mars-exploration/problem

def marsExploration(s):
    count = 0

    for i, char in enumerate(s):
        if char != "SOS"[i % 3]:
            count += 1

    return count

s = input().strip()
print(marsExploration(s))
