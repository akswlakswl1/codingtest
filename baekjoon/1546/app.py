# input을 리스트로 바로 받아오기
# for문에서 해당 인덱스값 변경


n = int(input())
s = list(map(int,input().split()))
m = max(s)

for i in range(len(s)):
        s[i] = (s[i]/m) * 100

print(sum(s)/n)
