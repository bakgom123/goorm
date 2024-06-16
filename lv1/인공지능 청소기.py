N = int(input())
for _ in range(N):
	a, b, c = map(int, input().split())
	if abs(a) + abs(b) <= c and (abs(a) + abs(b) - c) % 2 == 0:
		print("YES")
	else:
		print("NO")

