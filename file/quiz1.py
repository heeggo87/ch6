# 두 숫자를 입력받아 곱셈 결과 출력
n1 = input('첫번째 숫자를 입력하세요: ')
n2 = input('두번째 숫자를 입력하세요: ')

multi = int(n1) * int(n2)
print('결과: ', multi)


# 사용자로부터 이름과 나이를 입력받아 자기소개 출력
name = input('이름을 입력하세요: ')
age = input('나이를 입력하세요: ')

print(f'{name} 님의 나이는 {age}살 입니다')



# 사과 가격과 수량을 입력받아 총 가격 계산
price = input('사과 가격을 입력하세요(단위: 원): ')
quantity = input('사과 수량을 입력하세요: ')

total = int(price) * int(quantity)
print(f'총 가격은 {total}원 입니다.')



# 시험 점수를 입력받아 합격 여부 출력
# 60점 이상: 합격
# 60점 미만: 불합격
def check():
    yeobu = int(input('시험 점수를 입력하세요: '))
    if yeobu >= 60:
        print('합격')
    else:
        print('불합격')

check()



# 학생의 나이를 입력받아 버스요금 계산
# 어린이(0~12세): 1000원
# 청소년(13~18세): 1500원
# 성인(19세 이상): 2000원
def bus_fare():
    age = input('학생의 나이를 입력하세요: ')
    if int(age) <= 12:
        print('1000원')
    elif int(age) <= 18:
        print('1500원')
    else:
        print('2000원')

bus_fare()



# 문자를 계속 입력 받다가 0이 들어오면 종료하세요
# 반복문 필요
# 예) 'aaa' -> 계속
# 예) '0' -> 종료

while True: # '참' 이면 무한반복
    str = input('문자를 입력하세요: ')
    if str == '0':
        print('종료')
        break # 즉시 반복문 종료










