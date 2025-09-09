# 변수
# scope

a = 1 # 밖에 있으면 전역변수

def func(a): # 안에 있으면 지역변수
    a += 1

func(a)
print(a)


def func(b):
    b = 3
    print(b)

# 함수 밖에서 b 사용하기
print(b)


