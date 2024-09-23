import sys
sys.stdin = open("text.txt")

import sys
input = sys.stdin.readline

# 실제 실행되는 코드: sys.stdin.readline
K = int(input())
# print(K)

# 정수를 저장할 스택
stack = list()

for _ in range(K):
    number = int(input())
    if number == 0:
        stack.pop()
    elif number != 0:
        stack.append(number)        

# 모든 수의 합을 출력
print(sum(stack))
