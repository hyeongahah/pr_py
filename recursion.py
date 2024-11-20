def add_to_10(i):
    if i == 10:  # 기저 사례 : 재귀 호출을 멈추는 조건
        return i
    # return i + add_to_10(i + 1)  # 재귀 사례 : i가 10보다 커질 때까지 반복
    sum = i + add_to_10(i + 1)  # 반환값을 변수에 저장해서 디버깅하기 쉽게 한다
    return sum


sum = add_to_10(1)
print(f"1부터 10까지 더한 합은 {sum}입니다.")
