# 문자열은 이뷰터블 객체이므로 기존 객체를 수정하는 것이 아니라 새로운 객체를 반환한다
string = "he"
string += "llo"
print(string)

# 문자열 수정
strings = "hello"
strings = string.replace(
    "l", ""
)  # 첫 번째는 찾을 문자열, 두 번째는 변경할 문자열을 입력
print(strings)
