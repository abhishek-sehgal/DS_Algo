# Breadth First Traversal of a graph
def breadth_first_print(graph, node):
    queue = [node]
    while len(queue):
        current = queue.pop(0)
        print(current, end=",")
        for neighbor in graph[current]:
            queue.append(neighbor)


graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": [],
}

breadth_first_print(graph, "a")  # abcdef
print("\n")
