"""
11. 파이썬 문법 - 자주 사용되는 표준 라이브러리 

내장 함수 
itertools : 반복되는 데이터를 처리하는 기능 제공, 순열과 조합에서 자주 사용 (완전탐색에서)
heapq : 힙 자료구조 제공, 우선순위 큐 기능 구현에 사용 (최단경로알고리즘)
bisect : 이진 탐색 기능 제공
collections : 덱, 카운터 등 유용한 자료구조 포함
math : 필수적인 수학적 기능 제공, 팩토리얼, 제곱근, 최대공약수(GCD), 삼각함수 관련 함수부터 파이(pi) 같은 상수 포함


내장 함수 : sum, min, max, eval, sorted
"""

print(eval("(3+5)*7"))  # 56 문자열로 계산식을 입력받을 때 유용

print(sorted([9, 1, 8, 5, 4])) # [1, 4, 5, 8, 9] 오름차순 정렬
print(sorted([9, 1, 8, 5, 4], reverse=True)) # [9, 8, 5, 4, 1] 내림차순 정렬

# sorted with key 
array = [('홍길동', 35), ('이순신', 75), ('아무개', 50)]
result = sorted(array, key=lambda x: x[1]) # 점수 순으로 정렬
print(result) # [('홍길동', 35), ('아무개', 50), ('이순신', 75)]



""" 
itertools : 반복되는 데이터를 처리하는 기능 제공, 순열과 조합에서 자주 사용 (완전탐색에서)
"""
from itertools import permutations

data = ['A', 'B', 'C']
result = list(permutations(data, 2)) # 순열 
print(result) # [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]


from itertools import combinations

result = list(combinations(data, 2))  # 조합 
print(result) # [('A', 'B'), ('A', 'C'), ('B', 'C')]


# 중복 순열 
from itertools import product 

result = list(product(data, repeat=2)) # 중복 순열
print(result)

# 중복 조합 
from itertools import combinations_with_replacement
result = list(combinations_with_replacement(data, 2)) # 중복 조합
print(result)



"""
Counter: 리스트와 같은 반복 가능한 객체가 주어졌을 때, 해당 객체 내부의 원소가 몇 번씩 등장했는지 알려줌 (collections 라이브러리)
사전 자료형으로 변환가능 
"""

from collections import Counter

c = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(c['blue'])  # 3 
print(dict(c))  # {'red': 2, 'blue': 3, 'green': 1}
# 사전 자료형으로 변환가능 



"""
최대공약수와 최대공배수 (math 라이브러리)
"""

import math 

print(math.gcd(21, 14))  # 최대공약수 7

def lcm(a, b):
  return a*b // math.gcd(a, b)

print(lcm(21, 14))  # 최소공배수 42


