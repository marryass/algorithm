"""
6. 파이썬 문법 - 사전, 집합 자료형 
키, 값(value)의 쌍으로 갖는 자료형 
키로는 변경 불가능한 자료형이 가능 

"""

# 사전 자료형 선언 
data = dict()

data['사과'] = 'Apple'
data['바나나'] = 'Banana'

print(data)


"""
keys() : 키 데이터만 뽑아서 리스트로 이용할 때
values() : 값 데이터만 뽑아서 리스트로 이용할 때
"""

print(data.keys())
print(data.values())


for key in data.keys(): # key: data딕셔너리의 key값 
  print(data[key])  # 각 key에 해당하는 value값 출력



"""
집합 자료형 
중복 허용 X, 순서없음 

리스트 또는 문자열에 set()  함수를 이용하여 집합을 만듬 
{} 로 집합을 만듬

"""


data = set([1,2,4,4,5])
print(data)  # {1,2,4,5}  중복 허용 X 

data = {1,3,2,2,2,2,2,4}
print(data)  # {1,2,3,4}  중복 허용 X


"""
집합 자료형의 연산 
: 합집합, 교집합, 차집합 
"""


# 원소 추가 
data = {1,2,3,4} 

data.add(5)
print(data) # {1,2,3,4,5}

# 원소 여러개 추가
data.update([6,7])
print(data) # {1,2,3,4,5,6,7}

# 특정 값을 갖는 원소 삭제
data.remove(3)  # data 집합에서 3 삭제 
print(data) # {1,2,4,5,6,7}

"""
사전 자료형과 집합은 순서가 없기 때문에 인덱싱으로 값을 얻을 수 없음 
"""


