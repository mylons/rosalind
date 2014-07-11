import bioutil
import fasta
from operator import attrgetter
from collections import namedtuple

FastaGC = namedtuple('FastaGC', ['id', 'data', 'gc'])

fr = fasta.FastaReader('rosalind_gc.txt')

the_list = ((FastaGC(fasta.id, fasta.data, bioutil.gc_content(fasta.data)) for fasta in fr))
the_max = max(the_list, key=attrgetter('gc'))
print("{}\n{}".format(the_max.id, format(100 * the_max.gc, '0.6f')))



