valid_operators = ["+", "-", "*", "/"]
operator = "/"
divisor = 0
if operator in valid_operators and (operator == "/" and divisor == 0):
    print("0으로 나눌 수 없어 연산이 가능하지 않습니다.")

if operator in valid_operators:
    if operator == "/" and divisor == 0:
        print("0으로 나눌 수 없어 연산이 가능하지 않습니다.")

# 파이썬에는 switch, case 선택문이 없음
