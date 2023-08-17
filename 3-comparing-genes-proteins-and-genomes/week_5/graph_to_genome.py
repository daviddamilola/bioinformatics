from cycle_to_chromosome import CycleToChromosome

def GraphToGenome(graph: list[tuple[int]]) -> list[list[str]]:
    unused_edges: dict[int, int] = dict()
    chromosomes: list[list[str]] = []
    current_cycle = []
    for edge in graph[1:]:
        unused_edges[edge[0]] = edge
        unused_edges[edge[1]] = (edge[1], edge[0])
    
    current_edge = graph[0]
    current_cycle += current_edge
    while len(unused_edges) > 0:
        last_val = current_edge[1]
        # next val is last val - 1 if last val is even else last_val + 1
        # eg For (2, 5) next should have a 6 while for (2, 6) next should have a 5
        next_val = last_val - 1 if last_val % 2 == 0 else last_val + 1
        next_edge = unused_edges.get(next_val)
        if not next_edge:
            current_cycle = [current_cycle[-1]] + current_cycle[:-1]
            chromosomes.append(CycleToChromosome(current_cycle))
            current_cycle = []
            next_edge = list(unused_edges.values())[0]
        unused_edges.pop(next_edge[0])
        unused_edges.pop(next_edge[1])
        current_edge = next_edge
        current_cycle += current_edge
    if len(current_cycle) > 0:
        current_cycle = [current_cycle[-1]] + current_cycle[:-1]
        chromosomes.append(CycleToChromosome(current_cycle))
    return chromosomes


def FormatGraph(graph_str: str) -> list[tuple[int]]:
    graph_str = graph_str[:-1].split("), ")
    graph: list[tuple[int]] = []
    for pair in graph_str:
        pairs = pair[1:].split(", ")
        first, second = int(pairs[0]), int(pairs[1])
        graph.append((first, second))
    return graph

if __name__ == "__main__":
    graph_str ="(2, 4), (3, 6), (5, 1), (7, 9), (10, 12), (11, 8)"

    path = "./datasets/dataset_8222_8.txt"
    with open(path) as f:
        graph_str = f.readline().strip()
    graph = FormatGraph(graph_str)
    result = GraphToGenome(graph)
    result_str = ""
    for chromosome in result:
        result_str += "(" + " ".join(chromosome) + ")"
    with open('./results/graph_to_genome.txt', 'w') as f:
        f.write(result_str)