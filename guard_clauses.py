# 처음부터 예외를 고려하여 동작 구현부에서 입력값에 대한 예외를 고려하지 않아도 됨
def calculate_average(numbers):
    if numbers is None:  # 값이 없으면 종료
        return None
    if not isinstance(numbers, list):  # numbers가 list가 아니면 종료
        return None
    if len(numbers) == 0:  # numbers 길이가 0이면 종료
        return None

    total = sum(numbers)
    average = total / len(numbers)
    return average


print(calculate_average(12345))  # list가 아니므로 None
print(calculate_average([1, 2, 3, 4, 5]))  # 3.0
