TABLE = '''
A 85-89%
A- 80-84%
B+ 77-79%
B 73-76%
B- 70-72%
C+ 67-69%
C 63-66%
C- 60-62%
D+ 57-59%
D 53-56%
D- 50-52%
'''

grades = {}

def ryerson_letter_grade(pct: int):
    if pct > 89:
        return "A+"
    elif pct < 50:
        return "F"
    else:
        for line in TABLE.splitlines():
            line = line.strip().rstrip("%").split()
            if line:
                grade = line[0]
                low, high = [int(x) for x in line[-1].split("-")]
                grades[grade] = range(low, high + 1)
        for key, value in grades.items():
            if pct in value:
                return key


if __name__ == '__main__':
    print("Example:")
    print(ryerson_letter_grade(45))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert ryerson_letter_grade(45) == "F"
    assert ryerson_letter_grade(62) == "C-"
    
    print("Coding complete? Click 'Check' to earn cool rewards!")
