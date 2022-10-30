from collections import deque
from graphs import graph_firstTask, graph_secTask
import threading
import time

def bfs(graph_to_search, start, end):
    queue = [[start]] # Створюємо чергу вершин
    print(queue)
    visited = set() # Створюємо список пройдених вершин на базі сету

    while queue:
        # Отримуємо перший елемент черги, список
        path = queue.pop(0)
        print(path)

        # Отримуємо останній елемент списку
        vertex = path[-1]
        print(vertex)

        # Перевіряємо і повертаємо шлях у разі успіху
        if vertex == end:
            return path
        # Перевіряємо чи не пройдений вже елемент
        elif vertex not in visited:
            # отримуємо нові вершини і додаємо до черги
            for current_neighbour in graph_to_search.get(vertex, []):
                print(current_neighbour)
                new_path = list(path)
                print(new_path)
                new_path.append(current_neighbour)
                queue.append(new_path)
                print(f'queue {queue}')

            # Додаємо до відвіданого
            visited.add(vertex)


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


def bfs_bid(start, graph, search_queue, visited, end, middle_list: list):
    search_queue += graph[start]
    while search_queue:
        # print(f'Search queue {search_queue}')
        node = search_queue.popleft()
        # print(f'Get node {node}')
        k = 0
        if not node in visited:
            # Перевірямо середні вершини, у разі пройдення зупиняємо
            for i in middle_list:
                if node == i:
                    k += 1
                    print(f'{threading.current_thread()} ,Middle tree {node}')
                    if k == 2:
                        return

            else:
                search_queue += graph[node]
                visited += [node]


# Двонаправлений пошук
def bidirectional_search_bfs_based(startPoint, endPoint, graph, middle_list: list):
    # Створюємо черги
    searchQueue_direct = deque()
    searchQueue_backward = deque()
    visited_dir = []
    visited_back = []

    # Створюємо потоки для кожного направлення
    thread_dir = threading.Thread(target=bfs_bid,
                                  args=(startPoint, graph, searchQueue_direct, visited_dir, endPoint, middle_list,))
    thread_back = threading.Thread(target=bfs_bid,
                                   args=(endPoint, graph, searchQueue_backward, visited_back, startPoint, middle_list,))
    # Запускаємо потоки
    thread_dir.start()
    thread_back.start()

    # Перевіряємо списки на середні вершини
    while True:
        time.sleep(1)
        for i in middle_list:
            if i in visited_dir and i in visited_back:
                print("Done")
                return



if(__name__ == "__main__"):
    dfs('1', '13', graph_firstTask, [], set()) #deapth scan
    # bfs('A', 'Z', graph_secTask) # breadth scan
    # print(another(graph_secTask, 'A', 'Z'))
    # bidirectional_search_bfs_based('A', 'K', graph2, ['G', 'E']) #bidirectional scan

