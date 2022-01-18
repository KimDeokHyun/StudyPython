hit = 0

while hit < 100:        # hit 값이 참인 동안
    hit += 1           # hit=hit+1

    print(f'나무를 {hit:2d}번 찍었습니다')
    if hit == 10:
        print('나무가 넘어갑니다')
        break

print('나무찍기를 마칩니다')


#for 문
for hit in range(0,10):
    if hit > 9:
        break
    print(f'나무가 {hit+1}번 찍습니다.')
print('나무가 넘어갑니다')
print('나무찍기를 마칩니다.')

