
def loadData(name):
    lines = []
    file = open(name, "r")
    for line in file:
        if line == '\n':
            print('blep')
        else:
            lines.append(line.replace('\n',''))
    return lines

def scoreOfPlay(play):
    moves = play.split(' ')
    possibleMoves = {
      "A": "rock",
      "B": "paper",
      "C": "scissors",
      "X": "rock",
      "Y": "paper",
      "Z": "scissors"
    }
    scoreOwnMove = {
      "X": 1,
      "Y": 2,
      "Z": 3
    }
    if possibleMoves[moves[0]] == possibleMoves[moves[1]]:
        return 3 + scoreOwnMove[moves[1]]
    elif play == 'A Y' or play == 'B Z' or play == 'C X':
        return 6 + scoreOwnMove[moves[1]]
    else:
        return scoreOwnMove[moves[1]]

def scoreOfPlay2(play):
    moves = play.split(' ')
    opponentMoves = {
      "A": "rock",
      "B": "paper",
      "C": "scissors"
    }
    possibleMoves = ["rock", "paper", "scissors"]
    scoreOwnMove = {
      "rock": 1,
      "paper": 2,
      "scissors": 3
    }
    if moves[1] == 'Y':
        return 3 + scoreOwnMove[opponentMoves[moves[0]]]
    elif moves[1] == 'Z':
        index = possibleMoves.index(opponentMoves[moves[0]]) + 1
        if index > 2:
            index = 0
        return 6 + scoreOwnMove[possibleMoves[index]]
    else:
        index = possibleMoves.index(opponentMoves[moves[0]]) - 1
        if index < 0:
            index = 2
        return 0 + scoreOwnMove[possibleMoves[index]]

def calculateScore(strategyGuide, calculateFunction):
    totalScore = 0
    for play in strategyGuide:
        score = calculateFunction(play)
        totalScore = totalScore + score
    return totalScore

def day2():
    """
        Assignment day2:
        We get a strategy guide for rockpaperscissors and need to calculate score
        Part1: Your move XYZ is rockpaperscissors
        Part2: XYZ means draw/lose/win
        rock = 1, paper = 2, scissors = 3
        win = 6, draw = 3, lose = 0
    """
    part1 = calculateScore(strategyGuide, scoreOfPlay)
    part2 = calculateScore(strategyGuide, scoreOfPlay2)
    print("Day1 - Part1: " + str(part1))
    print("Day1 - Part2: " + str(part2))

