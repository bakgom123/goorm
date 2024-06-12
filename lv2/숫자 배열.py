def num_list(N):
    for i in range(N):
        line = []
        for j in range(1, N + 1):
            line.append(str(i * N + j))
        print(" ".join(line))

N = int(input())
num_list(N)