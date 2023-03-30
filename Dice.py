import random

class Dice:
    # #roll() 함수 만들어서 1-6 사이의 정수를 무작위로 생성하고 반환 -- ok
    # #필요한 데이터가 있으면 멤버 변수로 추가
    # def __init__(self, dice, person):
    #     self.dice = dice
    #     self.person = person #주사위를 던지는 사람 수

    def roll(self):
        return random.randint(1,6)



class DiceProbability:
    #생성자는 주사위를 던질 횟수(n번)을 인자로 받음
    #N번의 주사위 숫자를 저장할 수 있는 배열(a)를 멤버 변수로 포함
    #6개 주사위 숫자가 나오는 확률을 저장할 수 있는 배열 (b)를 멤버 변수로 포함
    #Dice clas의 roll()함수를 호출하여 주사위를 N번 굴리고 배열 a에 주사위 값 저장
    #calcProbability() 함수 : 각 번호별 확률을 계산해 배열 b에 저장
    #printProbability() 함수 : 1~6 주사위 값이 나타날 수 있는 확률을 화면에 출력
    # __init__() 함수 : 멤버 변수 초기화
    def __init__(self, n):
        self.total = n  # 총 roll 횟수
        self.dice = Dice()
        self.num = []  # roll 결과(주사위 눈 수)
        self.rate = [0, 0, 0, 0, 0, 0]  # 각 눈의 roll 확률

    def calcProbability(self, n):
        for i in range(n):
            self.num.append(self.dice.roll())  # n번 roll하여 n번의 결과(주사위 눈 수) 저장
        for i in range(6):
            self.rate[i] = round(100 * self.num.count(i + 1) / self.total, 3)  # 각 눈의 roll 확률 계산

    def printProbability(self, n):
        print("-----------------------------")
        for i in range(6):
            print("주사위" + str(i + 1) + ": " + str(self.num.count(i + 1)) + "번   비율: " + str(self.rate[i]) + "%")
        print("총 횟수: " + str(n) + "번")
        print("-----------------------------")
