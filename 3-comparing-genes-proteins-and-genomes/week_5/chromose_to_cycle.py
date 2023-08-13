def ChromosomeToCycle(chromosome: list[str]) -> list[int]:
    cycle = []
    for valStr in chromosome:
        val = int(valStr)
        postiveVal = abs(val)
        if val > 0:
            cycle.extend([2*postiveVal-1, 2*postiveVal])
        else:
            cycle.extend([2*postiveVal, 2*postiveVal-1])
    return cycle


if __name__ == "__main__":
    chromosomes = "+1 -2 -3 +4"
    path = "./datasets/dataset_8222_4.txt"
    with open(path) as f:
        chromosomes = f.readline().strip()[1:-1]
    chromosomes = chromosomes.split(" ")
    result = ChromosomeToCycle(chromosomes)
    print(result)
    with open('./results/chomosome_to_cycle.txt', 'w') as f:
        f.write("(" + " ".join(map(lambda x: str(x), result)) + ")")