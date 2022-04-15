import random
import time

# 단어 리시트: 여기에 단어를 추가하면 문제에 나옵니다.
w = ["고양이", "수박", "포도", "멜론", "참외", "청포도", "사과", "바나나", "복숭아"]

n = 1
print("[타자 게임] 준비되면 엔터!")
input()
start = time.time()

q = random.choice(w)
while n <= 9:
    print("* 문제", n)
    print(q)
    x = input()
    if q == x:
        print("통과")
        n = n + 1
        q = random.choice(w)
    else:
        print("오타! 다시 쓰세요")
end = time.time()
et = end - start
et = format(et, ".2f")
print("타자 시간 : ", et, "초")
