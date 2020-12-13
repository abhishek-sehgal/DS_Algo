def best_sum(target, vec):
    table = [None] * (target + 1)
    table[0] = []

    for i in range(target):
        if table[i] is not None:
            for num in vec:
                if i + num > target:
                    continue
                val = table[i + num]
                if val is None:
                    table[i + num] = [*table[i], num]
                else:
                    new_val = [*table[i], num]
                    if len(new_val) < len(val):
                        table[i + num] = [*table[i], num]

    return table[target]


print(best_sum(7, [5, 3, 4, 7]))
print(best_sum(8, [2, 3, 5]))
print(best_sum(8, [1, 4, 5]))
print(best_sum(100, [1, 2, 5, 25]))
