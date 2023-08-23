from colored_edges import ColoredEdges, FormatChromosome
from two_break_on_genome_graph import TwoBreakOnGenomeGraph
from graph_to_genome import GraphToGenome

def TwoBreakOnGenome(genome: str, indices: list[int]) -> list[list[str]]:
    chromosomes = FormatChromosome(genome)
    graph = ColoredEdges(chromosomes)
    new_graph = TwoBreakOnGenomeGraph(graph, indices)
    return GraphToGenome(new_graph)

if __name__ == "__main__":
    genome_str = "(+1 -2 -4 +3)"
    indices_str = "1, 6, 3, 8"
    path = "./datasets/dataset_8224_3.txt"
    with open(path) as f:
        genome_str = f.readline().strip()
        indices_str = f.readline().strip()
    indices = list(map(lambda x: int(x), indices_str.split(", ")))
    result = TwoBreakOnGenome(genome_str, indices)
    result_str = ""
    for chromosome in result:
        result_str += "(" + " ".join(chromosome) + ")"
    with open('./results/two_break_on_genome.txt', 'w') as f:
        f.write(result_str)
