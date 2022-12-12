import re
stacks = list()

def day5_p1():
    global stacks

    with open('input.txt', 'r') as f:
        stack_nums = int(len(str(f.readline()).strip('\n')) / 4) + 1
        for i in range(stack_nums):
            stacks.append('')

    with open('input.txt', 'r') as f:
        l = str()
        while l != '\n':
            l = str(f.readline())
            for i in range(1, len(l) - 1, 4):
                if l[i].isupper():
                    stacks[int(i/4)] += l[i]
        stacks = [s[::-1] for s in stacks]
        l = f.readline()
        while l:
            print(stacks)
            print(l)
            num, fro, to = map(int, re.findall(r'\d+', l))
            #move_p1(num, fro - 1, to - 1)
            move_p2(num, fro - 1, to - 1)
            l = f.readline()

    return ''.join([s[-1] for s in stacks])


def move_p1(a, x, y):
    global stacks
    for i in range(a):
        stacks[y] += stacks[x][-1]
        stacks[x] = stacks[x][:-1]


def move_p2(a, x, y):
    global stacks
    for i in range(a):
        stacks[y] += stacks[x][-a + i]
    stacks[x] = stacks[x][:-a]


if __name__ == '__main__':
    print(day5_p1())

