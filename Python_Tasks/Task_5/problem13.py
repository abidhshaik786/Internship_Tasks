# Problem 13: Nested Lists
# https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    students = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    second = sorted(set(s[1] for s in students))[1]

    for name, score in sorted(students):
        if score == second:
            print(name)
