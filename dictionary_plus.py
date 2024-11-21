# 딕셔너리는 순서가 없는 자료형이므로 인덱싱을 지원하지 않는다
dic = {1: "a"}
dic[2] = "b"
print(dic)

# key에 튜플은 쓸 수 있어도, 리스트는 쓸 수 없다.
dic["3"] = "apple"
print(dic)  # {1: 'a', 2: 'b', '3': 'apple'}

print(dic[1])


key = dic.keys()  # 키만 리스트로
print(key)
val = dic.values()  #  벨류만 리스트로
print(val)

item = dic.items()
print(item)

print(dic.get(1))  # key로 value 얻기

print("3" in dic)  # 값이 존재하는지 확인
