#시간과 관련된 문제
# M<45일때 시간이 달라지는 것을 잘 파악 했어야 했다.

H,M = map(int,input().split())

if M <45:
    M = M+15
    if H == 0:
        H = 23
    else:
        H = H-1
else:
    M = M-45
    
print(H,M)
