def max_m(T):
    max_sq = 0
    for _ in range(T):
        W, H = map(int, input().split())
        if W * H > max_sq:
            max_sq = W * H
    return max_sq

T = int(input())
print(max_m(T))
