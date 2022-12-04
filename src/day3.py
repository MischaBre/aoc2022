# day3 AoC 2022

def day3_part1() -> int:
    result = 0
    with open('../input/day3.txt', 'r') as f:
        for lines in f.readlines():
            result += return_string_priority(lines.strip())
    return result


def day3_part2() -> int:
    result = 0
    with open('../input/day3.txt', 'r') as f:
        lines = f.readlines()
        for i in range(0, len(lines)-1, 3):
            result += return_group_priority(lines[i:i+3])
    return result


def return_group_priority(l) -> int:
    r1 = list(set(l[0].strip()))
    r2 = [c for c in list(set(l[1])) if c in r1]
    r3 = [c for c in list(set(l[2])) if c in r2]
    print(r3)
    return sum(ord(c) - 96 for c in r3 if ord(c) > 96) + sum(ord(c) - 64 + 26 for c in r3 if ord(c) < 97)


def return_string_priority(s) -> int:
    dep1 = list(set(s[:int(len(s)/2)]))
    dep2 = list(set(s[int(len(s)/2):]))
    errors = [c for c in dep1 if c in dep2]
    # print(errors)
    return sum(ord(c)-96 for c in errors if ord(c) > 96) + sum(ord(c)-64+26 for c in errors if ord(c) < 97)


if __name__ == '__main__':
    print(day3_part2())
