# a = [1,2,3,4]
# type(a)
# len(a)

# a=[[2,3],[3,3,4]]     #2 3
# len(a)                #3 3 4

# ##리스트, 행렬의 차이점
#  #행렬구조에 특화된 numy 모듈에 대하여 먼저 학습
#  #행렬은 반드시 행과 열의 갯수가 인덱싱마다 같아야하고, 연산이 가능. 자료의 성격이 같아야 함

# #기본 파이썬 연산 a리스트 *3
# a = [1,2,3,4,5]
# val = 3
# b = []
# for x in a :
#     b.append(x+val)

# a= [1,2,3,4,5]
# b= [10,20,30,40,50]
# val = 3
# cc = []

# for x1, x2 in zip(a,b):
#     cc.append(x1+x2)

# ##넘파이
import numpy as np
# x=[[2,3,4],[2,3]]
# x2 = np.array(x) + 2
# np.shape(x)
# np.shape(x2)  # x2는 배열로 변환되었기 때문에 x2.shape

# #문자자료열 = 그룹변수(남자 x명, 여자 x명)

# #ex
# x=[[2,3,4],[22,33,44]]
# val = 100
# x2=np.array(x)
# x2+100     #x2+[[100,100,100]],[100,100,100]

# #1개의 픽셀에 0~255 값이 들어가면 그레이스케일 (0=검정, 255=흰색)
import matplotlib.pyplot as plt
# x = [[0,255,100],[255,0,200]] 
# plt.imshow(x,cmap ='gray')

# x2=np.array(x)
# x3=x2-300
# plt.imshow(x3, cmap='gray')

#사진 불러오기

from PIL import Image  # pil폴더에서 image 가져오기
img = Image.open('./pic/img1.png')
img
np.array(img)

#파일 리스트 불러오기
# import os
# file_list = os.listdir('./pic/')
# file_list

from PIL import Image
fileName=folderName '/' file_list[0]
Image.open(fileName)
