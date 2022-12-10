def calc_problem_1(instructions):
    reg_x = 1
    pending = []
    significant = [20, 60, 100, 140, 180, 220]
    sig_sum = 0
    num = 0

    while instructions:
        num += 1
        if not pending:
            i = instructions.pop(0)

            if i.startswith('addx'):
                _, addend = i.split()
                pending.append([2,int(addend)])
            else:
                pending.append([1,0])

        # "During"

        if num in significant:
            sig_sum += (num * reg_x)

        # "After"

        for p in pending:
            p[0] = p[0]-1
            if p[0] == 0:
                reg_x += p[1]

        pending = [p for p in pending if p[0] > 0]

    print(sig_sum)

def calc_problem_2(instructions):
    reg_x = 1
    pending = []
    significant = [40, 80, 120, 160, 200, 240]
    num = 0

    while instructions:
        num += 1
        if not pending:
            i = instructions.pop(0)

            if i.startswith('addx'):
                _, addend = i.split()
                pending.append([2,int(addend)])
            else:
                pending.append([1,0])

        # "During"

        position = (num - 1) % 40
        if position in [reg_x, reg_x - 1, reg_x + 1]:
            print('#', end='')
        else:
            print('.', end='')
        if num in significant:
            print()

        # "After"

        for p in pending:
            p[0] = p[0]-1
            if p[0] == 0:
                reg_x += p[1]

        pending = [p for p in pending if p[0] > 0]

def main():
    with open('input') as f:
        instructions = [l.strip() for l in f.readlines()]

    calc_problem_1(instructions[:])

    calc_problem_2(instructions[:])


if __name__ == '__main__':
    main()
