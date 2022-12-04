
def loadData(name):
    backpacks = []
    file = open(name, "r")
    for line in file:
        backpacks.append(line.replace('\n',''))
    return backpacks

def findItemInBothCompartments(backpack):
    # sep in two compartments
    c1 = backpack[:len(backpack)//2]
    c2 = backpack[len(backpack)//2:]
    for element in c1:
        if element in c2:
            return element
    print("error")

def getValueItem(item):
    if item.isupper():
        return ord(item) - 38
    else:
        return ord(item) - 96

def findAllPriorities(backpacks):
    total = 0
    for backpack in backpacks:
        doubleItem = findItemInBothCompartments(backpack)
        value = getValueItem(doubleItem)
        total += value
    return total

def findTeamBadges(backpacks):
    total = 0
    for teamLeaderIndex in range(0,len(backpacks),3):
        print(teamLeaderIndex)
        teamLeader = backpacks[teamLeaderIndex]
        teamMember1 = backpacks[teamLeaderIndex + 1]
        teamMember2 = backpacks[teamLeaderIndex + 2]
        badge = -1
        for item in teamLeader:

            if item in teamMember1 and item in teamMember2:
                print(item)
                value = getValueItem(item)
                print(value)
                badge = value
        total += badge
    return total


def day3():
    """
        Assignment day3:
        elves have backpacks now?
        part1: find the item that is in both compartments, comparments are split
        part 2: find the ite
        m that each elf team of 3 all have

    """
    backpacks = loadData('assignments/day3/data.txt')
    part1 = findAllPriorities(backpacks)
    part2 = findTeamBadges(backpacks)
    print("Day3 - Part1: " + str(part1))
    print("Day3 - Part2: " + str(part2))

