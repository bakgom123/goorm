def max_manhattan_distance(a, b, c, d):
    numbers = [a, b, c, d]
    numbers.sort()
    manhattan_distance = (numbers[-1] - numbers[0]) + (numbers[-2] - numbers[1])
    return manhattan_distance

a, b, c, d = map(int, input().split())

print(max_manhattan_distance(a, b, c, d))