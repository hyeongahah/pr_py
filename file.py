user_input = input("저장할 내용을 입력하세요")
f = open("test.txt", "a")  # 모드에 추가는 a, 읽기는 r, 쓰기는 w를 입력한다.
f.write("\n")
f.write(user_input)
f.write("\n")
f.close

# f = open("test.txt", "r")
# r = f.read()
# print(r)
