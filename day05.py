# 사용자로부터 문자열을 입력받는 코드를 작성하세요.

# 입력받은 문자열이 팰린드롬인지 여부를 판별하는 함수를 작성하세요.

# 판별 결과를 출력하는 코드를 작성하세요.

def is_P(str):
    str = str.lower()
    str2 = str[-1::-1]
    if str == str2 :
        return True
    else :
        return False

while True :
    str = input("input String ... ")
    print(is_P(str))



