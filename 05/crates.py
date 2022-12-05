from pprint import pprint

def move_stacks(stacks, instructions, multiple=False):
    for i in instructions:
        p = i.split()
        """p[1] is qty, p[3] is src, p[5] is dst"""

        p[1], p[3], p[5] = int(p[1]), int(p[3]), int(p[5])

        moved_blocks = stacks[p[3]][:p[1]]
        if not multiple:
            moved_blocks.reverse()

        stacks[p[5]] = moved_blocks + stacks[p[5]]
        stacks[p[3]] = stacks[p[3]][p[1]:]
    
    return stacks

def main():
    stacks = {}
    with open('input') as f:
        for l in [line.strip('\n') for line in f.readlines()]:
            if l.startswith(' 1'):
                break
            for x in range(0, 9):
                stacks[x+1] = stacks.get(x+1, [])
                value = l[x*4:x*4+3]
                if value != '   ':
                    stacks[x+1].append(value)

    with open('input') as f: #lol
        instructions = []
        for l in [line.strip('\n') for line in f.readlines()]:
            if l.startswith('move'):
                instructions.append(l)

    restacked = move_stacks(stacks.copy(), instructions)

    print('the top of the stacks moved one-at-a-time:')

    for k in restacked:
        print(restacked[k][0], end='')

    multiple_restacked = move_stacks(stacks.copy(), instructions, multiple=True)

    print('\nthe top of the stacks moved all at once:')
    
    for k in multiple_restacked:
        print(multiple_restacked[k][0], end='')
    
    print()


if __name__ == '__main__':
    main()
