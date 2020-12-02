file = open("inputDay2").read().split('\n')
counts = 0

# ---------------------------------
#   DAY ONE
#   PART 1
# ---------------------------------

for i in file:
    passwordRow = i.split(':')
    char = passwordRow[0][-1]
    passwordCounts = passwordRow[0].split('-')
    Count2 = passwordCounts[1].split(' ')
    passwordCounts[1] = Count2[0]
    check = list(map(int, passwordCounts))
    if check[0] <= passwordRow[1].count(char) <= check[1]:
        counts +=1
print(counts)
# ---------------------------------
#   DAY ONE
#   PART 2
# ---------------------------------

counts = 0
for i in file:
    passwordRow = i.split(':')
    char = passwordRow[0][-1]
    passwordCounts = passwordRow[0].split('-')
    Count2 = passwordCounts[1].split(' ')
    passwordCounts[1] = Count2[0]
    check = list(map(int, passwordCounts))
    if passwordRow[1][check[0]] == char and passwordRow[1][check[1]] != char:
        counts += 1
    elif passwordRow[1][check[0]] != char and passwordRow[1][check[1]] == char:
        counts += 1
print(counts)



