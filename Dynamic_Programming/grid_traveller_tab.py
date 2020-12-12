def grid_travller(m, n):
    table = [[0]*(n+1) for _ in range(m+1)]
    table[1][1] = 1
    for i in range(m+1):
        for j in range(n+1):
            if (i+1)<=m:
                table[i + 1][j] += table[i][j]
            if (j+1)<=n:
                table[i][j + 1] += table[i][j]

    return table[m][n]

print(grid_travller(1, 1))
print(grid_travller(2, 3))
print(grid_travller(3, 2))
print(grid_travller(3, 3))
print(grid_travller(18, 18))
