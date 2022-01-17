# 연산자
import datetime
from sqlite3 import Date
from xmlrpc.client import DateTime


a = 11
b = 4
print (a + b)
print (a - b)
print (a * b)
print (a **b)
print (a / b)

#문자열 연산
 #문자열 연산에서는 +, *만 존재
stat1 = 'hello'
stat2 = 'World'
print (stat1, stat2)   #hello World
print (stat1  + stat2) #helloWorld

res = stat1, stat2
print(res) #('hello', 'World')

res1 = stat1 + stat2
print(res1) #helloWorld

# 문자열 길이
print(len(stat1))    #5
stat3 = '안녕하세요'
print(len(stat3))    #5

# 문자열 인덱스, 리스트와 동일한 작업
print(stat3[0]) #안
print(stat3[1]) #녕
print(stat3[2]) #하
print(stat3[3]) #세
print(stat3[4]) #요
print(stat3[5]) #오류. 예외발생



print (stat3[-1]) #요

# 문자열 자르기
일시 = '2022-01-17 14:39:25'
print = 일시
print(일시[:4], '년')
print(일시[5:7], '월')
print(일시[8:10], '일')
print(일시[11:13], '시')
print(일시[14:16], '분')
print(일시[17:], '초')
print(일시[-5:-3], '분')

list_a = [1,2,3,4,5]
list_a[1] = 19
print(list_a)    #[1, 19, 3, 4, 5]

print(stat3)     #안녕하세요
stat4 = '저리가' + stat3[3:]
print(stat4)     #저리가세요

#문자열 포맷팅
str1 = "i'm so happy {0} U".format('to')
print(str1)                  #i'm so happy to U

첫번째 = '투'
두번째 = '유'
str1 = "i'm so happy {0} U. are {1}?".format(첫번째, 두번째)
print(str1)                  #i'm so happy 투 U. are 유?

str2 = f"i'm so happy {첫번째} U. are {두번째}?"
print(str2)                  #i'm so happy 투 U. are 유?

money = 100000000000
print(format(money, ',d'))   #100,000,000,000

from datetime import datetime
now = datetime.now()   #현재일시 생성
print(now)             #2022-01-17 15:31:04.907014
print(now.strftime('%Y년 %m월 %d일 %H : %M : %S')) #2022년 01월 17일 15 : 33 : 13

import math

myPi = math.pi
print(math.pi)                 #3.141592653589793
print('{0:0.6f}'.format(myPi)) #3.141593
print(f'{myPi:0.6f}')          #3.141593

full_name = 'Hugo MG Sung'
age = 47
greeting = f'''안녕하세요. 저는 {full_name}입니다. 
나이는 {age:0.2f}살 이구요.'''       
print(greeting)   #안녕하세요. 저는 Hugo MG Sung입니다.나이는 47.00살 이구요

part_name = full_name.split()
print(part_name)  #['Hugo', 'MG', 'Sung']

test = 'Hey. guys'
print(test.split(','))   #'Hey. guys'

#|
code = 'TEST|2002|01|17|F45678'
split_codes = code.split('|') 
print(split_codes)  # ['TEST', '2002', '01', '17', 'F45678']

# 단어교체 replace
print(full_name.replace('Hugo MG', 'Ashley'))

#strip ==Oracle TRIm과 동일

aaa = '   HELLO WORLD   '
print(aaa)
print(aaa.lstrip())           #   HELLO WORLD
print(aaa.rstrip())           #HELLO WORLD 
print(aaa.strip())            #HELLO WORLD

print(full_name.index('H'))   #0
print(full_name.index('u'))   #1
print(full_name.index('g'))   #2
print(full_name.index('G'))   #6
print(full_name.index('X'))   #not found

print(full_name.find('X'))    #-1
print(full_name.find('MG'))   #5

#문자 갯수 카운트 count
print(full_name.count('u'))   #2
print(full_name.count('ng'))  #1

print('-'.join(full_name))    #H-u-g-o- -M-G- -S-u-n-g

print(full_name.upper())      #HUGO MG SUNG
print(full_name.lower())      #hugo mg sung

