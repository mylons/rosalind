import bioutil

with open('dna.txt') as f:
    data = f.readlines()
    print(bioutil.hamming_distance(data[0].strip(), data[1].strip()))

