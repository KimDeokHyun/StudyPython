#기본 for 문

arr = [1, 2, 3, 4, 5]

for i in arr:
    print(f'{i:2.1f}')


arr1 = list(range(1,100))
for i in arr1:
    print(f'{i:2.1f}')

#튜플 for 문
arr2 = ('me', 'my', 'friend', 'jane')

for item in arr2:
    print(f'{item:>10}')

#합계 for 문
numbers = list(range(0,101))  #1~100
res = 0
for item in numbers:
    res += item

print(f'{numbers[0]} 부터{numbers[-1]}까지의 총 합은 {res} 입니다.')    


#홀수 짝수 구분 for 문
numbers = list(range(0,10))  #1~9
for item in numbers:
    if item % 2 != 0:
        print(f'{item}은 홀수')


#Continue Break
number = list(range(1,21)) # 1~20
for item in number:
    if item == 15:
        break           #break

    if item % 2 == 1:
        print(f'{item}은 홀수')

##구구단
print('구구단 프로그램')
for i in range(2,10): #2~9
    if i == 8:
        continue        #8단 삭제 // break : 8단 이후 삭제
    for j in range(1,10):  #1~9
        print(f'{i} X {j} = {i*j:2d}', end='  ')
    print('  ')

#inline for 문
a=[1,2,3,4]
result = [i*3 for i in a]
print(result)

