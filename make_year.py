import sys
from pathlib import Path

TEMPLATE =  """
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
    lines = get_input('{day}_input.txt')
    print(part_one(lines))
    print(part_two(lines))
"""

def fill_dir(year: str) -> None:
    Path(year).mkdir(exist_ok=True)

    for i in range(1, 26):
        day = str(i).zfill(2)
        path = Path(f"./{year}/{day}.py")

        if path.exists(): continue  # Don't overwrite progress

        with path.open('w') as f:
            f.write(TEMPLATE.format(day=day))

if __name__ == '__main__':
    fill_dir(sys.argv[1])
