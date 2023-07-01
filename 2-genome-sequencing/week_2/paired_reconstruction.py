import sys
import os

sys.path.append(os.path.abspath(".."))

from week_1.genome_path import GenomePath

from de_bruijn_paired_kmers import DeBruijnPairedKmers
from eulerian_path import EulerianPath
from paired_genome_path import PairedGenomePath

def PairedReconstruction(pairs, n, d):
    graph = DeBruijnPairedKmers(pairs)
    path = EulerianPath(graph)
    return PairedGenomePath(path, n, d)

if __name__ == "__main__":
    pair_length = 0
    divider = 0
    pairs = []
    
    with open('./datasets/dataset_204_16.txt') as f:
        params = f.readline().strip().split(" ")
        pair_length = int(params[0])
        divider = int(params[1])
        for line in f:
            pairs.append(line.strip().split("|"))

    a = PairedReconstruction(pairs, pair_length, divider)
    with open('./results/paired_reconstruction.txt', 'w') as f:
        f.write(PairedReconstruction(pairs, pair_length, divider))