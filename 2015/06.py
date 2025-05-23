from typing import List
import re

COORD_PAT = re.compile(r'\d{1,3},\d{1,3}')

def get_input(path: str) -> List[str]:
    with open(path) as f:
        return [line.strip() for line in f]

def part_one(lines: List[str]) -> int:
    lights = [[False for _ in range(1000)] for _ in range(1000)]
    for line in lines:
        turn_on  = line.startswith('turn on')
        turn_off = line.startswith('turn off')
        matches  = COORD_PAT.findall(line)
        x1, y1   = map(int, matches[0].split(','))
        x2, y2   = map(int, matches[1].split(','))

        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if turn_on:    lights[x][y] = True
                elif turn_off: lights[x][y] = False
                else:          lights[x][y] = not lights[x][y]
        

    return sum(cell for row in lights for cell in row)    

def part_two(lines: List[str]) -> int:
    lights = [[0 for _ in range(1000)] for _ in range(1000)]
    for line in lines:
        inc     = line.startswith('turn on')
        dec     = line.startswith('turn off')
        matches = COORD_PAT.findall(line)
        x1, y1  = map(int, matches[0].split(','))
        x2, y2  = map(int, matches[1].split(','))

        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if inc:   lights[x][y] += 1
                elif dec: lights[x][y] = max(0, lights[x][y] - 1)
                else:     lights[x][y] += 2
        

    return sum(cell for row in lights for cell in row)    

if __name__ == '__main__':
    lines = get_input('06_input.txt')
    print(part_one(lines))
    print(part_two(lines))
