
from typing import List

def get_input(path: str) -> List[str]:
    with open(path) as f:
        return [line.strip() for line in f]

def part_one(lines: List[str]) -> int:
    total = 0
    for line in lines:
        pass
    return total

def part_two(lines: List[str]) -> int:
    total = 0
    for line in lines:
        pass
    return total

if __name__ == '__main__':
    lines = get_input('17_input.txt')
    print(part_one(lines))
    print(part_two(lines))
