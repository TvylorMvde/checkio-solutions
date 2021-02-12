import numpy as np

def create_intervals(data):
    data = sorted(data)
    diffs = np.diff(list(sorted(data)))
    indices = [pos + 1 for pos, val in enumerate(diffs) if val != 1]
    intervals = [i for i in np.split(list(data), indices)]

    tuples = []
    for interval in intervals:
        if len(interval) == 0:
            continue
        elif len(interval) == 1:
            tuples.append((interval[0], interval[0]))
        else:
            tuples.append((interval[0], interval[-1]))

    return tuples


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert create_intervals({1, 2, 3, 4, 5, 7, 8, 12}) == [
        (1, 5), (7, 8), (12, 12)], "First"
    assert create_intervals({1, 2, 3, 6, 7, 8, 4, 5}) == [(1, 8)], "Second"
    print('Almost done! The only thing left to do is to Check it!')
