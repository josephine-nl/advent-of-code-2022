
def loadData(name):
    lines = []
    file = open(name, "r")
    for line in file:
        if line == '\n':
            print('blep')
        else:
            lines.append(int(line))
    return lines

def day2():
    """
        Assignment day2:
        Elves have food items with calorie counts (list with list of ints)
        Part1: Find the elf with the highest total calories
        Part2: Find the 3 eves with the highest and sum
    """
    data = loadData("assignments/day2/test.txt")
    part1 = 1
    part2 = 2
    print("Day1 - Part1: " + str(part1))
    print("Day1 - Part2: " + str(part2))

