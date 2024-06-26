from random import randint
import sys
import os

sys.path.append(os.path.abspath("."))

from week_3.motif_profile import ProfileWithLaplace
from week_3.score import Score
from week_3.profile_most_probable_kmer import ProfileMostProbableKMer
from week_4.profile_randomly_generated_kmer import ProfileRandomlyGeneratedKmer

def _gibbs_sampler_cycle(dna_list, k, t, N):
    dna_length = len(dna_list[0])
    random_integers = [randint(0, dna_length-k) for i in range(t)]
    motifs = [dna_list[i][r:r+k] for i,r in enumerate(random_integers)]
    best_motifs = list(motifs)
    best_motifs_score = Score(best_motifs)
    for j in range(N):
        i = randint(0, t-1)
        profile = ProfileWithLaplace([motif for index,motif in enumerate(motifs) if index != i])
        motifs[i] = ProfileMostProbableKMer(profile, k, dna_list[i])
        motifs_score = Score(motifs)
        if motifs_score < best_motifs_score:
            best_motifs_score = motifs_score
            best_motifs = motifs
    return best_motifs_score, " ".join(best_motifs)

def gibbs_sampler(dna_list, k, t, N):
    best_motifs_score = k*t
    best_motifs = None
    for repeat in range(500):
        bms, bm = _gibbs_sampler_cycle(dna_list, k, t, N)
        if bms < best_motifs_score:
            best_motifs = bm
            best_motifs_score = bms

    return best_motifs, best_motifs_score
    

if __name__ == "__main__":
    dnas = [
        "GTCATTTGACGCATAGCGATAACTAGGTTGGCTTGCAGTGCAGATCCGAAGCTTTCCCTTAGCTCGGCGACTTTCTGTCTGGGCTTTCCTTGGTTAGCTCTATTTCTCGGTCGAGGTTCCCTTAGGGCTCTCTGCTCTAGCACTACTGACGCTATAGCTGGCCATGCATGAGTCCAGTCGGCCAATCTGCAGACCAACCTAATCGAATAAGAAAGCGTGCTACCAAGCAACCCCAAAGCTGGGAGGGGTGAGCGTCAAAACCGGGTCCTCAATGCTGTAACTCAAATCATCCCGTAGTTACTGAATGTCATTTGACGCATA",
        "GCGATAACTAGGTTGGCTTGCAGTGCAGATCCGAAGCTTTCCCTTAGCTCGGCGACTTTCTGTCTGGGCTTTCCTTGGTTAGCTCTATTTCTCGGTCGAGGTTCCCTTAGGGCTCTCTGCTCTAGCACTACTGACGCTATAGCTGGCCATGCATGAGTCCAGTCGGCCAATCTGCAGACCAACCTAATCGAATAAGAAAGCGTGCTACCAAGCAACCCCAAAGCTGGGAGGGGTGAGCGTCTCGCGCTTTGTTGTCAAAACCGGGTCCTCAATGCTGTAACTCAAATCATCCCGTAGTTACTGAATGTCATTTGACGCATA",
        "GTAAGAGCGTTCAAGCGAATAATCTGAGTTTAGGGGCCGTGATCTCCGATAGTGTACAGCCGAGACTTGAGAGATTTTAACAATAGGGTCTAGGATCATTAGGAAGAGTGTCATCGCATTTGTTATCGGGGCTAAGCTACATTGCGTCGATCTTAACTCAACACTCAAAATTTTGCTCAGTAAGAATTTAACTGTTAACCACGCGAGCATTCCAGCTTCCGAGCTCCCGAAGAAGTCCCCCCCACTAATCGTTCTCGGACCACCTAGCTGTGCCAGGACAATAGTCGATGGCGGAAAGCCTCCGAAGCGGGCCCAGACCTC",
        "CACGGCCCACTTGCGAGGTAGCCAATTCACCGACCAACAATCGACGGGTCCCCGCGAGGACTGGCGTCTATGAAGGAGCTTGTGACAATCCTCACGACTTGTACACGCCGGCCTCTGGGCGTTCGGTCTACTCCCCTGGGGCGGATAGCATGTCCGTGTGGACTGCGTGGTCGACGGGTTAGCGTCATGACCTTTGTTCCACCACAGGGGGCCGGTAACGTTGCTTCGTGTGCCAGACGACCCTTGGGAGGTTCGGGGGGTCCGTCAACGATCTGGAAATACAGGGCATCTACATAAACGTGACGCTCACTTCCTACTCCG",
        "CCTAACGCGACACTACTCATTCCACTCAATCCTAAACTAGCCCAATACGAATAATTTCGGAACCCTATGGTCTAATCGCTTATCCCTAGACCCCCCAGGAGGCCATCCGCGACTTGTGGTGGGCCGCTTTGTTTAGTGCACGACGGTGGCTGGTATAGTCTCGGGGCACGTTAAGGCGCCTACTCCCTCACATAAATAATAGTAGAATCAGTTTAACGGAAAGTAAATCCGTTGGTTGCCCGTGACCAGGTAGCGTTAATTCTACTATCTGATGCTTTATAACGTAGAGTTGTTACCGACCAGTAGAAAACTGTAACTAGA",
        "AGATATAGGCGATTAACGCCCCCGCCTTCTTAGCAGGGTAACCGTAGTTGCCAGACTCTCGCTGCGTTTGAGTTGCCCCGCCTAGAGGTGGGTCACGAGCTTTGTTCTAGTCGAATCCTAGATGCCGTGGCGGCGCACCCTGCTCTTATAAAGCTCCTGCAATCGGTTTGCGACCTGCTAGGATGGAGCTGTGTCCCAAAAAAGGAGCGGGAGAATCGCACTGCTCAACCTCCACACCAACAAACGTGTACGTGTCCGTCGTTCCTGTTTCAGATGGGAATTGGAATGAAGCGGACTTATCATACGTTCAATTATTCATCC",
        "CACCTACTGCAAGGTAAGTCGTCATCCAAGTTGTTGGCTATTCATTAGATCCGAGAGTGGTAAAACGACGAGGGCGTTACCAACCTTGTTTCATGTCCCTGAGAGCGTACATCAAGGCCATTGGACTGTTACAGTAACAGGTTGCGCTGAACCAGATAGCCGGTGTTATCTCATGCGACACTCTCTAGGTATCTCGCGGGGTCACGTACTCAGTTCCAGCAGATAGGCTGTCGTCAGAGTACAATCTCACTTCCAGATTCAGACGGCATGTGCGGAGACAAGAGCGCGACTACCCTCAGCCGTATACTCTGAGTATGTGGA",
        "TTTAGTACAAGGGCGTCGCAAGAAATGTGACAAGACATAGACAATCATCGCACTCCCCGTTACAATGCTCACGTAACACACCGTATATCTGTGTAATAGGTACAGAATACACATCACACTGGCCCCATATACACCCCGGCCTACAAAAGCTTGATGTGATTCTGCAGAGAAGAGCGGTTCATCCGCTTTGGAGAGTCACTTTCGGCGGTGACTGCTGGGTGGGAGGGAAGGGAGTGGGTTCGATGTTAAGTTCGCATATGCGCTGAAGAGGATTGCGTCAGTCATAGTAAGGCAGCTCGCCAGTATTATGCGGAAATGCCT",
        "GCGGCAAGACAAGGGCCACTGGAGACGTCGGAGTGAATCTTAAACTTACCGTATAGTGCACAAATTGGAAGGTCCAGCAGTAACCCCACCGGGCCGGTGCTTGACCAGCAGGGCGTAGTCTAGTGTGTCAACTTCCCGAGGAGTATGGAAAGTCCGACAGGCCAACAGGAGCGTTCGGTTACATTGGAAATCGGTCATCCGCTTCTCTGCTGTGATCCCGTTAACGTGACAGCACATCGACCCCCTTTCGACCGGCTCCCCATCAATCGGCGTGTTTCTTAAGGCCAACCGAGGTCGGGAGCCTCCATGCCTATGGCAGCA",
        "GTAAGTTGCGGACACTCCGTTCACACCCTTTCAACGACGCTTATATAAAATAGACTGTGAACTCATCGGAACTAGCAGAATGTCGCACGAACCGGCTGCGGCATCTCCTTTTTCGATTCCCAGTAGGCAGGCTGGCTTCCTCTCATAGCTATAAGCTGTACACTAAACCTGGGGCGAAACGGAACGTTGGTGTCTCAGTACGAAATTCCGAAAGCAGGTGTCATGTCATCCGCTGCATTAGTCGTTCGTGCGTTTGTGTTGGCCTAATGCATGCTGATGAGCCTCTTTGCGATTGGGTAACTACTAGGCACGCGATATGGC",
        "CCCTTCAAGTTCAGGCCGGTCCCGTGTGTCGGGCCCACCGCATATGCCCGATAGTAGTTCAACCGGTGAATTAATGAGGGACTCCGCTTTGTTAAATGCGTCAGAGCGCAAGGTTCGCACTTTCGTGTTAGGACCGCTTCTCCTCTATGCCGTTTCCGTAGATTTTCGGTAGCCTTTGTCGCACTGGTATCGGGCGAGCTGCGGGTGCAGAGTTCCCCGTCATGCGCGTTCGTATTTGGGGGTTCACAGGTCCGCTTACTAGGCGTGGAGCGACTTAGGGTAAAGTTATCTATGAGCGTGGGCCATAAAAGATTCATTGTT",
        "AGGGTCATCTAATTTGTTGAAACAATTCGTGACGGACGGCTTTCGCTGAGGGCCCACCATAGGTGCAAAACTCGCCAAGAGGAGCATGCTCTTGTGGTAAGTAGCGAAAGAGGTCTATTTTTTTAATGCTAATTACCTTGCTGCGTTGAACGCTTCGCCTCAGAGTCCCTATGATATCATAATGTGGGTCACCCTTCGGGGACGTATTATCGGTATTTGAACTGCCCTGCATACCCCTGGCCCGGCAGCCCTTAACAAGAGGTACCATGGATAATACTTGTTAGATTTAAGCGTTACTGCAAAGCAAAAAACCCGCAACAC",
        "GACGACGTGCGTTTTTGCCGTTCGGCTGTGATCTCTTCCATCGTGTCACAGGCTTTGTTCCAACGAATGCGGGGGTAGGATCACAATACTAAGGTCAATTTATAGACGCCATTGAAAAGGACGATTAACAGTAGAGGACCAGCCCATGTCGCTCGGGTCGCGCCATAAGTCTGCCTCGAAAGAGTGCGAGACCCGAAGAGACATGACCCAATCTTGCTCGACCGGCGGTGTTTGTGCCCTGACAACGCCCTGCGAATCGGCCGGTATTCGATTCTATTACCTGAGATAGACAGGACCAGCGTAGTCTACCTGTCATATGCG",
        "GTTCACCTAATCGGCCACCATTTTAAGGCTTCACTTTTATAGACGCCTCTCTGGTCGGTGCCGCAGCAGCTGGGGCTACGTTCCTACGCCTGGACCATCCCTTTCAGCGCGGGTCTTAGGTTATGCCATGTAGGTCAGGTACGCATCCGCTTTGTACCCTATAATCCGATCCCCAATGCGAATGTTGAATTAGCTTCAGAAGGTGTCATGTGCGTGGTTGTGTTTTAACTCTGACATAAGGAGTTACGTTGTGGATGTCCCAATAAGAAAAGCGTCGACGGCCAGACGGCAAGTGCTAGCCTCGTTCCCGCGGAGCAGCTT",
        "TTTTAGACCACTGAGGGACCAACCCTACAAGTCCGTCATGGAATTGCCTAGGGCTTAGCGTGGAGGGGTATGCTCCGAGAGAATCGCAGCCCCTGAACTATTTTCCTTTACCCAGTATCCGCTTTGTTCTCAAAATTAAACTTTTGAGTGGCTTTTTAGACGAACGGCGACACTCGTAGCCTTCAGAATGGCAGCCACGGGTGACCGGGGAGGTTGTAGCTCGACACCCCCTTTCTCTGGTGTGAACTGACCCTTAATTACGCGCCTGGCGATTTTCATAGGGGTGTTGTGATCGCCACGGTAGGGCGCCTGCTTTGCTTA",
        "CCTCTCAGAAGTTTTTTTAATCCAAGTGCTGGAGTCTCTCCATAGCGTTTGACGTCGTGATGGTACGAGTTGAACATGCCATTATCAGCGTGCAACGTATTCCATTACGAGCGCGCTCGCCAAGAGTAAGCTCTGCGAGCGAGCATAGTACTCGCGTGAGTCATCCGCTTTAGGGGCTCGGAACCGAGATCGGACTTGTGGAGTCGGCCGGCCCCTACCGTTAGTCCGAGTTGGGAGAGTCTGTATAGTAGCGCGATACGACGTATCCATTTGCGATGGCATTAGATAAAACCTTTGCCATGACTAGAGCAGCTCTTTAGC",
        "GCGGTTATATAGCACGCTTCTTAATGAAGATGTTCCGGGTCGTTGTCTACGGATGCTACTCCGATTACTCAATCATAAACGGATGATGTTAGTGCACGTCATCCGTGCTGTTTTTCGAACACAATACGGATACAGCCCATGATGTGATGCCAAAGTAACTCTGCCAGATTGGGGTACGATCCACCTCGTTATCTGGACATTATGTTCGGCAACTTAACCTATGTTTCCGACTGTCGGCCGGCCTGTGGTGACCACTCTAGGTCACGCTGCCAGGGCCTAATCGTAAAACTGGCTGGTGATAGGTACGATTGGAGCTCGTTT",
        "GTATAAATAAATCTCCTGCTACCCTCCCTGGCGGGTTCTAAGTAACTATAGTGACAGGATTAAGGTAGTTGATTGGATACCTCTCATGCACATACTCAGTTAGGTCATCCGCGGCGTTCTAATCGTCTATAATTGGTAATGTCCTAATACAATCACAAGGTTCGCCAGTCCACGGGCGCTTGCTGTTATTTCCCTCGTCCCTTGGTATCTGTTGGCAAGCCAACACATACTTTTCAGGGACAGACCTTAACGCAACTCCTAACGCGAGGGAAAGCTCTCGTGACGCGAGGTAGGCGATGCTTATATACCAGTTTTAGCAGT",
        "CGTCCCATCAAACGCAGGCTCTGACGTTCACTGTTCGAAGGGTCTATCCCGCTGAACCTGTGGATGTACCAGATCTTCGTCACACCCGTCGTGGCCACCTCTCGGTAAGTGACGACGCTTCTGAACACATCCAGATAAGCTATGTGTCGTTATCTTATATTGCCTTTTAAAAACCTCTCTCGTAATGTTGTCTCGGCCCGGAGGTGACTCCATGGAAAGCGCCTTATAGACGGCAGGAGCTTATGGTGGCTGTCTGTCGCTTTGTTATTTATGGGACATCGAAGTGCTTGTCCGGGCTCATCGACCAGGTTTGTTAGTAAG",
        "GGTCGTACGTACATGGGGGATATGAGTCGTACCATTCCCTGGCGCACGGCCACCACATTGATCAATGGAGCACACACCTCAGGGCGCTGGTCGCATTAGGCATACCCTAAGTTGAGGGGTTAGTTCAACTGACCTGTGCAGGAAATGCTTTCAAACTGTCTTAGTTGACGTTTGTTTAGTTTAGTTCAGCAAGAGTGGCTATCAACACTTGTCACTGTATTGCTCCGGGAGGGTCATTTCCTTTGTTGCTGCCTTTCCCCGAGCATCTTGACTACCTCCCCGCGTAATCAGAGTTCAATGGACAAAGATGGATCAAGCACA"
    ]

    print(gibbs_sampler(dnas, 15, 20, 100))