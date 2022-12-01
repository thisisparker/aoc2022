elves = []

with open('input') as f:
    elf = []
    for l in f.readlines():
        if l != '\n':
            elf.append(int(l))
        else:
            elves.append(elf)
            elf = []

print('Max elf is carrying', sum(max(elves, key=sum)))

elves.sort(key=sum, reverse=True)

top_3 = 0

for p in range(3):
    top_3 += sum(elves[p])

print('Top 3 elves are carrying', top_3)
