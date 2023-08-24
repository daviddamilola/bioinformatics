from two_break_distance import Blocks, Cycles
# from two_break_on_genome_graph import TwoBreakOnGenomeGraph
from two_break_on_genome import TwoBreakOnGenome
from graph_to_genome import GraphToGenome, FormatGenome
from colored_edges import FormatChromosome, ColoredEdges

def TwoBreakSorting(genome_a: str, genome_b: str) -> list[str]:
    genome_sequence: list[str] = [genome_a]
    block_length = len(Blocks(genome_a))
    cycles = Cycles(genome_a, genome_b)
    cycle_length = len(cycles)
    current_chromosome = genome_a
    while cycle_length < block_length:
        non_trivial_cycle = NextNonTrivalCycle(cycles)
        if not non_trivial_cycle:
            raise "Non trivial cycle found and block length not attained"
        indices = list(non_trivial_cycle[0] + non_trivial_cycle[1])
        chromosome = TwoBreakOnGenome(current_chromosome, indices)
        chromosome_str = FormatGenome(chromosome)
        new_cycles = Cycles(chromosome_str, genome_b)
        if len(new_cycles) > cycle_length:
            cycle_length = len(new_cycles)
            cycles = new_cycles
            current_chromosome = chromosome_str
            genome_sequence.append(chromosome_str)
        else:
            x = indices[2]
            indices[2] = indices[3]
            indices[3] = x
            chromosome = TwoBreakOnGenome(current_chromosome, indices)
            chromosome_str = FormatGenome(chromosome)
            new_cycles = Cycles(chromosome_str, genome_b)
            if len(new_cycles) > cycle_length:
                cycle_length = len(new_cycles)
                cycles = new_cycles
                current_chromosome = chromosome_str
                genome_sequence.append(chromosome_str)
            else:
                raise "No indices gave a lower cycle count"
    return genome_sequence

def NextNonTrivalCycle(cycles: list[list[int]]) -> list[int]:
    for cycle in cycles:
        if len(cycle) > 1:
            return cycle
    return None

if __name__ == "__main__":
    genome_a = "(+9 -8 +12 +7 +1 -14 +13 +3 -5 -11 +6 -2 +10 -4)"
    genome_b = "(-11 +8 -10 -2 +3 +4 +13 +6 +12 +9 +5 +7 -14 -1)"
    path = "./datasets/dataset_288_5.txt"
    with open(path) as f:
        genome_a = f.readline().strip()
        genome_b = f.readline().strip()
    result = TwoBreakSorting(genome_a, genome_b)
    with open('./results/two_break_sorting.txt', 'w') as f:
        f.write("\n".join(result))

# Sample Input:

# (+1 -2 -4 +3)
# 1, 6, 3, 8
# Sample Output:

# (+1 -2)(-3 +4)


