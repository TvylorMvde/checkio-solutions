def to_encrypt(text, delta):
    letters = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for letter in text:
        if letter == " ":
            result += " "
            continue
        
        idx = letters.index(letter)
       
        if idx + delta <= len(letters) - 1:
            result += letters[idx + delta]
        else:
            result += letters[abs(delta - (len(letters) - idx))]
    return result




if __name__ == '__main__':
    print("Example:")
    print(to_encrypt("important text", 10))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_encrypt("a b c", 3) == "d e f"
    assert to_encrypt("a b c", -3) == "x y z"
    assert to_encrypt("simple text", 16) == "iycfbu junj"
    assert to_encrypt("important text", 10) == "swzybdkxd dohd"
    assert to_encrypt("state secret", -13) == "fgngr frperg"
    print("Coding complete? Click 'Check' to earn cool rewards!")
