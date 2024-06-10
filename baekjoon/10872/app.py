#재귀 함수
#재귀 함수는 순차적으로 호출을 하고 역순으로 종료한다.

def factorial(n):
    result = 1
    if n>0:
        result = n* factorial(n-1)
    return result

n = int(input())
print(factorial(n))
