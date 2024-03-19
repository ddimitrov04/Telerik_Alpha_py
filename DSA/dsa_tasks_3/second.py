def dfs(matrix, visited, i, j, N, M):
    if i < 0 or i >= N or j < 0 or j >= M or visited[i][j]:
        return 0

    visited[i][j] = True
    area_size = 1

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in directions:
        nx, ny = i + dx, j + dy
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and matrix[i][j] == matrix[nx][ny]:
            area_size += dfs(matrix, visited, nx, ny, N, M)

    return area_size

def largest_surface(matrix, N, M):
    visited = [[False for _ in range(M)] for _ in range(N)]
    max_area = 0

    for i in range(N):
        for j in range(M):
            if not visited[i][j]:
                area = dfs(matrix, visited, i, j, N, M)
                max_area = max(max_area, area)

    return max_area

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

print(largest_surface(matrix, N, M))