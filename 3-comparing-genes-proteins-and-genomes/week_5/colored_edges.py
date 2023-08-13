from chromose_to_cycle import ChromosomeToCycle

def ColoredEdges(chromosomes: list[list[str]]) -> list[tuple[int]]:
    edges: list[tuple[int]] = []
    for chromosome in chromosomes:
        cycle = ChromosomeToCycle(chromosome)
        cycle = cycle[1:] + cycle[:1]
        for i in range(0, len(cycle), 2):
            edges.append((cycle[i], cycle[i+1]))

    return edges

def FormatChromosome(chromosome_str: str) -> list[list[str]]:
    chromosome_str = chromosome_str[1:-1].split(")(")
    return  list(map(lambda chro: chro.split(" "), chromosome_str))

if __name__ == "__main__":
    chromosomes = "(+1 -2 -3 -4)"
    path = "./datasets/dataset_8222_7.txt"
    with open(path) as f:
        chromosomes = f.readline().strip()
    chromosomes = FormatChromosome(chromosomes)
    result = ColoredEdges(chromosomes)
    with open('./results/colored_edges.txt', 'w') as f:
        f.write(str(result)[1:-1])