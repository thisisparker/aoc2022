def main():
    with open('input') as f:
        output = [l.strip() for l in f.readlines()][1:]

    tree = {}
    parent_dirs = ['/']
    for i in output:
        pwd = parent_dirs[-1]
        if i.startswith('$ cd'):
            dst = i.split()[2]
            if dst == '..':
                parent_dirs.pop()
            else:
                parent_dirs.append(pwd + dst + '/')

        elif i.startswith('$ ls'):
            continue

        else:
            size_or_type, name = i.split()
            if not size_or_type.isnumeric():
                continue

            for d in parent_dirs:
                tree[d] = tree.get(d, 0) + int(size_or_type)

    small_dirs = [d for d in tree if tree[d] <= 100000]

    print(sum([tree[d] for d in small_dirs]))

    available = 70000000 - tree['/']
    target = 30000000 - available

    print(min([tree[d] for d in tree if tree[d] >= target]))


if __name__ == '__main__':
    main()
