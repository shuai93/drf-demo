"""
一个关于进制问题的思考
"""

temp = {
    '10': 'a',
    '11': 'b',
    '12': 'c',
    '13': 'd',
    '14': 'd',
    '15': 'f'
}

temp_reverse = {v: k for k, v in temp.items()}


def translate1(num: int, extra: int) -> str:
    result = []
    while num != 0:
        result.append(str(num % extra))
        num = num // extra
    return "".join([temp.get(i, i) for i in result[::-1]])


def translate2(b: str, extra: int) -> int:
    result = 0
    for index, value in enumerate(b[::-1]):
        result += int(temp_reverse.get(value, value)) * extra ** index

    return result


def translate3(num: int):
    result = []
    while num != 0:
        result.append(str(num % 2))
        num = num // 2

    return "".join(result[::-1])


def num2xls_col(idx):
    if idx < 1:
        raise ValueError("Index is too small")
    result = ""
    while idx != 0:
        idx, r = divmod(idx - 1, 26)
        result = chr(r + ord('A')) + result
    return result


def main():
    # print(translate3(6))
    # print(translate1(6, 2))
    # for num in range(1, 26 * 8):
    #     if num % 26 in [0, 1, 2, 25, 24]:
    #         print(num2xls_col(num), end=",")
    #     elif num % 26 == 3:
    #         print("...", end="")
    "".startswith()
    for i in range(14, 20):
        b = translate1(i, 16)
        o = translate2(b, 16)
        print(hex(i)[2:], "".join(b), i, o)


if __name__ == "__main__":
    main()
