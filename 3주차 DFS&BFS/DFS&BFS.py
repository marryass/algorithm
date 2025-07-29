'''
DFS : 깊이 우선 탐색, 그래프에서 깊은 부분을 우선적으로 탐색 
스택 / 재귀함수 이용 

동작과정 
1. 탐색 시작 노드를 스택에 삽입하고 방문처리 (방문 기준: 번호가 낮은 인접 노드부터)
2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문 처리. 방문하지 않은 인접노드가 없으면 스택에서 최상단 노드를 꺼냄 
3. 더이상 2번의 과정을 수행할 수 없을 때까지 반복 
'''

def dfs(graph, v, visited):
  visited[v] = True
  print(v, end=' ')

  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)



graph = [
  [],    # 0 번 노드는 비워둠 
  [2,3,8],
  [1,7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
]

visited = [False] * 9  # 8개의 노드지만 0번 포함해서 9개 만들어줌


dfs(graph, 1, visited) # 1 2 7 6 8 3 4 5
print(visited) # [False, True, True,... True] # 0번 노드만 False





'''
BFS : 너비 우선 탐색, 그래프에서 가까운 노드부터 우석적으로 탐색 
큐 자료구조 이용 


'''

from collections import deque

def bfs(graph, start, visited):
  queue = deque([start])
  visited[start] = True

  while queue:
    v = queue.popleft()
    print(v, end=' ')

    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True




      

graph = [
  [],    # 0 번 노드는 비워둠 
  [2,3,8],
  [1,7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
]

visited = [False] * 9  # 8개의 노드지만 0번 포함해서 9개 만들어줌


bfs(graph, 1, visited) # 1 2 3 8 7 4 5 6


print()
# -------------------------------------------------------------
# 문제 : 음료수 얼려 먹기 => DFS로 풀기 
print()
print('문제 : 음료수 얼려 먹기')

'''
N x M 크기의 얼음 틀이 있습니다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시됩니다. 구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주합니다.
이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하세요.


입력조건 
첫 번째 줄에 얼음 틀의 세로 길이 N과 가로 길이 M이 주어집니다. (1 <= N, M <= 1,000)
두 번째 줄부터 N + 1번째 줄까지 얼음 틀의 형태가 주어집니다.
이때 구멍이 뚫려있는 부분은 0, 그렇지 않은 부분은 1입니다.

출력조건 
한 번에 만들 수 있는 아이스크림의 개수를 출력합니다.

'''

def dfs(x, y):
  if x <= -1 or x >= n or y <= -1 or y>= m:
    return False 

  if graph[x][y] == 0:
    graph[x][y] = 1

    dfs(x-1, y)
    dfs(x, y-1)
    dfs(x+1, y)
    dfs(x, y+1)
    return True
    
  return False
    




# n, m = map(int, input().split())
n, m = 4, 5
# 입력 
# 00110
# 00011
# 11111
# 00000

graph = []
# for i in range(n):
#   graph.append(list(map(int, input())))

graph = [[0,0,1,1,0],[0,0,0,1,1],[1,1,1,1,1],[0,0,0,0,0]]

result = 0 

for i in range(n): # 0 1 2 3
  for j in range(m): # 0 1 2 3 4
    if dfs(i, j) == True:
      result += 1

print(result) # 3
print(graph) # 다 1이 되어 있음 





# -------------------------------------------------------------
# 문제 : 미로 탈출 => BFS로 풀기 
print()
print('문제 : 미로 탈출')

'''
동빈이는 N × M 크기의 직사각형 형태의 미로에 갇혔습니다. 미로에는 여러 마리의 괴물이 있어 이를 피해 탈출해야 합니다.
동빈이의 위치는 (1, 1)이며 미로의 출구는 (N, M)의 위치에 존재하며 한 번에 한 칸씩 이동할 수 있습니다. 이때 괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시되어 있습니다. 미로는 반드시 탈출할수 있는 형태로 제시됩니다.
이때 동빈이가 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하세요. 칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 계산합니다.

입력조건 
첫째 줄에 두 정수 N. M(4≤N, M≤200)이 주어집니다. 다음 N개의 줄에는 각각 M개의 정수(O 혹은 1)로 미로의 정보가 주어집니다. 각각의 수들은 공백 없이 붙어서 입력으로 제시됩니다. 또한 시작칸과 마지막 칸은 항상 1입니다.

출력조건 
첫째 줄에 최소 이동 칸의 개수를 출력합니다.

'''

from collections import deque

def bfs(x, y):
  queue = deque()
  queue.append((x, y))

  while queue:
    x, y = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue 

      if graph[nx][ny] == 0:
        continue

      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx, ny))

  return graph[n-1][m-1]


# n, m = map(int, input().split())
n, m = 5, 6

graph = []
# for i in range(n):
#   graph.append(list(map(int, input())))
graph = [[1,0,1,0,1,0],[1,1,1,1,1,1],[0,0,0,0,0,1],[1,1,1,1,1,1],[1,1,1,1,1,1]]


dx = [-1,1,0,0]
dy = [0,0,-1,1]

print(bfs(0,0))

