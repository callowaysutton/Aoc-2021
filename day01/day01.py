scan = []
prev = -float('inf')
count = 0

with open("input.txt") as lines:
    for line in lines:
        scan.append(int(line.strip()))

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

print(count-1)