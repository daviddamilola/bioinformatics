import math

def countNodes(adj_list: list[tuple[int]]) -> int:
    """
    Given an adjacency list, returns the number of nodes in the graph.
    """
    nodes = set()
    for (in_, out_, length) in adj_list:
        nodes.add(in_)
        nodes.add(out_)
    return len(nodes)

def DistanceBetweenTrees(n: int, adj_list: list[tuple[int]]):
    num_nodes = countNodes(adj_list)
    matrix = [[math.inf] * num_nodes for _ in range(num_nodes)]
    graph = createGraph(adj_list)
    for i in range(num_nodes):
        for j in range(num_nodes):
            if i == j:
                matrix[i][j] = 0
            elif j in graph[i]:
                matrix[i][j] = graph[i][j]
    for k in range(num_nodes):
        for i in range(num_nodes):
            for j in range(num_nodes):
                sum_around = matrix[i][k] + matrix[j][k]
                if matrix[i][j] > sum_around:
                    matrix[i][j] = sum_around

    matrix = matrix[:n]
    matrix = [row[:n] for row in matrix]
    return matrix


def createGraph(adj_list: list[tuple[int]]) -> dict[int, dict[int, int]]:
    """
    Given an adj list e.g.
    ```
    3->5:7
    4->0:11
    4->1:2
    ```
    __Returns__
    ```js
    {
        3: {5: 7},
        4: {0: 11, 1: 2}
    }
    ```
    """
    result: dict[int, dict[int, int]] = dict()
    for (in_, out_, length) in adj_list:
        if not in_ in result:
            result[in_] = dict()
        result[in_][out_] = length
    
    return result


if __name__ == "__main__":
    import os
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = dir_path + "/datasets/dataset_30284_12.txt"

    n = 0
    adj_list: list[tuple[int]] = []
    with open(file_path) as f:
        n = int(f.readline().strip())
        for line in f:
            in_, out_result = line.split("->")
            out_, result = out_result.split(":")
            adj_list.append((
                int(in_.strip()),
                int(out_.strip()),
                int(result.strip()),
            ))
            
    matrix = DistanceBetweenTrees(n, adj_list)
    result_path = dir_path + "/results/distance_between_nodes.txt"
    matrix_str = ""
    for row in matrix:
        matrix_str += " ".join([str(val) for val in row]) +'\n'
    print("Matrix str\n" + matrix_str)
    with open(result_path, 'w') as f:
        f.write(matrix_str)

