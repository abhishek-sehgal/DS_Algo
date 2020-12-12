def can_sum(target, vec):
    table = [False] * (target + 1)
    table[0] = True

    for i in range(target):
        if not table[i]:
            continue
        for num in vec:
            if i + num <= target:
                table[i + num] = True

    return table[-1]


print(can_sum(7, [5, 3, 4]))
print(can_sum(7, [5, 3, 4, 7]))
print(can_sum(7, [2, 4]))
print(can_sum(8, [2, 3, 5]))
print(can_sum(300, [7, 14]))
