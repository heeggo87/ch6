# 더하기 함수
def add(a, b):
    return a + b

result = add(3, 4)
print(result)

# 익명(람다) 함수
# 함수를 짧게 만들 때 사용

# 변수 = lambda 매개변수: 반환값
add = lambda a, b: a + b

# 람다 함수 호출
result = add(3, 4)
print(result)


# 문자열 정렬
# sort: 목록을 순차적으로 정렬하는 함수
strings = ["foo", "card", "ba", "aaa"]

# sort 함수의 입력값으로 함수 입력
# 문자의 크기를 비교하는 함수
# 변수 = lambda 매개변수: 반환값

strings.sort(key = lambda x : len(x))

print(strings)

