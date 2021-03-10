"""
스택을 활용한 DFS
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


def dfs_stack(adjacent_graph, start_node):
    # 개선 전
    #stack = []
    #visited = [start_node]
    #adj_nodes = adjacent_graph[start_node]
    #stack += adj_nodes
    #while stack:
    #    cur_node = stack.pop()
    #    adj_nodes = adjacent_graph[cur_node]
    #    visited.append(cur_node)
    #    for adj_node in adj_nodes:
    #        if adj_node not in visited:
    #            stack.append(adj_node)
    #return visited

    # 개선 후
    stack = [start_node]
    visited = []

    while stack:
        current_node = stack.pop()
        visited.append(current_node)
        adj_nodes = adjacent_graph[current_node]
        for adj_node in adj_nodes:
            if adj_node not in visited:
                stack.append(adj_node)
    return visited


print(dfs_stack(graph, 1))  # 시작노드 1
# [1, 9, 10, 5, 8, 6, 7, 2, 3, 4] 이 출력돼야 함
