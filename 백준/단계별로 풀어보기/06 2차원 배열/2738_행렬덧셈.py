# 20250723
# https://www.acmicpc.net/problem/2738
# 2738_행렬덧셈.py

'''
행렬 덧셈 성공
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	128 MB	126829	66913	57272	53.065%
문제
N*M크기의 두 행렬 A와 B가 주어졌을 때, 두 행렬을 더하는 프로그램을 작성하시오.

입력
첫째 줄에 행렬의 크기 N 과 M이 주어진다. 둘째 줄부터 N개의 줄에 행렬 A의 원소 M개가 차례대로 주어진다. 이어서 N개의 줄에 행렬 B의 원소 M개가 차례대로 주어진다. N과 M은 100보다 작거나 같고, 행렬의 원소는 절댓값이 100보다 작거나 같은 정수이다.

출력
첫째 줄부터 N개의 줄에 행렬 A와 B를 더한 행렬을 출력한다. 행렬의 각 원소는 공백으로 구분한다.

'''
n, m = map(int, input().split())

mat = [ [0]*m for _ in range(n*2)]

for i in range(n*2):
  num = list(map(int, input().split()))
  mat[i] = num

a = mat[:n]
b = mat[n:]


for i in range(n):
  for j in range(m):
    print(a[i][j] + b[i][j], end=" ")
  print()
