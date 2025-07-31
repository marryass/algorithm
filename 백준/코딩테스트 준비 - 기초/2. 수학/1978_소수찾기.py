# 20250730
# https://www.acmicpc.net/problem/1978
# 1978_소수찾기.py

'''
문제
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

입력
첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

출력
주어진 수들 중 소수의 개수를 출력한다.
'''


n = int(input())

data = list(map(int, input().split()))


not_prime = 0 

for num in data:
  if num == 1 or (num % 2 == 0 and num !=2):
    not_prime += 1
  else: 
    for i in range(3, int(num**0.5)+1, 2):
      if num % i == 0:
        not_prime += 1
        break

print(n-not_prime)




