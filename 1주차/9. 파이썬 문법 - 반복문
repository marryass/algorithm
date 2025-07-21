"""
9. 파이썬 문법 - 반복문 
while, for 문// 코테에서는 주로 for문 사용 
"""


# while 문 

i = 1
result = 0 

while i<= 9:
  result += i
  i += 1

print(result)  # 45 (1+2+3+4+5+6+7+8+9)


#1 부터 9까지 홀수의 합 구하기 
i = 1
result = 0 

while i <= 9:
  if i % 2 == 1:
    result += i
  i += 1

print(result)  # 25 (1+3+5+7+9)


# for 문 : 리스트, 튜플, 문자열, 딕셔너리 등 순회 가능
a = [1,2,3,4,5,6,7,8,9]
for i in a: 
  print(i)

a = set(a)
print(a)  # {1, 2, 3, 4, 5, 6, 7, 8, 9}
for i in a: 
  print(i)


a = tuple(a)
print(a) # (1, 2, 3, 4, 5, 6, 7, 8, 9)
for i in a:
  print(i)
  
# range() 함수 : range(시작값, 끝값+1)

result = 0 
for i in range(1, 10):
  print(i)  # 1~9 까지 출력 
  result += i

print(result)  # 45 (1+2+3+4+5+6+7+8+9)

"""
continue : 다음 반복문으로 넘어감
"""

result = 0 

for i in range(1, 10):  # i 는 1부터 9까지 
  if i % 2 == 0:  # i가 짝수일때 다음 반복문으로 넘어감 (뒤에 코드 실행 X)
    continue
  result += i

print(result)  # 25 (1+3+5+7+9)



"""
break : 반복문 종료
"""

i = 1 

while True:
  print("현재 i의 값 : ", i)
  if i == 5:
    break
  i += 1


# 특정 번호의 학생 (2,4)는 제외하고 학생들의 합격여부 판단하기 
score = [90, 85, 77, 65, 97]
std_list = {2,4}

for i in range(len(score)): # range(5) : 0~4
  if i+1 in std_list:
    continue
  if score[i] >= 80:  # 80점 이상일때 합격
    print(i+1, "번 학생은 합격입니다.")
  


# 구구단 (중첩된 반복문)
for i in range(2, 10): # 2~9
  for j in range(1, 10): # 1~9
    print(i, "X", j, "=", i*j)

