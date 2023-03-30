from Dice import DiceProbability
# 2개의 class를 사용하여 사용자로부터 입력 받은 횟수만큼 주사위를 굴리고
# 1-6 값이 나올 수 있는 확률을 구해서 화면에 출력

def main():
    # 객체 생성
    total = input("주사위를 몇번 굴리시나요?\n")
    dice = DiceProbability(int(total))
    # 생성된 객체에서 method를 사용
    dice.calcProbability(dice.total)
    dice.printProbability(dice.total)



if __name__ == "__main__":
    main()
