"""
큐를 활용한 BFS
"""


graph = {
    1: [2, 3, 4],
    2: [1, 5],
    3: [1, 6, 7],
    4: [1, 8],
    5: [2, 9],
    6: [3, 10],
    7: [3],
    8: [4],
    9: [5],
    10: [6]
}


def bfs_queue(adj_graph, start_node):
    need_to_visit = [start_node]
    visited = []
    while need_to_visit:
        cur_node = need_to_visit.pop(0)
        visited.append(cur_node)
        adj_nodes = adj_graph[cur_node]
        for adj_node in adj_nodes:
            if adj_node not in visited:
                need_to_visit.append(adj_node)
    return visited


print(bfs_queue(graph, 1))  # 시작노드 1
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 이 출력되어야 합니다!
