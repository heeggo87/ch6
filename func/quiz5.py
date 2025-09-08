# 단을 입력받아 구구단을 출력하는 함수를 만드세요
def gugudan(dan):
    for i in range(1, 10):
        print(f"{dan} x {i} = {dan * i}")

gugudan(7)



def gugudan_all():
    for dan in range(2, 10):      # 2단부터 9단까지
        # print(f"--- {dan}단 ---")
        for i in range(1, 10):    # 1부터 9까지 곱하기
            print(f"{dan} x {i} = {dan * i}")
        print()  # 단 구분을 위해 줄바꿈

# 함수 실행
gugudan_all()



# 리스트를 입력받아 그 안에 문자열(str) 자료형이 몇 개인지 세는 함수를 만드세요
def func(lis):
    for item in lis:
        if type(item) == str:
            print(item, ':문자')


# def func(lis):
#     cnt = 0
#     for item in lis:
#         if type(item) == str:
#             cnt += 1
#     return cnt


func([1, "apple", 3.5, "banana", 10, "hi"])
func(["a", "b", "c"])
func([1, 2, 3]) 