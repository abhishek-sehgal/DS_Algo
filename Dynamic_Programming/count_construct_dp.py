def count_construct(target, word_bank, memo=None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    if target == "":
        return 1

    total_count = 0

    for word in word_bank:
        if target.startswith(word):
            total_count += count_construct(target[len(word) :], word_bank, memo)

    memo[target] = total_count
    return total_count


print(count_construct("purple", ["purp", "p", "ur", "le", "purpl"]))
print(count_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(count_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(count_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
print(
    count_construct(
        "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
        ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"],
    )
)
