"""
인접 리스트 방식 DFS
"""


graph = {
    1: [2, 5, 9],
    2: [1, 3],
    3: [2, 4],
    4: [3],
    5: [1, 6, 8],
    6: [5, 7],
    7: [6],
    8: [5],
    9: [1, 10],
    10: [9]
}
visited = []


def dfs_recursion(adjacent_graph, cur_node, visited_array):
    visited_array.append(cur_node)
    for adj_node in adjacent_graph[cur_node]:
        if adj_node not in visited_array:
            dfs_recursion(adjacent_graph, adj_node, visited_array)
#    cur_adj_nodes = adjacent_graph[cur_node]
#    while cur_node not in visited:
#        visited.append(cur_node)
#        for i in range(len(cur_adj_nodes)):
#            cur_node = cur_adj_nodes[i]
#            dfs_recursion(adjacent_graph, cur_node, visited)


dfs_recursion(graph, 1, visited)
print(visited)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 이 출력되어야 합니다!