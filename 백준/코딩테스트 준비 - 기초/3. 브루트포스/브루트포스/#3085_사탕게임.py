# 20250805
# https://www.acmicpc.net/problem/3085
# 3085_사탕게임.py

'''
문제
상근이는 어렸을 적에 "봄보니 (Bomboni)" 게임을 즐겨했다.

가장 처음에 N×N크기에 사탕을 채워 놓는다. 사탕의 색은 모두 같지 않을 수도 있다. 상근이는 사탕의 색이 다른 인접한 두 칸을 고른다. 그 다음 고른 칸에 들어있는 사탕을 서로 교환한다. 이제, 모두 같은 색으로 이루어져 있는 가장 긴 연속 부분(행 또는 열)을 고른 다음 그 사탕을 모두 먹는다.

사탕이 채워진 상태가 주어졌을 때, 상근이가 먹을 수 있는 사탕의 최대 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 보드의 크기 N이 주어진다. (3 ≤ N ≤ 50)

다음 N개 줄에는 보드에 채워져 있는 사탕의 색상이 주어진다. 빨간색은 C, 파란색은 P, 초록색은 Z, 노란색은 Y로 주어진다.

사탕의 색이 다른 인접한 두 칸이 존재하는 입력만 주어진다.

출력
첫째 줄에 상근이가 먹을 수 있는 사탕의 최대 개수를 출력한다.
'''

N = int(input())
board = [list(input().strip()) for _ in range(N)]

def check(board):

  N = len(board)
  max_count = 1

  # 행 검사 
  for i in range(N):
    count = 1 
    for j in range(1, N):
      if board[i][j-1] == board[i][j]:
        count += 1
      else: 
        count = 1 
      max_count = max(max_count, count)
      
  # 열 검사 
  for j in range(N):
    count = 1 
    for i in range(1, N):
      if board[i][j] == board[i-1][j]:
        count += 1
      else: 
        count = 1
      max_count = max(count, max_count)
      
  return max_count



max_count = 1

for i in range(N):
  for j in range(N):

    # 오른쪽이랑 교환 
    if j+1 < N and board[i][j] != board[i][j+1]:
      board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
      max_count = max(max_count, check(board))
      board[i][j], board[i][j+1] = board[i][j+1], board[i][j]

    # 아래랑 교환 
    if i+1 < N and board[i][j] != board[i+1][j]:
      board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
      max_count = max(max_count, check(board))
      board[i][j], board[i+1][j] = board[i+1][j], board[i][j]

print(max_count)
  

    

      

