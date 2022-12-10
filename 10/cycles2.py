def get_runtime(i):
    times = {'noop': 1,
             'addx': 2,
            }
    return times[i.split()[0]]

def compute_sig_sums(comp):
    if comp.num in comp.sigcycles:
        comp.sig_sum += (comp.num * comp.register)

def print_crt(comp):
    position = (comp.num - 1) % 40
    if position in [comp.register - 1, comp.register, comp.register + 1]:
        print('#', end='')
    else:
        print('.', end='')
    if comp.num in comp.sigcycles:
        print()

class Computer:
    def __init__(self, do_action, sigcycles=[], **kwargs):
        self.sigcycles = sigcycles
        self.do_action = do_action

        if 'sig_sum' in kwargs:
            self.sig_sum = kwargs.get('sig_sum')

    def operate(self, instructions, register=1):
        self.num = 0
        self.register = register
        pending = []
        inst = instructions.copy()
        while inst:
            self.num += 1
            if not pending:
                i = inst.pop(0)
                pending.append([get_runtime(i),i])

            # during
            self.do_action(self)

            #after
            for p in pending:
                p[0] -= 1
                if p[0] == 0:
                    self.run(p[1])

            pending = [p for p in pending if p[0] > 0]

    def run(self, operation):
        if operation.startswith('noop'):
            pass
        elif operation.startswith('addx'):
            addend = int(operation.split()[1])
            self.register += addend

def main():
    with open('input') as f:
        instructions = [l.strip() for l in f.readlines()]

    comp1 = Computer(compute_sig_sums, [20,60,100,140,180,220], sig_sum=0)
    comp1.operate(instructions)
    print(comp1.sig_sum)

    comp2 = Computer(print_crt, [40,80,120,160,200,240])
    comp2.operate(instructions)


if __name__ == '__main__':
    main()
