# Problem 20: No Idea!
# https://www.hackerrank.com/challenges/no-idea/problem

if __name__ == '__main__':
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    a = set(map(int, input().split()))
    b = set(map(int, input().split()))

    happiness = 0

    for num in array:
        if num in a:
            happiness += 1
        elif num in b:
            happiness -= 1

    print(happiness)
