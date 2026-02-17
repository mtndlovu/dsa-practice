for i in range(5):
    row = list(map(int, input().split()))
    for j in range(5):
        if row[j]:
            moves = abs(2 - i) + abs(2 - j)
            print(moves)
            break