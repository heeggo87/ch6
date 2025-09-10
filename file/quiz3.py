# score.txt 파일을 읽고 합계와 평균을 구하세요

f = open('score.txt', 'r') 
text =f.read() 

scores = text.split()
print(scores) # ['80', '90', '70', '100', '60']

sum = 0
for s in scores:
    sum += int(s)
    print(s) # 80 90 70 100 60

print(sum) # 400

a = len(scores) # len: 요소 개수 반환하는 함수
print(a) # 5

avg = sum / len(scores) # 400 / 5 = 80.0

print('합계:', sum)
print('평균:', int(avg)) # 80 -> 정수로 반환

f.close()





# numbers.txt 파일을 읽고 짝수만 출력하세요

f = open("numbers.txt", "r")
lis = f.readlines()

for line in lis:
    # print(type(line)) # str
    if int(line) % 2 == 0:
        print(line, end='')

f.close() 


    





