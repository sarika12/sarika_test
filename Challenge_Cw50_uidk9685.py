"""
Challenge CW-50 - 31 Dec 2020 

Challenge 1 (pylint score * 10 Points):
The decimal number, 585 = 10010010012(binary), is palindromic in both bases.
Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
"""


def calculate():
    answer = sum(i for i in range(0, 100000) if is_decimal_binaryto_palindrome(i))
    return str(answer)


def is_decimal_binaryto_palindrome(n):
    value = str(n)
    if value  != value[:: -1]:
        return False
    rev = bin(n)[2:]
    return rev == rev[:: -1]


if __name__ == "__main__":
    print(calculate())

