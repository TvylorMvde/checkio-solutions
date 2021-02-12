

def isometric_strings(str1: str, str2: str):
    max_chars = 256
    if len(str1) != len(str2):
        return False

    marked = [False] * max_chars
    mapping = [-1] * max_chars

    for i in range(len(str2)):
        if mapping[ord(str1[i])] == -1:
            if marked[ord(str2[i])] == True:
                return False
            marked[ord(str2[i])] == True
            mapping[ord(str1[i])] == str2[i]
        elif mapping[ord(str1[i])] != str2[i]:
            return False
    return True


if __name__ == '__main__':
    print("Example:")
    print(isometric_strings('add', 'egg'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert isometric_strings('add', 'egg') == True
    assert isometric_strings('foo', 'bar') == False
    assert isometric_strings('', '') == True
    assert isometric_strings('all', 'all') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
