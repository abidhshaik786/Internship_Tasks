# Problem 6: Pangrams
# https://www.hackerrank.com/challenges/pangrams/problem

def pangrams(s):
    if set("abcdefghijklmnopqrstuvwxyz").issubset(set(s.lower())):
        return "pangram"

    return "not pangram"

print(pangrams(input().strip()))
