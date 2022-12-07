def main():
    with open('input') as f:
        output = [l.strip() for l in f.readlines()][1:]

    tree = {}
    pwd = '/'
    current_view = None
    for i in output:
        if i.startswith('$ cd'):
            dst = i.split()[2]
            pwd = pwd + dst + '/' if dst != '..' else pwd.rsplit('/', 2)[0] + '/'
        elif i.startswith('$ ls'):
            continue
        else:
            size_or_type, name = i.split()
            if size_or_type.isnumeric():
                parent_dirs = []
                for slash in range(1, pwd.count('/') + 1):
                    parent_dirs.append(pwd.rsplit('/', slash)[0] + '/')
                for d in parent_dirs:
                    tree[d] = (tree.get(d, 0) + int(size_or_type))

    small_dirs = [d for d in tree if tree[d] <= 100000]

    print(sum([tree[d] for d in small_dirs]))

    available = 70000000 - tree['/']
    target = 30000000 - available

    print(min([tree[d] for d in tree if tree[d] >= target]))

        

if __name__ == '__main__':
    main()
