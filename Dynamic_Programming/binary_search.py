import random

# Recursive rendition of the popular search algorithm
def bin_search(vec, x):
    if len(vec) == 1:
        return x == vec[0]
    mid = len(vec) // 2
    if vec[mid] == x:
        return True
    elif vec[mid] < x:
        return bin_search(vec[mid + 1 :], x)
    else:
        return bin_search(vec[:mid], x)


vec = [random.randint(0, 100) for _ in range(20)]
vec = sorted(vec)
print(vec)
print("Is 20 in the array: ", bin_search(vec, 20))
print(bin_search(vec, vec[0]))
print(bin_search(vec, vec[-1]))
