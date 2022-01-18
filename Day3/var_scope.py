#변수 라이프스코프
a=1

def vartest(a):
    a=a+1
    return a

a = vartest(a)
print(a)