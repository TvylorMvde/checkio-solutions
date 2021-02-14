from math import sqrt, pi, pow

def simple_areas(*args):
    if len(args) == 3:
        a, b, c = args
        #heron formula: a + b + c / 2
        h = sum(args) / 2
        return sqrt(h * (h - a) * (h - b) * (h - c))
    elif len(args) == 2:
        a, b = args
        return a * b
    else:
        return pi * pow(1 / 2 * args[0], 2)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=2):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(simple_areas(3), 7.07), "Circle"
    assert almost_equal(simple_areas(2, 2), 4), "Square"
    assert almost_equal(simple_areas(2, 3), 6), "Rectangle"
    assert almost_equal(simple_areas(3, 5, 4), 6), "Triangle"
    assert almost_equal(simple_areas(1.5, 2.5, 2), 1.5), "Small triangle"
