"""Generate an infinite stream of successively larger random lists."""

import helper

def generate_cases():
    size = -1
    while True:
        size += 1
        yield helper.random_list(size)


if __name__ == '__main__':
    for case in generate_cases():
        if len(case) > 10:
            break
        print(case)