rows = open("input").read().split("\n")

print(rows)


def CalcSlope(right, down):
    countTree = 0
    x = 0
    for y in range(0, len(rows), down):
        if (x - len(rows[y])) >= 0:
            x -= len(rows[y])
        if rows[y][x] == "#":
            countTree += 1
        x += right
    return countTree

print(CalcSlope(1, 1) * CalcSlope(3, 1) * CalcSlope(5, 1) * CalcSlope(7, 1) * CalcSlope(1, 2))
