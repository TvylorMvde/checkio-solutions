from itertools import permutations


def reversed_permutation_index(length: int, index: int):
    return sorted(permutations(range(length)), key=lambda x: x[0])[index -1]



if __name__ == '__main__':
    print(reversed_permutation_index(6, 271))
    # assert tuple(reversed_permutation_index(3, 5)) == (2, 0, 1)
