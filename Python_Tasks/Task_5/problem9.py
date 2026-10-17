# Problem 9: Word Order
# https://www.hackerrank.com/challenges/word-order/problem

n = int(input())
words = {}

for _ in range(n):
    word = input()
    words[word] = words.get(word, 0) + 1
print(len(words))
print(*words.values())
