# Random 함수
import random

print(random.choice(range(1,7))) #주사위

# Lottery
numbers = list(range(1,46))
print(numbers)
lottery = []           #list()

for i in range(6):
    lottery.append(random.choice(numbers))   #번호 중복 가능

print(lottery)     #[23, 9, 41, 16, 27, 44]

