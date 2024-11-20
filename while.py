i = 0
while i < 3:
    print(i)
    i += 1

# 지수 계산
import math

error = 100
magin = 0.001
x = 3
old_exp_x = 1
i = 1
while error > magin:
    exp_x = old_exp_x + 1 / math.factorial(i) * x**i
    error = abs(exp_x - old_exp_x)
    old_exp_x = exp_x
    i += 1
print(f"무한 급수를 {i}번 반복하여 찾아낸 exp(3) = {exp_x}")
print(f"급수간 오차는 {error}입니다")
