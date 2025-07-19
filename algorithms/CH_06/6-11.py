n = int(input())
array = []
for _ in range(n):
    info = list(input().split())
    array.append(info)

array.sort(key=lambda student: student[1])

for student in array:
    print(student[0],end=' ')
