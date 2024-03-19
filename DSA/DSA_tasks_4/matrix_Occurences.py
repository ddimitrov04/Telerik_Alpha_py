# Exercise appends to be similar to dsa_tasks_3 second exercise.
def dfs(matrix, x, y, visited):
    if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0])\
            or matrix[x][y] == 0 or visited[x][y]:
        return 0
    visited[x][y]= True
    size = 1
    size += dfs(matrix, x - 1, y, visited)
    size += dfs(matrix, x + 1, y, visited)
    size += dfs(matrix, x, y - 1, visited)
    size += dfs(matrix, x, y + 1, visited)
    return size

def find_same(matrix):
    N = len(matrix)
    M = len(matrix[0])
    visited = [[False for _ in range(M)] for _ in range(N)]
    same = []
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 1 and not visited[i][j]:
                sames = dfs(matrix, i, j, visited)
                same.append(sames)
    same.sort(reverse=True)
    return same


N, M = map(int, input().split())
matrixx = [list(map(int, list(input()))) for _ in range(N)]

all = find_same(matrixx)
for same in all:
    print(same)
