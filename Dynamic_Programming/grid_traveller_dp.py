def grid_travller(m, n, memo=None):
    if memo is None:
        memo = {}
    key = f"{m},{n}"
    if (key) in memo:
        return memo[key]
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    else:
        memo[key] = grid_travller(m - 1, n, memo) + grid_travller(m, n - 1, memo)
    return memo[key]


print(grid_travller(1, 1))
print(grid_travller(2, 3))
print(grid_travller(3, 2))
print(grid_travller(3, 3))
print(grid_travller(18, 18))
