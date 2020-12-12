def all_construct(target, word_bank, memo=None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    if target == "":
        return [[]]

    result = []

    for word in word_bank:
        if target.startswith(word):
            suffix = target[len(word) :]
            suffix_ways = all_construct(suffix, word_bank, memo)
            target_ways = list(map(lambda x: [word, *x], suffix_ways))
            result.extend(target_ways)

    # Comment this line for brute force
    memo[target] = result
    return result


print(all_construct("purple", ["purp", "p", "ur", "le", "purpl"]))
print(all_construct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))
print(all_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(all_construct("aaaaaaaaaaaaaaaaaaaaaaaaaaz", ["a", "aa", "aaa", "aaaa", "aaaaa"])) # If we remove the z, it becomes the worst case scenario
