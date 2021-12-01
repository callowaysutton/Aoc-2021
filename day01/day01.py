scan = []
with open("input.txt") as lines:
    for line in lines:
        scan.append(int(line.strip()))

def p1(scan):
    """Part One Solution
    """
    prev = -float('inf')
    count = 0
    for i,pulse in enumerate(scan):
        if pulse > prev:
            prev = pulse
            count+=1
        else:
            prev = pulse

    return count-1

def p2(scan):
    """Part Two Solution
    """
    prev = -float('inf')
    count = 0
    for i,pulse in enumerate(scan):
        a = 0
        try:
            for j in range(3):
                a+=scan[i+j]
        except:
            break
        if a > prev:
            prev = a
            count+=1
        else:
            prev = a

    return count-1

print(f"Problem 1 Solution: {p1(scan)}")
print(f"Problem 2 Solution: {p2(scan)}") 