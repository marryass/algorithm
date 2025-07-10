"""
복잡도
시간 복잡도 : 수행 시간
공간 복잡도 : 메모리 사용량

빅오 표기법
• 가장 빠르게 증가하는 항만을 고려하는 표기법
• 함수의 상한만 표시

"""


# N 개의 데이터 합을 계산
# 시간 복잡도 : O(N)

array = [2,5,1,2,3]
summary = 0 

for x in array:  # 모든 데이터를 하나하나씩 넣음 (총 N번 반복)
  summary += x

print(summary)



# 이중 반복 문 
# 시간 복잡도 : O(N^2)
# for 문 내부에 다른 함수 호출시 함수의 시간 복잡도도 고려해야함 (항상 O(N^2) 아님)))
for i in array:
  for j in array:
    temp = i * j
    print(temp)   # i*j번 실행 (총 N*N번 반복)



"""
코테에서는 pypy가 python보다 빠름 
문제에서 시간제한(수행시간 요구사항)을 먼저 확인해야됨 
시간 복잡도에 맞게 짤 수 있는지 생각할 것 
"""

# 수행시간 측정 예제 
import time 
start_time = time.time() #시작 시간 

for _ in range(10): # 프로그램 실행 
  print("hello")

end_time = time.time() # 종료 시간
print("time : ", end_time - start_time)





