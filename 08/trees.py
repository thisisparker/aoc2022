def main():
    with open('input') as f:
        tree_rows = [l.strip() for l in f.readlines()]

    visible_trees = 0
    rows = len(tree_rows)
    cols = len(tree_rows[0])

    for y in range(rows):
        for x in range(cols):
            h = int(tree_rows[y][x])
            obs_e = ''.join([t for t in tree_rows[y][x+1:] if int(t) >= h])
            obs_w = ''.join([t for t in tree_rows[y][:x] if int(t) >= h])
            obs_n = ''.join([t for r in range(y)
                                        for t in tree_rows[r][x] if int(t) >= h])
            obs_s = ''.join([t for r in range(y+1, rows) 
                                        for t in tree_rows[r][x] if int(t) >= h])

            if not(obs_e) or not(obs_w) or not(obs_n) or not(obs_s):
                visible_trees += 1

    print(visible_trees)

    t = tree_rows

    scenic_scores = {}
    for y in range(rows):
        for x in range(cols):
            h = int(tree_rows[y][x])
            views = {'n':0,'s':0,'e':0,'w':0}
            n = y - 1
            while n >= 0:
                views['n'] += 1
                if int(t[n][x]) >= h:
                    break
                else:
                    n -= 1
            s = y + 1
            while s < rows:
                views['s'] += 1
                if int(t[s][x]) >= h:
                    break
                else:
                    s += 1
            e = x + 1
            while e < cols:
                views['e'] += 1
                if int(t[y][e]) >= h:
                    break
                else:
                    e += 1
            w = x - 1
            while w >= 0:
                views['w'] += 1
                if int(t[y][w]) >= h:
                    break
                else:
                    w -= 1
            scenic_scores[(x,y)] = views['n'] * views['s'] * views['e'] * views['w']

    print(max(scenic_scores.values()))

if __name__ == '__main__':
    main()
