def CycleToChromosome(cycle: list[int]) -> list[int]:
    chromosome = []
    for index in range(0, len(cycle), 2):
        val = cycle[index]
        cycleNo = int((index / 2) + 1)
        chromosome.append("-"+str(cycleNo)) if val % 2 == 0 else chromosome.append("+"+str(cycleNo))
    return chromosome


if __name__ == "__main__":
    cycle = "1 2 4 3 6 5 7 8"
    cycle = cycle.split(" ")
    path = "./datasets/dataset_8222_5.txt"
    with open(path) as f:
        p_str = f.readline().strip()[1:-1]
        cycle = p_str.split(" ")
    cycle = list(map(lambda x: int(x), cycle))
    result = CycleToChromosome(cycle)
    print(result)
    with open('./results/cycle_to_chomosome.txt', 'w') as f:
        f.write("(" + " ".join(result) + ")")