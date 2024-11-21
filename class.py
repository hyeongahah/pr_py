# 사칙 연산
class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def mul(self):
        result = self.first + self.second
        return result

    def sub(self):
        result = self.first + self.second
        return result

    def div(self):
        result = self.first + self.second
        return result


# 클래스 상속
class MoreFourCal(FourCal):
    def pow(self):
        result = self.first**self.second
        return result


# a = MoreFourCal(2, 3)
# print(a.pow())


class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second


# a = SafeFourCal(4, 0)
# print(a.div())

# 클래스 변수는 객체 변수와 달리 클래스로 만든 모든 객체에 공유된다
# 객체변수는 클래스변수와 동일한 이름으로 생성할 수 있다
