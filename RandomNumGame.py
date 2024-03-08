import random as ran
answer = ran.randint(1, 20)
print("answer = %d" % answer)
i = 4
while True:
    if i == 0:
        print("아쉽습니다. 정답은 %d입니다." % answer)
        break
    num = int(input("기회가 %d번 남았습니다. 1-20 사이의 숫자를 맞혀보세요: " % i))
    if num == answer:
        print("축하합니다. %d번 만에 숫자를 맞히셨습니다." % (4-i+1))
        break
    elif num > answer:
        print("Down")
        i = i - 1
        continue
    else:
        print("UP")
        i = i - 1
        continue







