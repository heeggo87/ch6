# test.txt 파일을 만들고 다음과 같이 쓰세요
# 'hello'
# 'hi'
f = open('test.txt', 'w')

f.write('hello\n')
f.write('hi')


# score.txt 파일을 만들고 다음과 같이 쓰세요
# '80 90 70 100 60'
f = open('score.txt', 'w')
f.write('80 90 70 100 60')


# numbers.txt 파일을 만들고 다음과 같이 쓰세요
# 10
# 11
# ...
# 20
f = open('numbers.txt', 'w')

for i in range(10, 21):
    f.write(str(i) + '\n')

f.close()
        
