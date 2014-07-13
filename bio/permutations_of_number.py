from itertools import permutations

def all_permutations(num):
    """
    written to solve http://rosalind.info/problems/perm/

    permutation is defined as {1, 2.. num}
    therefore must +1 in the range to get that behavior

    :param num:
    :return: generator for permuations
    """
    return (p for p in permutations(range(1, num+1)))

with open('number.txt') as f:
    num = int(f.read().strip())
    permutations = [p for p in all_permutations(num)]
    print(len(permutations))
    for perm in permutations:
        print(str(perm).replace('(', '').replace(')', '').replace(',', ''))


