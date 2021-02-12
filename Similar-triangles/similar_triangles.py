from itertools import combinations
from math import pow, sqrt, acos, pi

class Triangle:

    def __init__(self, coords):
        if isinstance(coords, list):
            if len(coords) == 3:
                self.coords = coords
            else:
                raise ValueError("Wrong number of coordinates. Must be 3!")
        else:
            raise TypeError("Argument must be a list of coordinates.")


    def calculate_sides(self):
        self.sides = []
        for x, y in combinations(self.coords, 2):
            self.sides.append(sqrt(pow(y[0] - x[0], 2) + pow(y[1] - x[1], 2)))
        self.a, self.b, self.c = [round(side, 3) for side in self.sides]


    def calculate_angles(self):
        self.alpha = acos((self.b**2 + self.c**2 - self.a**2) / (2 * self.b * self.c))
        self.beta = acos((self.a**2 + self.c**2 - self.b**2) / (2 * self.a * self.c))
        self.gamma = acos((self.a**2 + self.b**2 - self.c**2) / (2 * self.a * self.b))
        self.angles = [round(x * 180 / pi, 3) for x in [self.alpha, self.beta, self.gamma]]


# SSS: side-side-side
def sss(t1, t2):
    if len({x / y for x, y in zip(t1.sides, t2.sides)}) == 1:
        return True


# AAA: angle-angle-angle
def aaa(t1, t2):
    a1 = set(t1.angles)
    a2 = set(t2.angles)
    if len(a1.intersection(a2)) >= 2:
        return True


# SAS: side-angle-side
def sas(t1, t2):
    for obj in (t1, t2):
        obj.sides.sort()
        obj.angles.sort()
    
    s1, s2 = t1.sides, t2.sides
    a1, a2 = t1.angles, t2.angles

    if s1[0] / s2[0] == s1[1] / s2[1]:
        if a1[2] == a2[2]:
            return True
    if s1[1] / s2[1] == s1[2] / s2[2]:
        if a1[0] == a2[0]:
            return True
    if s1[2] / s2[2] == s1[0] / s2[0]:
        if a1[1] == a2[1]:
            return True
    return False


def similar_triangles(coords_1, coords_2):
    t1 = Triangle(coords_1)
    t2 = Triangle(coords_2)

    t1.calculate_sides()
    t1.calculate_angles()

    t2.calculate_sides()
    t2.calculate_angles()

    for t in (t1, t2):
        print(t.a, t.b, t.c)
        print([angle for angle in t.angles])

    if sss(t1, t2):
        return True

    if aaa(t1, t2):
        return True
    
    if sas(t1, t2):
        return True
    
    return False


if __name__ == '__main__':

    # These "asserts" are used for self-checking and not for an auto-testing
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [
                             (3, 0), (4, 2), (5, 0)]) is True, 'basic'
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(
        3, 0), (4, 3), (5, 0)]) is False, 'different #1'
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [
                             (2, 0), (4, 4), (6, 0)]) is True, 'scaling'
    assert similar_triangles([(0, 0), (0, 3), (2, 0)], [
                             (3, 0), (5, 3), (5, 0)]) is True, 'reflection'
    assert similar_triangles([(1, 0), (1, 2), (2, 0)], [(
        3, 0), (5, 4), (5, 0)]) is True, 'scaling and reflection'
    assert similar_triangles([(1, 0), (1, 3), (2, 0)], [(
        3, 0), (5, 5), (5, 0)]) is False, 'different #2'
    assert similar_triangles(
        [[-3, -1], [3, 3], [-3, 1]], [[-3, -9], [9, 9], [3, 9]]) is True
    
    print("Coding complete? Let's try tests!")

   

