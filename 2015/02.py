from itertools import accumulate

def find_sqft():
    with open('02_input.txt') as f:
        total = 0
        for line in f:
            w, l, h = map(int, line.strip().split('x'))
            total += 2*w*h + 2*l*h + 2*w*l + min(w*h, l*h, w*l)
        return total

def part_two():
    with open('02_input.txt') as f:
        total = 0
        for line in f:
            w, l, h = map(int, line.strip().split('x'))
            bow = w*l*h
            wrap = (sum([w, l, h]) - max(w, l, h)) * 2
            total += bow + wrap
        return total

if __name__ == '__main__':
    print(find_sqft())
    print(part_two())
