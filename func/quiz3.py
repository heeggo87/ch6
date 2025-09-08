# 값을 하나 입력받아 타입이 str이면 '문자입니다'를 출력
# 타입이 str 이 아니면 아무것도 출력되지 않습니다

def string(value):
    if isinstance(value, str):
        print("문자입니다")

string("안녕하세요")
string(123)


# 값을 하나 입력받아 0보다 크면 '양수입니다'를 출력

def check(num):
    if num > 0:
        print('양수입니다')

check(5)


# 리스트를 입력받아 첫번째 값을 반환하는 함수

def first(lis):
        return lis[0]

result = first([10,20,30])
print(result)


# 문자열을 입력받아 길이를 반환하는 함수

def length(str):
        return len(str)
    
result = length('안녕하세요')
print(result)














