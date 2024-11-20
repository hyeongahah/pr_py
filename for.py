for _ in range(
    5
):  # for 반복문 안에서 사용할 반복 제어 변수가 없으면 밑줄을 변수로 대신 사용
    print("처리할 문장")

sum1 = 0
for i in range(10):
    print(i + 1)
    sum1 = sum1 + (i + 1)
print("1부터 10까지의 합은", sum)


# range(1, 11, 2) 시작 값 1, 종료 값 11, 증가값 2
print(sum(range(1, 11, 2)))

# for 중복 반복문의 경우 안쪽에 있는 반복문이 바깥쪽에 있는 반복의 횟수만큼 반복하여 수행된다
for i in range(2, 5, 2):
    for j in range(1, 4):
        print(i, "x", j, "=", i * j)
