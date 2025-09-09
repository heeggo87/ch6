# 키보드로 입력받기
# 모니터에 출력하기
# print: 화면에 숫자, 문자, 리스트 등을 출력하는 함수
# print 함수의 특징
print(123)
print('abc')
print([1,2,3])

print('hello' 'worild')
print('hello' + 'worild')
print('hello', 'worild') # 쉼표를 쓰면 공백이 들어감

print(1) # 1을 출력하고 줄바꿈
print(2)
print(3)

# print 함수의 선언부
# end는 기본값이 있는 매개변수 
# '\n'는 특수문자로 줄바꿈
# end 옵션은 앞에 value 를 출력하고, 마지막으로 \n 을 출력함
# print(value, end='\n')

# end 매개변수를 줄바꿈 대신 공백으로 바꾸기
print(1, end=' ')
print(2, end=' ')
print(3, end=' ') # 1 2 3

print(1, end=', ')
print(2, end=', ')
print(3, end=' ') # 1, 2, 3