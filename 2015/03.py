from typing import List, Tuple

def get_input(path: str) -> List[str]:
    with open(path) as f:
        return [line.strip() for line in f]

def move(pos: Tuple[int, int], direction: str) -> Tuple[int, int]:
    x, y = pos
    match direction:
        case '^': return (x, y + 1)
        case 'v': return (x, y - 1)
        case '>': return (x + 1, y)
        case '<': return (x - 1, y)
        case _: raise ValueError(f"Unknown direction: {direction}")

def part_one(lines: List[str]) -> int:
    visited = {(0, 0)}
    pos = (0, 0)
    for line in lines:
        for c in line:
            pos = move(pos, c)
            visited.add(pos)
    return len(visited)

def part_two(lines: List[str]) -> int:
    visited = {(0, 0)}
    santa = (0, 0)
    robo = (0, 0)

    for i, c in enumerate(''.join(lines)):
        if i % 2 == 0:
            robo = move(robo, c)
            visited.add(robo)
        else:
            santa = move(santa, c)
            visited.add(santa)

    return len(visited)

if __name__ == '__main__':
    lines = get_input('03_input.txt')
    print(part_one(lines))
    print(part_two(lines))
