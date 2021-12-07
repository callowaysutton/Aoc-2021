values = []
with open("input.txt") as a:
    for i in a:
        values.append(i.strip())

values = ["00100",
"11110",
"10110",
"10111",
"10101",
"01111",
"00111",
"11100",
"10000",
"11001",
"00010",
"01010"]

prob = {}

def p1(values):
    """Part One Solution
    """
    gamma = ""
    epsilon = ""
    for val in values:
        for i,bit in enumerate(val):
            if i not in prob:
                prob[i] = int(val[i])
            else:
                prob[i] += int(val[i])

    for i in prob:
        gamma += str(round(prob[i]/len(values)))

    epsilon = ''.join(['1' if i == '0' else '0' for i in gamma])

    return int(gamma,2) * int(epsilon,2)

def p2(values):
    """Part Two Solution
    """
    def Oxy(num1,pos):
        num = 0
        if len(num1)==1:
            return num1[0]
        for i in num1:
            num += int(i[pos])
        common = "1" if num/len(num1) > 0.49 else "0"
        return Oxy([i for i in num1 if i[pos] == common], pos+1)
    
    def Carb(num1,pos):
        num = 0
        if len(num1) == 1:
            return num1[0]
        for i in num1:
            if i[pos] == '0':
                num += 1
        common = "1" if num/len(num1) > 0.5 else "0"
        print(common)
        return Carb([i for i in num1 if i[pos] == common], pos+1)
    return int(Oxy(values,0),2)*int(Carb(values,0),2)

# print(f"Problem 1 Solution: {p1(values)}")
print(f"Problem 2 Solution: {p2(values)}")