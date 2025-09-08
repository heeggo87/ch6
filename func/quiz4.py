# 숫자를 입력받아 양수/음수/0 을 판별하는 함수를 만드시오

def func(num):
    if num > 0:
        print('양수')
    elif num < 0:
        print('음수')
    else:
        print("0")

func(7)


# 리스트를 입력받아 리스트안의 숫자를 모두 더해 합을 반환하는 함수만들기
# def sum_list(numbers):
#     return sum(numbers)

# print(sum_list([10, 20, 30]))

def func(lis):
    hap = 0
    for n in lis:
        hap += n

    return hap

result1 = func([1,2,3,4,5])
print(result1)
result2 = func([10,20,30])
print(result2)

 






