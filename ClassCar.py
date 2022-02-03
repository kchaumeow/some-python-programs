class Car():
    def __init__(self, name, gaz=0,put=0):
        self.name = name
        self.gaz = gaz
        self.put = put
    def fill(self):
         self.gaz += 100
         print('Машина ',self.name,' заправлена!','\n',self.ur())
         return  ''
    def go(self):
       s = int(input('Расстояние: '))
       while s/10 > self.gaz:
           print('Бензина не хватит на такое расстояние!')
           s = int(input('Расстояние: '))
       print('Машина ',self.name,' поехала!')
       self.gaz -= s/10
       print(self.ur())
       self.put +=s
       return ''
    def ur(self):
         print( 'Уровень топлива: ',self.gaz)
         return  ''
def main():
    name = input('Введите марку машины: ')
    myCar = Car(name)
    choice = None
    while choice != '0':
        print('''

            Автомобиль:
                0 - выйти
                1 - заправить автомобиль
                2 - поехать
                3 - уровень бензина в баке
                4 - пройденный путь
                
                ''')
        choice = input('Что будем делать: ')
        if choice == '1':
            myCar.fill()
        elif choice == '2':
            myCar.go()
        elif choice == '3':
            myCar.ur()
        elif choice == '0':
            print('Пока!')
            break
        elif choice == '4':
            print('Машина ',myCar.name,' проехала ',myCar.put,'км')
        else:
            print('Введен некорректный символ!')

main()
    
         
            
            
        
