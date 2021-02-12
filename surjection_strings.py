# import re

# def isometric_strings(str1, str2):
#     # example with 'add and 'egg':
#     # single characters are replaced with 0's
#     # multiplied characters with 1's
#     # for example 'add' is now represented by '01', so do 'egg'
#     # finally there's a comparison between two new strings '01' == '01'
#     for char1, char2 in zip(str1, str2):
#         str1 = re.sub("%s{2,}" % char1, "1", str1)
#         str1 = re.sub("%s{1}" % char1, "0", str1)
#         str2 = re.sub("%s{2,}" % char2, "1", str2)
#         str2 = re.sub("%s{1}" % char2, "0", str2)
#     return str1 == str2

w1, w2 = 'add', 'egg'

print(set(zip(w1,w2)))
    



# if __name__ == '__main__':
#     print("Example:")
#     print(isometric_strings('add', 'egg'))

#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert isometric_strings('add', 'egg') == True
#     assert isometric_strings('foo', 'bar') == False
#     assert isometric_strings('', '') == True
#     assert isometric_strings('all', 'all') == True
#     print("Coding complete? Click 'Check' to earn cool rewards!")
