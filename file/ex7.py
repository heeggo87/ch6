# 파일 내용 읽어오기

# 파일이름, 모드
# 경로가 같을때는 파일 이름만 작성
# 파일에 한글이 있으면 인코딩 추가
f = open('file2.txt', 'r', encoding='utf-8')

# read 함수로 내용 읽어오기
# readlines 는 리스트로 반환
lis = f.readlines()

# 내용을 한줄씩 출력
for line in lis:
    print(line, end='') 


# file2.txt 의 새로운 내용 추가 : 11~20줄
# 내용추가 -> 쓰기모드 (w 또는 a)
# 'w' 모드는 기존의 내용을 덮어씌움 -> write 모드
# 'a' 모드는 이전 내용 뒤에 추가됨 -> append 모드
f = open('file2.txt', 'a', encoding='utf-8')

for i in range(11, 21):
    f.write(f'{i}번째 줄입니다\n')

f.close()