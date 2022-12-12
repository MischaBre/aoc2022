def check_list_contains(x,y):
    return (int(y[0]) <= int(x[0]) and int(x[1]) <= int(y[1])) or \
           (int(x[0]) <= int(y[0]) and int(y[1]) <= int(x[1]))


def check_list_overlap(x,y):
    return int(x[0]) <= int(y[1]) and int(y[0]) <= int(x[1])

def day4_p1():
    with open('input.txt', 'r') as f:
        ranges = [str(l).strip().split(',') for l in f.readlines()]
        #print(ranges)
        #sum_ranges = [x for x in ranges if check_list_contains(x[0].split('-'), x[1].split('-'))]
        sum_ranges = [x for x in ranges if check_list_overlap(x[0].split('-'), x[1].split('-'))]
        print(sum_ranges)
        return len(sum_ranges)


if __name__ == '__main__':
    print(day4_p1())
