import re


def long_repeat(line: str) -> int:
  if len(line) != 0:
    matches = [match.group() for match in re.finditer(r'(.)\1*', line)]
    return len(sorted(matches, key=len)[-1])
  return 0


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')
