def loadData(name):
    itemsPerElf = []
    items = []
    file = open(name, "r")
    for line in file:
        if line == '\n':
            itemsPerElf.append(items)
            items = []
        else:
            items.append(int(line))
    return itemsPerElf

def calculateCaloriesPerElf(itemsPerElf):
    caloriesPerElf = []
    for items in itemsPerElf:
        totalCalories = sum(items)
        caloriesPerElf.append(totalCalories)
    return caloriesPerElf

def day1():
    """
        Assignment day1:
        Elves have food items with calorie counts (list with list of ints)
        Part1: Find the elf with the highest total calories
        Part2: Find the 3 eves with the highest and sum
    """
    itemsPerElf = loadData("assignments/day1/data.txt")
    caloriesPerElf = calculateCaloriesPerElf(itemsPerElf)
    caloriesPerElf.sort(reverse=True)
    print("Day1 - Part1: " + str(caloriesPerElf[0]))
    totalTop3 = caloriesPerElf[0] + caloriesPerElf[1] + caloriesPerElf[2]
    print("Day1 - Part2: " + str(totalTop3))


