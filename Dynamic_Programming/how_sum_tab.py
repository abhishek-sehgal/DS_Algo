def how_sum(target, vec):
    table = [None] * (target + 1)
    table[0] = []
    for i in range(target):
        if table[i] is not None:
            for num in vec:
                if i + num <= target:
                    table[i + num] = [*table[i], num]
    return table[target]


print(how_sum(7, [2, 3]))
print(how_sum(7, [5, 3, 4, 7]))
print(how_sum(7, [2, 4]))
print(how_sum(8, [2, 3, 5]))
print(how_sum(300, [7, 14]))
