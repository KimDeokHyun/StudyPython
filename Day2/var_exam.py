# 변수
a = '헬로우'
print(a)

a=3.141592
print(a)

a=10
print(a)

a=99999999999999999999999999999999999999999999999999
print(a)

a = 1/10
print(a)

#변수 값을 지정(할당) - assign 방법
a = 3      # 왼쪽 값은 문자 변수만 가능
b = 3.141592
c = 'python'
d = (1, 2, 3)       #튜플
e = [1, 2, 3, 4]    #리스트
f = [7, '8', '$', a]

# 변수명
#변수지정 안되는 것 : 숫자시작, 기호, 띄어쓰기 (4val, -val, *val, val-, val$)
val = 10
val2 = 20
val4 = 30
Val = 40
val_ = 50
Val_ = 60
val_of_change = 99
MyAccountofBank = 1
은행계좌금액 = 1


print(id(val_))
print(id(Val_))

#변수타입 확인 
print(type(val_))  #50
print(type(d))     #(1, 2, 3)  
print(type(c))     #python
print(type(e))     #[1, 2, 3, 4]
print(type(f))     #[7, '8', '$', a]



