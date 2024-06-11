#파이썬에서 set은 중복을 허용하지 않는 데이터 구조
#아래와 같이 풀어도 됨 미리 중복 방지
#import sys
# n = int(sys.stdin.readline())
# s_set = set()

# for i in range(n):
#     s_set.add(sys.stdin.readline().strip())

# # 집합을 리스트로 변환 후 정렬
# s_list = list(s_set)
# s_list.sort()  # 사전 순으로 정렬
# s_list.sort(key=len)  # 길이 순으로 정렬

# for word in s_list:
#     print(word)

import sys
n = int(sys.stdin.readline())
s_list = [' '] * n
for i in range(n):
    s_list[i] = sys.stdin.readline().strip()
s_list = list(set(s_list))    
s_list.sort()
s_list.sort(key=len)
for j in s_list:
    print(j)
