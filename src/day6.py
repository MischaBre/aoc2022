

def day6_p1():
    with open('../input/day6.txt', 'r') as f:
        inputs = [str(l) for l in f.readlines()]
        for inp in inputs:
            for i, _ in enumerate(inp):
                len_marker = 4
                len_message = 14
                # test_marker = inp[i:i + len_marker]
                test_message = inp[i:i + len_message]
                if is_unique_str_char(test_message, len_message):
                    return i + 14
    return 0


def is_unique_str_char(test_str, length):
    return len(set(test_str)) == length


if __name__ == '__main__':
    print(day6_p1())