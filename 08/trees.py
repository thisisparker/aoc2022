def main():
    with open('input') as f:
        tree_rows = [l.strip() for l in f.readlines()]

    rows = len(tree_rows)
    cols = len(tree_rows[0])
    sightlines = {}

    for y in range(rows):
        for x in range(cols):
            dirs = []
            # view looking north
            dirs.append(''.join([t for r in range(y)
                                    for t in tree_rows[r][x]][::-1]))
            # view looking east
            dirs.append(tree_rows[y][x+1:])
            # view looking south
            dirs.append(''.join([t for r in range(y+1, rows)
                                    for t in tree_rows[r][x]]))
            # view looking west
            dirs.append(tree_rows[y][:x][::-1])

            sightlines[(x,y)] = dirs

    visible_trees = 0
    for k in sightlines:
        for d in sightlines[k]:
            if not any(int(t) >= int(tree_rows[k[1]][k[0]]) for t in d):
                visible_trees += 1
                break

    print(visible_trees)

    scenic_scores = []
    for k in sightlines:
        scenic_score = 1
        for d in sightlines[k]:
            view_distance = 0
            for t in d:
                view_distance += 1
                if int(t) >= int(tree_rows[k[1]][k[0]]):
                    break
            scenic_score = scenic_score * view_distance
        scenic_scores.append(scenic_score)

    print(max(scenic_scores))

if __name__ == '__main__':
    main()
