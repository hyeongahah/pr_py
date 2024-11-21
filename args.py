def avg_number(*args):
    # 매개변수에 *args를 붙이면 입력 개수가 제한되지 않는다. 인자들을 튜플의 형태로 처리한다.
    # 다른 매개 변수를 함께 사용할 시, 마지막에 입력해야 한다.
    result = 0
    for i in args:
        result += i
    return result / len(args)


print(avg_number(3, 4, 5, 6))

# 매개변수에 **kwargs를 입력할 경우, 인자들을 딕셔너리 형태로 처리한다.

# 모두를 혼합할 경우, Positional Argument가 제일 먼저 위치해야하고 그 다음에 Keyword Argument, *args, **kwargs 순으로 인자를 받아야한다. (ex : age, name='홍길동', *args, **kwargs)
