# 공간 복잡도 줄이기
# 계수 정렬 O(N)
# 계수 정렬은 각 숫자의 개수를 세어주는 방식으로, 이 문제와 같이 숫자의 범위가 제한적이고 큰 수의 데이터를 정렬해야 할 때 매우 효율적
import sys
n = int(sys.stdin.readline())
num_list = [0] * 10001

for _ in range(n):
    num = int(sys.stdin.readline())
    num_list[num] += 1

for i in range(10001):
    if num_list[i] != 0:
        for _ in range(num_list[i]):
            print(i)
