# 나머지 매개변수를 사용하여 입력받은 과일의 이름만 출력하세요

def calc(**kwargs):
    for key in kwargs:
        print(key) # apple banana orange

calc(apple=1200, banana=800, orange=1500)




# 나머지 매개변수를 사용하여 입력받은 학생의 점수만 출력하세요

# dic 에서 vlaue 꺼내기
dic = {'철수':90, '영희':85, '민수':100}
print(dic.values()) # dict_values([90, 85, 100])
print(dic.items()) # dict_items([('철수', 90), ('영희', 85), ('민수', 100)])

def show_scores(**kwargs):
    for v in kwargs.values():
        print(v) # 90 85 100

show_scores(철수=90, 영희=85, 민수=100)



# 나머지 매개변수를 사용하여 입력받은 도시 이름과 인구 수를 모두 출력하세요
# 인구 수는 만명 단위로

def show_population(**kwargs):
    for key, value in kwargs.items():
        print(key, value) # seoul 950 busan 340 incheon 300

show_population(seoul=950, busan=340, incheon=300)

print(dic.keys())
print(dic.values())
print(dic.items())



# 나머지 매개변수를 사용하여 입력받은 상품의 상품명만 출력하세요
def show_items(**kwargs):
    for key in kwargs.keys():
        print(key)
    # for key in kwargs:
    #     print(key) # 코드는 다르나 동일한 결과로 출력됨

show_items(milk=2500, bread=2000, egg=3000)












