"""
10. 파이썬 문법 - 함수와 람다 표현식 

내장함수 : 이미 있는 함수 (print, input, len 등)
사용자정의함수 

"""


# 더하기 함수 (사용자 정의)
def add(a, b):  # 매개변수 : a, b
  return a + b  # 반환값 

print(add(3, 7)) # 10 

result = add(5, 7)
print(result) # 12

result = add(b = 5, a = 3) # 파라미터 지정하기 
print(result)  # 8 


"""
global 키워드 : 지역변수를 전역변수로 만들기
지역변수를 만들지 않고, 함수바깥에 선언된 전역변수를 바로 참조함 
"""


a = 0 
def func():
  global a   # 전역변수에 10 더하기
  a += 10

print(a)  # 0 
func()  # 함수 실행 (전역변수 a에 10 더하기)
print(a)  # 10 


a = 0 
def func():  
  a += 50  # 함수 내에 지역변수 a를 먼저 선언해줘야됨 (a = 0)  아니면 오류남 


# print(a)
# func()
# print(a)   # 오류발생 : 지역변수 a가 선언되지 않았기 때문




# 리스트는 함수 내부에서 지역변수 설정 안해도 됨 (오류 없음)
a = [1,2,3,4]

def func():
  a.append(10)

print(a)  # [1,2,3,4]
func()
print(a) # [1,2,3,4,10]



a = [1,1,1]

def func():
  a = []
  a.append(10)
  print(a)    

print(a)  # [1,1,1] (위에서 선언한 전역변수 리스트 )
func()  # [10] (함수 내부에서 선언한 지역변수 리스트 )
print(a)  # [1,1,1] (func()함수를 실행해도 전역변수 리스트는 변하지 않음)




"""
 람다 표현식 
 특정한 기능을 수행하는 함수를 한 줄에 작성할 수 있음

 함수자체를 입력으로 받는 함수에서 유용하게 사용 (map 등))

"""

print((lambda a, b: a + b)(3, 6))   # 9 
# (lambda   ) 자체가 함수로서 작용 


a = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]

print(sorted(a, key=lambda x: x[1])) # 두번째 원소를 기준으로 정렬 



list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

result = map(lambda a, b: a + b, list1, list2)
print(list(result))



