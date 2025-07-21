"""
7. 파이썬 문법 - 기본 입출력 
input() : 한 줄의 문자열을 입력받는 함수
map() : 리스트의 모든 원소에 각각 특정한 함수를 적용할 때 사용

ex) list(map(int, input().split())) : 공백을 기준으로 구분하여 (input().split()) 각각 숫자 자료형으로 적용
"""


# n = int(input("숫자를 입력하세요 : "))
# print(n)

# # 공백을 기준으로 문자열을 입력받고, 리스트로 저장
# data = input("문자열을 입력 : ").split()  
# print(data)


# # 공백을 기준으로 숫자를 입력받고, 리스트로 저장
# data = list(map(int, input("숫자를 입력 : ").split())) 
# print(data)


"""
입력 빠르게 받기 : sys 라이브러리의 sys.stdin.readline() 함수 이용
입력 후 엔터가 줄 바꿈 기호로 입력되므로 rstrip() 메서드를 함께 사용
"""
import sys 

# data = sys.stdin.readline().rstrip()
# print(data)

"""
print() 
출력 후 줄바꿈을 원치 않는 경우 end 속성 이용

"""
a = 7
b = 3
print(a, b)  # 7 3  / 띄어쓰기로 구분해서 출력 

print(a, b, end=' ')  # 7 3  / 출력후 줄바꿈 안함 
print(a, b, sep=',') # 7,3 / ,로 구분해서 출력


"""
f-string
f-string을 이용하면 변수를 문자열 안에 넣을 수 있음

"""  
a = 7 
print(f"정답은 {a}")  # 정답은 7 
