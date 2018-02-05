'''
模拟游戏
输入：A、B获胜的概率；模拟的次数
输出：A、B分别获胜的次数
'''
from random import * 
# import random   # random.random() = random()
def printIntro():
    print("This program simulates a game between two.")
    print("There are two players, A and B")
    print("Problility(a number between 0 and 1) is used")

def getInputs():
    a = eval(input("What is the prob.players A wins?"))
    b = eval(input("What is the prob.players B wins?"))
    n = eval(input("How many games to simulates?"))
    return a, b, n

def simOneGame(probA, probB):
    scoreA = 0
    scoreB = 0
    serving = "A"   # 当前发球权
    while not gameOver(scoreA, scoreB): # 谁先获得15分结束
        if serving == "A":  # A发球
            if random() < probA:
                scoreA += 1
            else:
                serving = "B"
        else:               # B发球
            if random() < probB:
                scoreB += 1
            else:
                serving = "A"
    return scoreA, scoreB

def simNGames(n, probA, probB):
    winsA = 0
    winsB = 0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB:
            winsA += 1
        else:
            winsB += 1
    return winsA, winsB

def gameOver(a, b):
    return a == 15 or b == 15

def printSummary(winsA, winsB):
    n = winsA + winsB
    print("\nGames simulated:%d"%n)
    print("Wins for A:{0}({1:0.1%})".format(winsA, winsA/n))
    print("Wins for B:{0}({1:0.1%})".format(winsB, winsB/n))


def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB)

if __name__ == '__main__':
    main()