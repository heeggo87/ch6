# 반대로 파일의 내용을 읽어오기

# 읽기모드로 파일 열기
# 파일이름, 모드(w,r)
f = open('새파일.txt','r')

# 파일의 내용 읽어오기
# 읽기함수들 중에서 
# readlines 은 결과를 리스트로 반환
# 결과는 리스트로 저장됨
# lines = f.readlines()
# print(lines)

text =f.read()
print(text) 

# 문자열 안에 있는 알파벳을 하나씩 꺼내기
# 함수의 인자: 구분자
# split 함수는 공백을 기준으로
# 문자열을 쪼개고 결과를 리스트로 반환
lis = text.split(' ') # 공백
print(lis)

# 알파벳을 하나씩 출력하기
for ch in lis:
    print(ch)

# 사용이 끝났으면 닫기
f.close()

