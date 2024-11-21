num = [1, 5, 282, 3, 2, 1]
num.sort()  # 정렬하기
print(num)
num.reverse()  # 역순
print(num)

num.append(7)
print(num)
print(num.index(2))  # 위칫값 리턴

num.insert(2, 99)  # [2] 위치에 99 삽입
print(num)

num.remove(1)  # 리스트에서 첫 번째로 나오는 value 삭제
print(num)

print(num.pop(1))  # x번째 요소를 리턴하고, 그 요소는 리스트에서 삭제

num.extend([3, 4, 4, 5])  # 리스트에 리스트를 추가

print(num)

a = [1, 2, 3]
a += [2, 3]  # 리스트에 리스트를 추가하는 다른 방법
print(a)
del a[0]  # x 번째 요소를 삭제, pop과 달리 리턴하는 값이 없다
print(a)

# 튜플은 수정과 삭제가 안 될 뿐, 함수는 리스트와 동일
