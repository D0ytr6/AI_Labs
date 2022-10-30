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
