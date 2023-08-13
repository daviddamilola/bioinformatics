from cycle_to_chromosome import CycleToChromosome

def GraphToGenome(graph: list[tuple[int]]) -> list[list[str]]:
    chromosomes: list[list[str]] = []
    current_chromosome = []
    for pair in graph:
        if pair[1] < pair[0]:
            current_chromosome = [pair[1]] + current_chromosome + [pair[0]]
            cycle = CycleToChromosome(current_chromosome)
            chromosomes.append(cycle)
            current_chromosome = []
        else:
            current_chromosome += pair
    return chromosomes


if __name__ == "__main__":
    graph_str ="(2, 4), (3, 6), (5, 1), (7, 9), (10, 12), (11, 8)"

    path = "./datasets/dataset_8222_8.txt"
    with open(path) as f:
        graph_str = f.readline().strip()
    graph_str = graph_str[:-1].split("), ")
    graph = []
    for pair in graph_str:
        pairs = pair[1:].split(", ")
        first, second = int(pairs[0]), int(pairs[1])
        graph.append((first, second))
    result = GraphToGenome(graph)
    result_str = ""
    for chromosome in result:
        result_str += "(" + " ".join(chromosome) + ")"
    with open('./results/graph_to_genome.txt', 'w') as f:
        f.write(result_str)