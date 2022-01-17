#리스트 연산
arr = list(range(5))
print(arr)                  #[0, 1, 2, 3, 4]

arr = list(range(5,20,2))
print(arr)                  #[5, 7, 9, 11, 13, 15, 17, 19]

print(arr[0] + arr[5])      #20

#2차원 배열(리스트)
arr2 = [1, 2, ['Hi', 'My', 'Friend']]
print(arr2[0])       #1
print(arr2[2])       #['Hi', 'My', 'Friend']
print(arr2[2][1])    #My
print(arr2[2][1][0]) #M

arr3 = list(range(1,4))
print(arr3)         #[1, 2, 3]
print(arr3 *3)      #[1, 2, 3, 1, 2, 3, 1, 2, 3]
print(arr3 + arr)   #[1, 2, 3, 5, 7, 9, 11, 13, 15, 17, 19]

#리스트 함수
print('-- 리스트 내장함수')
del(arr3[1])
print(arr3)         #[1, 3]

arr3.remove(1)
print(arr3)         #[3]

#리스트 삭제
arr4 = [4, 2, 6, 9, 12, 16, 7, 1, 3, 3, 5]
arr4.remove(3)     #값을 찾아서 삭제
print(arr4)        #[4, 2, 6, 9, 12, 16, 7, 1, 3, 5]
del(arr4[8])       #리스트 인덱스로 삭제
print(arr4)        #[4, 2, 6, 9, 12, 16, 7, 1, 5]

arr.sort()
print(arr4)        #[4, 2, 6, 9, 12, 16, 7, 1, 5]

arr4.reverse()
print(arr4)        #[5, 1, 7, 16, 12, 9, 6, 2, 4]

arr4.insert(2,10)
print(arr4)        #[5, 1, 10, 7, 16, 12, 9, 6, 2, 4]

tup1 = tuple(range(1,6))
print(tup1)        #(1, 2, 3, 4, 5)

#tup1[0] = 99
print(tup1)        #TypeError: 'tuple' object does not support item assignment

#딕셔너리

dic1 = {1 : 'a'}
dic1[2] = 'b'
print(dic1)        #{1: 'a', 2: 'b'}

dic1['name'] = 'hugo'
print(dic1)        #{1: 'a', 2: 'b', 'name': 'hugo'}

del dic1['name']
print(dic1)        #{1: 'a', 2: 'b'}

print(dic1.keys())     #dict_keys([1, 2])
print(dic1.values())   #dict_values(['a', 'b'])
print(dic1.items())    #dict_items([(1, 'a'), (2, 'b')])

#리스트를 튜플 변환
print('-- 리스트/튜플 변환 --')
print(tup1)          #(1, 2, 3, 4, 5)

print(arr4)          #[5, 1, 10, 7, 16, 12, 9, 6, 2, 4]
tup2 = tuple(arr4)   #튜플로 변환
print(tup2)          #(5, 1, 10, 7, 16, 12, 9, 6, 2, 4)

arr.sort()
print(tup1)          #(1, 2, 3, 4, 5)

arr5 = list(tup1)
print(arr5)          #[1, 2, 3, 4, 5]

arr5.append(6)
print(arr5)          #[1, 2, 3, 4, 5, 6]

tup1 = tuple(arr5)
print(tup1)          #(1, 2, 3, 4, 5, 6)
