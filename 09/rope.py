class Position:
    def __repr__(self):
        return f'({self.x}, {self.y})'
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __hash__(self):
        return hash((self.x, self.y))
    def __init__(self, x, y):
        self.x = x
        self.y = y


def calculate_tail_position(head_pos, tail_pos):
    if abs(head_pos.x - tail_pos.x) == 2:
        new_x = (head_pos.x + tail_pos.x) // 2
        
        slide = (1 if head_pos.y > tail_pos.y
                    else -1 if head_pos.y < tail_pos.y
                    else 0)

        tail_pos = Position(new_x, tail_pos.y + slide)
    elif abs(head_pos.y - tail_pos.y) == 2:
        new_y = (head_pos.y + tail_pos.y) // 2

        slide = (1 if head_pos.x > tail_pos.x
                    else -1 if head_pos.x < tail_pos.x
                    else 0)
        tail_pos = Position(tail_pos.x + slide, new_y)

    return tail_pos

def move_head(direction, head_pos, tail_pos):
    if direction == 'L':
        head_pos = Position(head_pos.x-1, head_pos.y)
    elif direction == 'R':
        head_pos = Position(head_pos.x+1, head_pos.y)
    elif direction == 'U':
        head_pos = Position(head_pos.x, head_pos.y+1)
    elif direction == 'D':
        head_pos = Position(head_pos.x, head_pos.y-1)

    tail_pos = calculate_tail_position(head_pos, tail_pos)

    return head_pos, tail_pos

def main():
    with open('input') as f:
        moves = [l.strip() for l in f.readlines()]
# Sample input 1:
#    moves = """R 4
#               U 4
#               L 3
#               D 1
#               R 4
#               D 1
#               L 5
#               R 2""".split('\n')
#    moves = [l.strip() for l in moves]

# Sample input 2:
#    moves = """R 5
#               U 8
#               L 8
#               D 3
#               R 17
#               D 10
#               L 25
#               U 20""".split('\n')
#    moves = [l.strip() for l in moves]

    moves = [(m.split()[0], int(m.split()[1])) for m in moves]

    tail_visited = []

    head_pos = Position(0,0)
    tail_pos = Position(0,0)
    for m in moves:
        direction, distance = m
        while distance:
            head_pos, tail_pos = move_head(direction, head_pos, tail_pos)
            tail_visited.append(tail_pos)

            distance -= 1

    print(len(set(tail_visited)))

    all_pos = [Position(0,0) for _ in range(10)]

    tail_visited = []
    for m in moves:
        direction, distance = m
        while distance:
            all_pos[0], all_pos[1] = move_head(direction,
                                         all_pos[0],
                                         all_pos[1])
            for p in range(2, len(all_pos)):
                all_pos[p] = calculate_tail_position(all_pos[p-1],
                                                     all_pos[p])


            tail_visited.append(all_pos[-1])

            distance -= 1

    print(len(set(tail_visited)))

if __name__ == '__main__':
    main()
