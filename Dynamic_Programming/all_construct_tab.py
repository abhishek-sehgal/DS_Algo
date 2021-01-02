def all_construct(target, word_bank):
    table = [[] for _ in range(len(target) + 1)]
    table[0] = [[]]
    for i in range(len(target) + 1):
        for word in word_bank:
            if target[i : i + len(word)] == word:
                new_combination = list(map(lambda x: [*x, word], table[i]))                
                table[i+len(word)].extend([*new_combination])
    return table[len(target)]


print(all_construct("purple", ["purp", "p", "ur", "le", "purpl"]))
print(all_construct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))
print(all_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(
    all_construct("aaaaaaaaaaaaz", ["a", "aa", "aaa", "aaaa", "aaaaa"])
)  # If we remove the z, it becomes the worst case scenario
