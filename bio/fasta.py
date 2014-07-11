from collections import namedtuple


Fasta = namedtuple('Fasta', ['id', 'data'])


class FastaReader:
    """
    this class is only going to work for rosalind
    type data i think -- they provide weird fasta's
    """
    def __init__(self, file_name):
        self._fn = file_name

    def _make_fasta(self, fasta):
        tmp = fasta.split()
        return Fasta(id=tmp[0],
                     data=''.join(tmp[1:]).replace('\n', ''))

    def __iter__(self):
        with open(self._fn) as f:
            lines = f.read().split('>')[1:]
            for line in lines:
                yield self._make_fasta(line)



