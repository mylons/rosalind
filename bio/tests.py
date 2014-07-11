__author__ = 'mylons'
from unittest import TestCase
import bioutil


class BioUtilTests(TestCase):

    def setUp(self):
        self.dna = 'GATGGAACTTGACTACGTAAATT'
        self.rna = 'GAUGGAACUUGACUACGUAAAUU'

    def test_dna_to_rna(self):
        self.assertEqual(bioutil.dna_to_rna(self.dna), self.rna)

    def test_reverse_complement(self):
        dna = 'AAAACCCGGT'
        comp = 'ACCGGGTTTT'
        self.assertEqual(bioutil.reverse_complement(dna), comp)

    def test_gc


# TODO fasta.FastaReader tests
