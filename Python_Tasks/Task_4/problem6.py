# Problem 6: Find the Runner-Up Score
# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
    n = int(input())
    scores = list(map(int, input().split()))

    scores = sorted(set(scores))
    print(scores[-2])
