my_list = [1, 2, 3, 4, 5]
my_list2 = [1, 3, 5] + [7, 0]
my_list3 = list(my_list)
print(my_list)
print(my_list2)
print(my_list3)

# 인덱싱
m_list = [1, 2, 4]
m_list.append(6)
print(m_list)

del m_list[2]
print(m_list)

# 슬라이싱 (a 이상 b 미만)
print(my_list[0:2])
print(my_list[1:])
print(my_list[3:4])
print(my_list[-4:-2])
