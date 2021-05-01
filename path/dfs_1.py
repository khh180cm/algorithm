"""
깊이 우선 탐색
"""

arr = [i for i in range(9)]

adj_nodes_info = {
    0: [1, 2, 3],
    1: [0, 4],
    2: [0],
    3: [0, 6],
    4: [1, 5],
    5: [4, 6, 7, 8],
    6: [3, 5],
    7: [5, 8],
    8: [5, 7],
}

# 방문 노드 저장
visited = []


def dfs(node):
    # 노드 값 검증
    assert type(node) == int and node >= 0,\
        'Value must be greater than 0 with integer number'
    # 기저 조건
    if node in visited:
        return
    else:
        visited.append(node)
        adj_nodes = adj_nodes_info[node]
        for i in adj_nodes:
            dfs(i)


print(visited)
dfs(0)
print(visited)
