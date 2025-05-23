from typing import List

def get_input(path: str) -> List[str]:
    with open(path) as f:
        return [line.strip() for line in f]

def part_one(lines: List[str]) -> int:
    nice_lines = 0
    vowels = {'a', 'e', 'i', 'o', 'u'}
    disallowed = {'ab', 'cd', 'pq', 'xy'}

    for line in lines:
        vowel_cnt = sum(1 for c in line if c in vowels)
        found_disallowed = any(c1 + c2 in disallowed for c1, c2 in zip(line, line[1:]))
        found_double = any(c1 == c2 for c1, c2 in zip(line, line[1:]))

        if found_double and not found_disallowed and vowel_cnt >= 3:
            nice_lines += 1
    return nice_lines

def part_two(lines: List[str]) -> int:
	nice_lines = 0
	for line in lines:
		has_pair = any(line[i:i+2] in line[i+2:] for i in range(len(line) - 1))
		has_repeat = any(line[i] == line[i+2] for i in range(len(line) - 2))
        # has_repeat = any(c1 == c2 for c1, c2 in zip(line, line[2:]))
		if has_pair and has_repeat:
			nice_lines += 1
	return nice_lines

if __name__ == '__main__':
    lines = get_input('05_ex_input.txt')
    print(part_one(lines))
    print(part_two(lines))
