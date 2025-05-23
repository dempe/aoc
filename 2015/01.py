def find_floor() -> int:
    floor = 0
    with open('01_input.txt') as f:
        for line in f.read():
            for paren in line:
                if paren == '(':
                    floor += 1
                elif paren == ')':
                    floor -= 1
    return floor

def find_pos() -> int:
    floor = 0
    pos = 1
    with open('01_input.txt') as f:
        for line in f.read():
            for paren in line:
                if paren == '(':
                    floor += 1
                elif paren == ')':
                    floor -= 1
                if floor == -1:
                    return pos
                pos += 1
    return floor
                

if __name__ == "__main__":
    print(find_floor())
    print(find_pos())

