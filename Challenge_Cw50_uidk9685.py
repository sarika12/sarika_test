"""
Challenge CW-50 - 31 Dec 2020 

Challenge 1 (pylint score * 10 Points):
The decimal number, 585 = 10010010012(binary), is palindromic in both bases.
Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
"""


def calculate():
    ans = sum(i for i in range(0, 100000) if is_decimal_binary_palindrome(i))
    return str(ans)


def is_decimal_binary_palindrome(n):
    s = str(n)
    if s != s[:: -1]:
        return False
    t = bin(n)[2:]
    return t == t[:: -1]


if __name__ == "__main__":
    print(calculate())

#
# def calculation():
#     for i in (range(0, 100000)):
#         if is_decimal_binary_pal((i)):
#             ans = str(i)
#     return ans
#
#
# def is_decimal_binary_pal(n):
#     s = str(n)
#
#     if s != s[:: -1]:
#         return False
#     t = bin(n)[2:]
#     return t == t[::-1]
#     print(t)
#
#
# if __name__ == "__main__":
#     print(calculation())
