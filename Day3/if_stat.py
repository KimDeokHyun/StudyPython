#if구문 - 흐름제어
name = 'C'

if name == 'A' or name == 'B': #들여쓰기( =Tab, Space x4)
    print('의사를 만나러 갑니다.')
    print('의사선생님께 인사합니다.')
elif name =='C':
    print ('주사실로갑니다.')
else:
    print('호출할 때 까지 대기합니다')

#if구문 - 흐름제어 name
name = ['명건', '태경', '기영', '광조']

if '명건' in name:
    print('의사를 만나러 갑니다.')
    print('의사선생님께 인사합니다.')
elif name =='다원':
    print ('주사실로갑니다.')
else:
    print('호출할 때 까지 대기합니다')

# 예제3
x = 10
if x != 10:
    print("10이 아닙니다")
else:
    [print('10')]

