# Problem 19: Weighted Uniform Strings
# https://www.hackerrank.com/challenges/weighted-uniform-string/problem

def weightedUniformStrings(s, queries):
    weights = set()
    previous = ""
    count = 0

    for char in s:
        if char == previous:
            count += 1
        else:
            count = 1

        weight = (ord(char) - ord('a') + 1) * count
        weights.add(weight)
        previous = char

    result = []

    for query in queries:
        if query in weights:
            result.append("Yes")
        else:
            result.append("No")

    return result

s = input().strip()
queries_count = int(input().strip())
queries = []

for _ in range(queries_count):
    queries.append(int(input().strip()))

result = weightedUniformStrings(s, queries)
print("\n".join(result))
