import random
class Animal:
    def __init__(self,name,ves = 50,energy=20):
        self.name = name
        self.ves = ves
        self.energy = energy
    def inf(self):
        print('Текущий вес: ',self.ves,'\n','Текущая энергия: ',self.energy,sep = '')
        return ''
    def eat(self):
        self.ves+=5
        self.energy+=10
        
        return self.inf()
    def walk(self):
        if self.ves >= 5 and self.energy >=20:
            self.ves-=5
            self.energy-=20
            print(self.name,'погулял')
        else: print(self.name,' не может гулять, накормите его или дайте ему отдохнуть')
        return self.inf()
    def sleep(self):
        if self.energy < 50:
            self.energy+=30
        else:
            print(self.name,'не устал')
        return self.inf()
class Tiger(Animal):
    def __init__(self,name,ves,energy=20):
        super().__init__(name,ves,energy=20)
    def kill(self):
        s = random.randint(1,2)
        m = input('Введите имя жертвы: ')
        if self.energy >= 30 and self.ves>=6:
            if s == 1:
                self.ves-=5
                self.energy-=30
                print('Тигр',self.name,'убил',m)
            if s == 2:
                print(self.name,'хороший тигр, и не будет этого делать!')
        else: print('Тигр',self.name,'слишком устал, чтобы убивать')
        return self.inf()
def main():
    name = input('Введите имя животного: ')
    ves = int(input('Введите вес животного: '))
    animal = Tiger(name,ves)
    choice = None
    while choice != 0:
        print('''
            Доступные действия:
               0 - оставить животное в одиночестве
               1 - проверить животное
               2 - накормить животное
               3 - сон
               4 - прогулка
               5 - убивать
            '''
        )
        choice = input('Что будем делать: ')
        if choice == '1':
            animal.inf()
        elif choice == '2':
            animal.eat()
        elif choice == '3':
            animal.sleep()
        elif choice == '4':
            animal.walk()
        elif choice == '5':
            animal.kill()
        elif choice == '0':
            print(animal.name,' расстроенно прощается...')
            break
        else:
            print('Неверный символ')
main()

    





        