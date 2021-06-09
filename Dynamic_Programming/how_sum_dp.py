def how_sum(target, vec, memo=None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return None

    for num in vec:
        remainder = target - num
        result = how_sum(remainder, vec, memo)
        if result is not None:
            memo[target] = [*result, num]
            return memo[target]

    memo[target] = None
    return None


print(how_sum(7, [2, 3]))
print(how_sum(7, [5, 3, 4, 7]))
print(how_sum(7, [2, 4]))
print(how_sum(8, [2, 3, 5]))
print(how_sum(300, [7, 14]))
