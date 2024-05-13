#파이썬에서 contain은 in으로 확인하면됨
#리스트에 dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ'] 저장해서 확인하는 방법도 있음
#dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
#a = input()
#ret = 0
#for j in range(len(a)):
#    for i in dial:
#        if a[j] in i:
#            ret += dial.index(i)+3
#print(ret)


s = input()
result = 0
for char in s:
    num = ord(char) - 65
    result += (num//3)+3
    if char in 'SVYZ':
        result -= 1
print(result)
