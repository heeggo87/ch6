# 함수 만들기
# 문자를 입력 받고 나쁜 말이 들어오면 종료하는 함수
def say_nick(nick): # 매개변수는 별명
   if nick == '바보':
      return 
   print(f'나의 별명은 {nick}입니다') # 나의 별명은 짱구입니다

# 함수 호출
say_nick('짱구')
say_nick('바보') # 나쁜말을 입력하면 강제 종료

# return 
# 더이상 코드를 실행하지 않고 함수 종료
# return 키워드 뒤에 값 생략 가능
# 값이 return 만 있으면 함수만 종료
# 특정한 조건에서 함수를 강제로 종료할 때 사용



# 함수 만들기
def func():
   a = 1
   b = 2
   c = 3
   return a, b, c

# 반환값은 무조건 1개
# 한번에 abc 를 반환하면 어떻게 될까?
# return 에 값을 여러개 쓰면 tuple 로 묶어서 반환됨
print(func()) # (1, 2, 3)