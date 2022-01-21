#person.py
#Person 클래스
from unicodedata import name


class Person:
    name = '무명이' #이름이 없다
    age = 0
    height = 0
    gender = ''
    feetsize = 250
    bloodtype = ''


#생성자
    def __init__(self, name, age, height, gender) -> None:
        self.name = name
        self.age =  26
        self.height = height
        self.gender = gender
        print('Person이 생성되었습니다.')

    def 소개한다(self) -> None:
        greeting = f'''안녕하세요. 저는 {self.name}입니다
        {self.gender}구요. {self.age}살입니다.
        '''
        print(greeting)
        
    
    def 먹는다(self,food):
        print(f'{self.name}이(가) {food}를 먹는다')

    def 일한다(self,drink):
        print(f'{self.name}이(가) {drink}을(를) 마시면서 일한다')


if __name__ == '__main__':
    smg = Person('KDH',26, 170, 'male')  # = __init__(self, name, age)
    # smg.name = 'KDH'
    # smg.age = 26
    # smg.height = 170
    # smg.gender = 'male'
    smg.feetsize = 250
    smg.bloodtype = 'RH+b'
   
    smg.소개한다()
    smg.먹는다('밥')
    smg.일한다('핫식스')

