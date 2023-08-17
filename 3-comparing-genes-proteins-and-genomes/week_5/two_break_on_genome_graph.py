from graph_to_genome import FormatGraph

def TwoBreakOnGenomeGraph(graph: list[tuple[int]], indices: list[int]) -> list[tuple[int]]:
    first_index = -1
    second_index = -1
    first_index_val = indices[0]
    second_index_val = indices[2]

    for i in range(len(graph)):
        edge = graph[i]
        if first_index_val in edge:
            first_index = i
        if second_index_val in edge:
            second_index = i
        if first_index > -1 and second_index > -1:
            break

    graph[first_index] = (indices[0], indices[2]) if graph[first_index][0] == first_index_val else (indices[1], indices[3])
    graph[second_index] = (indices[1], indices[3]) if graph[first_index][0] == indices[0] else (indices[0], indices[2])
    return graph


if __name__ == "__main__":
    graph_str = "(2, 4), (3, 8), (7, 5), (6, 1)"
    indices_str = "1, 6, 3, 8"
    path = "./datasets/dataset_8224_2.txt"
    with open(path) as f:
        graph_str = f.readline().strip()
        indices_str = f.readline().strip()
    graph = FormatGraph(graph_str)
    indices = list(map(lambda x: int(x), indices_str.split(", ")))
    result = TwoBreakOnGenomeGraph(graph, indices)
    with open('./results/two_break_on_genome_graph.txt', 'w') as f:
        f.write(str(result)[1:-1])
