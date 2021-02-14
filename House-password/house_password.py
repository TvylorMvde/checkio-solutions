import string

ascii_letters_digits = string.ascii_letters + string.digits


def checkio(data: str):
    is_digit, is_upper, is_lower = [False, False, False]
    if len(data) >= 10:
        for i in data:
            if i not in ascii_letters_digits:
                return False
            if i.isdigit():
                is_digit = True
            if i.isupper():
                is_upper = True
            if i.islower():
                is_lower = True
    else:
        return False

    return all([is_digit, is_upper, is_lower])


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
