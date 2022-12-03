# AoC day2

translation_dict = {'A': 'X',
                    'B': 'Y',
                    'C': 'Z'}
winning_dict =     {'X': 'Y',
                    'Y': 'Z',
                    'Z': 'X'}
score_dict =       {'X': 1,
                    'Y': 2,
                    'Z': 3}


def day2() -> int:
    result = 0
    with open('../input/day2.txt', 'r') as f:
        for _, l in enumerate(f.readlines()):
            opp, you = l.strip().split(' ')[0:2]
            # part1
            # result += score_dict[you] + winning_score(opp, you)

            # part2
            reaction_you = reaction_scheme(opp, score_dict[you])
            result += score_dict[reaction_you] + winning_score(opp, reaction_you)
    return result


def winning_score(a, b) -> int:
    if translation_dict[a] == b:
        return 3
    if winning_dict[translation_dict[a]] == b:
        return 6
    else:
        return 0


# part 2
def reaction_scheme(a, r) -> int:
    if r == 1:
        return winning_dict[winning_dict[translation_dict[a]]]
    if r == 2:
        return translation_dict[a]
    if r == 3:
        return winning_dict[translation_dict[a]]


if __name__ == '__main__':
    print(day2())
