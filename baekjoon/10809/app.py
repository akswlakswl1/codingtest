#포함 하는지 확인 if char in s

n = "abcdefghijklmnopqrstuvwxyz"
s = input()
for char in n:
    if char in s:
        index = s.index(char)
        print(index,end=(' '))
    else:
        print('-1',end=(' '))
