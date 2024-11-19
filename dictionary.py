# key와 value로 구성됨
my_dict = {}

my_dict["apple"] = 1
my_dict["banana"] = 2
my_dict["orange"] = 3
print(my_dict)

# 	딕셔너리 검색
key = "apple"
if key in my_dict:
    value = my_dict[key]
    print(f"{key} : {value}")
else:
    print(f"{key}는 딕셔너리 존재하지 않습니다")

# 딕셔너리 수정
my_dict["banana"] = 4
print(my_dict)

# 딕셔너리 삭제
del my_dict["orange"]
print(my_dict)

# 키를 찾아서 삭제하므로 키가 없는 경우에는 예외 처리를 해줘야 한다.
m_dict = {"apple": 1, "banana": 2, "orange": 3}
key = "kiwi"
if key in my_dict:
    print(f"값: {m_dict[key]}")
else:
    print(f"'{key}' 키가 딕셔너리에 없습니다.")
