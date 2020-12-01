file = open("day1Input.txt").read().split('\n')
file = list(map(int, file))

# ---------------------------------
#   DAY ONE
#   PART 1
# ---------------------------------

for i in file:
    for x in file:
        if x+i == 2020:
            print(x * i)
            break


# ---------------------------------
#   DAY ONE
#   PART 2
# ---------------------------------

file = list(map(int, file))
for i in file:
    for x in file:
        for t in file:
            if x+i+t == 2020:
                print(x * i * t)
                break


