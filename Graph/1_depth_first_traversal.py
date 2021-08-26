# Depth First Traversal of a graph
def depth_first_print(graph, node):
    stack = [node]
    while len(stack):
        current = stack.pop(-1)
        print(current, end=",")
        for neighbor in graph[current]:
            stack.append(neighbor)


def depth_first_print_rec(graph, node):
    print(node, end=",")
    for neighbor in graph[node]:
        depth_first_print_rec(graph, neighbor)


graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": [],
}

depth_first_print(graph, "a")  # acebdf
print("\n")
depth_first_print_rec(graph, "a")  # abdfce
print("\n")
