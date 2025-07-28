'''
재귀함수 : 자기 자신을 다시 호출하는 함수 
재귀함수 사용시 종료조건을 명시해야됨 (아니면 무한호출됨)
'''

# 재귀함수 예시 
def recursive_function(i):
  if i == 10:
    return

  print(i, '번째 재귀함수에서', i+1, '번째 재귀함수를 호출')
  recursive_function(i+1)
  print(i, '번째 재귀함수를 종료함')

recursive_function(1)



# 팩토리얼 구현 예제 

# 반복문으로 구현한 팩토리얼 

def factorial_iterative(n):
  result = 1 
  for i in range(1, n+1):
    result *= i
  return result

print(factorial_iterative(5)) # 120 


# 재귀함수로 구현한 팩토리얼 
def factorial_recursive(n):
  if n <= 1:
    return 1
    
  return n*factorial_recursive(n-1)

print(factorial_recursive(5)) # 120 



# 최대공약수 
'''
유클리드 호제법 
두 자연수 A, B (A>B)에 대해 A 를 B로 나눈 나머지가 R이라고 할때 
A, B 의 최대공약수 = B, R의 최대공약수 

예를 들어, 192와 162의 최대공약수 
= 162 와 30(192/162의 나머지)의 최대공약수 
= 30 과 12(162/30의 나머지)의 최대공약수 
= 12와 6(30/12의 나머지)의 최대공약수 
마지막으로 12는 6의 배수 => 6이 최대공약수가 됨 
'''


def gcd(a, b):
  if a % b == 0 :
    return b
  else: 
    return gcd(b, a%b)

print(gcd(192, 162)) # 6
print(gcd(162, 192)) # 6
