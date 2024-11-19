# def function_name(param1, param2, param3, ..., paramN):
# 	# 함수의 실행코드
# 	return result # 반환값


def add(num1, num2):
    result = num1 + num2
    return result


ret = add(5, 10)
print(ret)

# 람다식(함수를 간단하게 표현하는 방법, 익명 함수를 만드는 데 사용)

# 변수로 참조하는 방법
add_lamb = lambda x, y: x + y
print(add_lamb(5, 4))

# 인수로 람다식을 넘기는 방법
num = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, num))  # map() 함수에 람다식을 넘기기
print(squares)
