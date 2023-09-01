import sys

def SharedKMers(genome1: str, genome2: str, k: int) -> list[tuple[int]]:
    result: list[tuple[int]] = []
    genome1_map: dict[str, list[int]] = dict()
    for i in range(len(genome1) - k+1):
        kmer = genome1[i: i+k]
        reverse_kmer = reverse_complement(kmer)
        if genome1_map.get(kmer) == None:
            genome1_map[kmer] = []
        if genome1_map.get(reverse_kmer) == None:
            genome1_map[reverse_kmer] = []
        genome1_map[kmer].append(i)
        genome1_map[reverse_kmer].append(i)

    for i in range(len(genome2) - k+1):
        kmer = genome2[i:i+k]
        matches = genome1_map.get(kmer)
        if not matches:
            continue
        for match in matches:
            result.append((match, i))
    return result

def reverse_complement(kmer: str) -> str:
    a = {'A':'T', 'T':'A', 'C': 'G', 'G': 'C'}
    rc_k = ""
    for i in kmer:
        rc_k += a[i]
    return rc_k[::-1]

def run_virus():
    e_coli_path = "./datasets/rearrangements_E_coli.txt"
    s_enterica_path = "./datasets/rearrangements_Salmonella_enterica.txt"
    genome1 = ""
    genome2 = ""
    k = 30
    with open(s_enterica_path) as f:
        genome1 = f.read().strip()
    with open(e_coli_path) as f:
        genome2 = f.read().strip()
    
    result = SharedKMers(genome1, genome2, k)
    print(len(result))

if __name__ == "__main__":
    if sys.argv[1] == "-v":
        run_virus()
        exit()
    genome1 = "AGAT"
    genome2 = "AATC"
    k = 3
    path = "./datasets/dataset_289_5.txt"
    with open(path) as f:
        k = int(f.readline().strip())
        genome1 = f.readline().strip()
        genome2 = f.readline().strip()
    result = SharedKMers(genome1, genome2, k)
    result_str = "\n".join(map(lambda i: str(i), result))
    with open('./results/shared_kmers.txt', 'w') as f:
        f.write(result_str)
