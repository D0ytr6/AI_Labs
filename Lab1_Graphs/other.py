from collections import deque


# Breadth first search
def bfs(startPoint, searchPoint, graph):
    searchQueue = deque()
    visited = []
    searchQueue += graph[startPoint]
    way = searchPoint

    while searchQueue:
        # print(f'Search queue {searchQueue}')
        node = searchQueue.popleft()
        print(f'Get node {node}')
        if not node in visited:
            if node == searchPoint:
                print(f'Found {node}')
                return True
            else:
                searchQueue += graph[node]
                visited += [node]

    print("Not Found")
    return False

# Recursive searching in deap
def dfs(startPoint, searchPoint, graph, visited: list, way: set):

    # Перевіряємо вершини на рівність
    if startPoint == searchPoint:
        print(f'Find node {startPoint}')
        # print(f'Current way {way}')
        return True

    if startPoint in visited:
        return False

    # додаємо до відвіданого
    visited.append(startPoint)
    # Проходим по вершинам
    for node in graph[startPoint]:
        print(node)
        way.add(node)
        if not node in visited:
            # Рекурсивний запуск функції з іншими стартовим параметром
            if dfs(node, searchPoint, graph, visited, way):
                return True

    return False