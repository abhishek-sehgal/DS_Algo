from collections import deque


def bfs(graph, vertex):
    queue = deque([vertex])
    level = {vertex: 0}
    parent = {vertex: None}
    while queue:
        v = queue.popleft()
        for n in graph[v]:
            if n not in level:
                print(f"Visiting {n}")
                queue.append(n)
                level[n] = level[v] + 1
                parent[n] = v

    return level, parent

def dfs(graph, vertex):
    stack = [vertex]
    level = {vertex: 0}
    parent = {vertex: None}
    while stack:
        v = stack.pop()
        for n in graph[v]:
            if n not in level:
                print(f"Visiting {n}")
                stack.append(n)
                level[n] = level[v] + 1
                parent[n] = v

    return level, parent

if __name__ == "__main__":
    graph = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "D"],
        "D": ["B", "C", "E"],
        "E": ["B", "D"],
    }

    print(bfs(graph, "A"))
    print(dfs(graph, "A"))
