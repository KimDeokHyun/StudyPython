#파일입출력

#파일출력
   #f = open('newfile.txt','w')
   #f.close()

#해당 폴더에 파일 생성
   #f = open('C:/Sources/test.txt','w')
   #f.close()
   #print('파일이 생성되었습니다')

# newfile.txt 파일입력(읽어오기)
f = open('newfile.txt', 'r', encoding='utf-8')
while True:
    line = f.readline()
    if not line:
        break

    print(line)

f.close()