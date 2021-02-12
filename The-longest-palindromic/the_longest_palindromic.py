def longest_palindromic(text):
    palyndromes = []
    for i in range(len(text)):
        start = end = i
        for j in range(len(text)):
            substring = text[start:end+1]
            if substring == substring[::-1]:
                palyndromes.append(substring)
            end += 1
    return max(palyndromes, key=len)


if __name__ == '__main__':
    print("Example:")
    print(longest_palindromic('abc'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert longest_palindromic('abc') == 'a'
    assert longest_palindromic('abacada') == 'aba'
    assert longest_palindromic('artrartrt') == 'rtrartr'
    assert longest_palindromic('aaaaa') == 'aaaaa'
    print("Coding complete? Click 'Check' to earn cool rewards!")
