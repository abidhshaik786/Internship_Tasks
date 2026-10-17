# Problem 20: Piling Up!
# https://www.hackerrank.com/challenges/piling-up/problem

from collections import deque

for _ in range(int(input())):
    n = int(input())
    cubes = deque(map(int, input().split()))
    top = float('inf')

    while cubes:
        if cubes[0] >= cubes[-1]:
            cube = cubes.popleft()
        else:
            cube = cubes.pop()

        if cube > top:
            print("No")
            break

        top = cube
    else:
        print("Yes")
