# 파일을 쓰기 모드로 열기
f = open('new.txt', 'w')
f.write('hello world')
# f.close() -> with문은 파일을 자동으로 닫아주기때문에 생략가능

# with문 사용하기
# 위 코드를 간단하게 작성하기
with open('new.txt', 'w') as f:
    f.write('hello world')
