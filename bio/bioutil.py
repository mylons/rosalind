"""
Functions that solve the rosalind problems. Trying to write them in
generic enough ways that I may be able to use them in later problems,
if that's even possible
"""

COMPLEMENTS = {'A': 'T',
               'T': 'A',
               'G': 'C',
               'C': 'G'}


def dna_to_rna(dna):
    # replace T with U
    return dna.replace('T', 'U')


def count_nucs(dna):
    return {'A': dna.count('A'),
            'C': dna.count('C'),
            'G': dna.count('G'),
            'T': dna.count('T')}


def reverse_complement(dna):
    return ''.join([COMPLEMENTS[nuc] for nuc in dna][::-1])


def gc_content(dna):
    return (dna.count('G') + dna.count('C')) / float(len(dna))


def hamming_distance(dna1, dna2):
    # assumes equal length
    return sum(1 for a, b in zip(dna1, dna2) if a != b)




