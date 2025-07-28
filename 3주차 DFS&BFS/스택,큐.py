'''
스택 : 선입후출 자료구조 
먼저 들어간 데이터가 나중에 나감 (입구와 출구가 동일한 형태)
'''

# 스택 구현 예제 

# 삽입(5) - 삽입(2) - 삽입(3) - 삭제() - 삽입(1) - 삽입(4) - 삭제() 
stack = []
stack.append(5)  # [5]
stack.append(2)  # [5,2]
stack.append(3)  # [5,2,3]
stack.pop()      # [5,2]
stack.append(1)  # [5,2,1]
stack.append(4)  # [5,2,1,4]
stack.pop()      # [5,2,1]

print(stack)     # [5,2,1]
print(stack[::-1])  # 최상단 원소부터 출력 [1,2,5]




'''
큐 : 선입선출 자료구조 
먼저 들어간 데이터가 먼저 나감 (입구와 출구가 모두 뚫려 있는 터널과 같은 형태)
'''

# 큐 구현 예제

# 삽입(5) - 삽입(2) - 삽입(3) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
from collections import deque

queue = deque()

queue.append(5) # [5]
queue.append(2) # [5,2]
queue.append(3) # [5,2,3]
queue.popleft() # [2,3]
queue.append(1) # [2,3,1]
queue.append(4) # [2,3,1,4]
queue.popleft() # [3,1,4]

print(queue) # [3,1,4]
queue.reverse()
print(queue) # [4,1,3]

