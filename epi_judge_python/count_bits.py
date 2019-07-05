from test_framework import generic_test


def count_bits(x):
    num = 0
    one = 1
    while x:
        if x & one:
            num += 1
        x = x >> 1
    # print("x=", x , "num = ", num)
    return num

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("count_bits.py", 'count_bits.tsv',
                                       count_bits))
