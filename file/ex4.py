# 파일 쓰기 모드로 열기

f = open('file1.txt', 'w')

for n in range(1, 11):
    f.write(f'{n}\n')

f.close()



# 파일 쓰기 모드로 열기

# 한글 입력시 깨짐발생으로 인코딩 설정해야함
f = open('file2.txt', 'w', encoding='utf-8') # 인코딩 추가

for i in range(1, 11):
    f.write(f'{i}번째 줄입니다\n') 

f.close()


