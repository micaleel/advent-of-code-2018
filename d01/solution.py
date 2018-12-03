def part_1():
    """
    Solution to Ex1 Pt 1
    """
    with open('input.txt') as fp:
        frequency = 0
        for line in fp.readlines():
            frequency += int(line)
        print(f'Ex 1 Pt 1: Answer {frequency}')

def get_first_reach(changes):
    frequencies = set([0])
    frequency = 0
    change_idx = 0
    num_cycles = 0
    while True:
        frequency += int(changes[change_idx])
        if frequency in frequencies:
            return frequency
        else:
            frequencies.add(frequency)
        change_idx = (change_idx + 1) % len(changes)
        num_cycles + 1
        if num_cycles > len(changes):
            return None

def part_2():
    """
    Solution to Ex1 Pt 2
    """
    with open('input.txt') as fp:
        answer = get_first_reach(fp.readlines())
        print(f'Ex 1 Pt 2: {answer}')


if __name__ == '__main__':
    part_1()
    part_2()