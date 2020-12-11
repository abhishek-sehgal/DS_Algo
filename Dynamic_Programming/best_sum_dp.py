"""
Given a target sum, can you provide the least amount of numbers 
that add up to the target from a given set of vectors?
If not, return empty array
"""


def best_sum(target, vec, memo=None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return None

    shortest_combination = None

    for num in vec:
        remainder = target - num
        result = best_sum(remainder, vec, memo)

        if result is not None:
            combination = [*result, num]
            if shortest_combination is None or len(combination) < len(
                shortest_combination
            ):
                shortest_combination = combination

    memo[target] = shortest_combination
    return shortest_combination


print(best_sum(7, [5, 3, 4, 7]))
print(best_sum(8, [2, 3, 5]))
print(best_sum(8, [1, 4, 5]))
print(best_sum(100, [1, 2, 5, 25]))
