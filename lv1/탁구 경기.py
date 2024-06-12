def winner(rounds):
    dalgu, phonix = 0, 0
    for _ in range(rounds):
        win = input().strip()
        if win == "D":
            dalgu += 1
        elif win == "P":
            phonix += 1
        if abs(dalgu - phonix) >= 2:
            break
    print(f"{dalgu}:{phonix}")

rounds = int(input())
winner(rounds)