# 두 수의 차를 구하는 함수 정의
# 매개변수: 함수에 필요한 입력값. 숫자 두개
# 반환값: 두 수의 차를 구해서 결과를 반환
def sub(n1, n2):
   return n1 - n2

# 함수 호출
# 함수이름(함수에 필요한 값 입력)
# 함수를 호출하는 쪽에서 결과를 받고 확인할 것
# 인자를 순서대로 입력 (n1, n2)
result = sub(7, 3) 
print(result) # 4

# 인자를 순서와 상관없이 입력
# 매개변수의 이름을 직접 지정
result = sub(n2=3, n1=7)
print(result) # 4


# 문자열 두개를 입력받아 연결하는 함수 정의
def add_text(str1, str2):
#    print(str1 + str2)
#    print(str1, str2)
   print(f'{str1} {str2}')

# 함수 호출
# 매개변수를 순서대로 입력 (str1, str2)
add_text('hello', 'world')

# 매개변수 이름을 지정하여 입력
add_text(str2='world', str1='hello')


