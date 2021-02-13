def middle(text):
    middle = len(text) // 2
    if len(text) % 2 != 0:
        return text[middle]
    return text[middle - 1] + text[middle]


print(middle('test'))

if __name__ == '__main__':
    print("Example:")
    print(middle('example'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert middle('example') == 'm'
    assert middle('test') == 'es'
    assert middle('very-very long sentence') == 'o'
    assert middle('I') == 'I'
    assert middle('no') == 'no'
    print("Coding complete? Click 'Check' to earn cool rewards!")
