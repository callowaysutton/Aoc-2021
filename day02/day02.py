direction = []

with open("input.txt") as a:
    for i in a:
        direction.append(i.strip())

def p1(scan):
    """Part One Solution
    """
    h = 0
    d = 0
    for move in direction:
        where = move.split()
        if where[0] == 'forward':
            h += int(where[1])
        if where[0] == 'up':
            d -= int(where[1])
        if where[0] == 'down':
            d += int(where[1])
    return (h*d)

def p2(direction):
    """Part Two Solution
    """
    h = 0
    d = 0
    aim = 0

    for move in direction:
        where = move.split()
        if where[0] == 'forward':
            h += int(where[1])
            d += aim * int(where[1])
        if where[0] == 'up':
            aim -= int(where[1])
        if where[0] == 'down':
            aim += int(where[1])
    return (h*d)

print(f"Problem 1 Solution: {p1(direction)}")
print(f"Problem 2 Solution: {p2(direction)}") 