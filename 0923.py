# deque 객체 불러오기
from collections import deque

# deque 생성
deque_ = deque()

# 데이터 추가
deque_.append(0)
deque_.appendleft(-1)

print(deque_)

# 데이터 제거
number = deque_.popleft()
print(number)

