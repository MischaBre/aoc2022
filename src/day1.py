# day1 of aoc2022

def day1() -> int:
    with open('../input/day1.txt', 'r') as f:
        elves_cal = list()
        cal_sum = 0
        for l in f:
            if l == '\n':
                elves_cal.append(cal_sum)
                cal_sum = 0
            else:
                cal_sum += int(l)
        print(sorted(elves_cal, reverse=True))
        # part 1
        # return max(elves_cal)

        # part 2
        return sum(sorted(elves_cal, reverse=True)[0:3])


if __name__ == '__main__':
    print(day1())
