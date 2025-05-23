from typing import List
from hashlib import md5

SECRET_KEY = 'ckczppom'

def part_one() -> int:
    for i in range(1, 10 ** 9):
        key = f"{SECRET_KEY}{str(i)}"
        if md5(key.encode()).hexdigest().startswith("00000"):
            return i

    return 0

def part_two() -> int:
    for i in range(1, 10 ** 9):
        key = f"{SECRET_KEY}{str(i)}"
        if md5(key.encode()).hexdigest().startswith("000000"):
            return i

    return 0

if __name__ == '__main__':
    print(part_one())
    print(part_two())
