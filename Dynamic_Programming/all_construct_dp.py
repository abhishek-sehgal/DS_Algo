def all_construct(target, word_bank, memo=None):
    if memo is None: memo = {}
    if target in memo: return memo[target]
    if target == '': return [[]]

    ways = []

    for word in word_bank:
        if target.startswith(word):
            suffix = target[len(word):]
            result = all_construct(suffix, word_bank, memo)

    return ways


print(all_construct("purple", ["purp", "p", "ur", "le", "purpl"]))
print(all_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(all_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(all_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
print(
    all_construct(
        "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
        ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"],
    )
)
