def collect_coins(labyrinth, n, m):
    for i in range(n):
        for j in range(m):
            if labyrinth[i][j] == 0:
                scrooge_position = (i, j)
                break

    coins_collected = 0
    while True:
        current_x, current_y = scrooge_position
        moves = {'left': (current_x, current_y - 1), 'right': (current_x, current_y + 1),
                 'up': (current_x - 1, current_y), 'down': (current_x + 1, current_y)}
        best_move = None
        max_coins = 0

        for move in ['left', 'right', 'up', 'down']:
            nx, ny = moves[move]
            if 0 <= nx < n and 0 <= ny < m:
                if labyrinth[nx][ny] > max_coins:
                    max_coins = labyrinth[nx][ny]
                    best_move = (nx, ny)

        if best_move and max_coins > 0:
            scrooge_position = best_move
            labyrinth[best_move[0]][best_move[1]] -= 1
            coins_collected += 1
        else:
            break

    return coins_collected


N, M = map(int, input().split())
labyrinth = [list(map(int, input().split())) for i in range(N)]
print(collect_coins(labyrinth, N, M))
