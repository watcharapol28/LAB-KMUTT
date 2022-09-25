#mainclass
class ACS:

    def __init__ (self,name,number,sex):
        self.__name = name
        self.__number = number
        self.__sex = sex

    def _showdata(self):
        print(self.__number,end=' / ')
        print(self.__sex,end=' / ')
        print(self.__name)
    
    #setter method
    def setName(self,newname):
        self.__name = newname

    #getter method
    def getName(self):
        return self.__name

    #classmethod()
    def how_old(self, obtained_age):
        ages = obtained_age
        print('Obtained ages:', ages)
    

#subclass
class boy(ACS):
    _gender = 'boy '
    def __init__(self, name, number, game):
        #super()
        super().__init__(name, number,self._gender)
        self.game = game
        
    def _showdata(self):
        super()._showdata()
        print(self.game)
    pass

#component
class Kmutt():
    def comp(self):
        print('Component')


class Student():
    def __init__(self):
        self.student = Kmutt()

    def showcomp(self):
        print('Composite')
        self.student.comp()

#Polymorphism
def func(obj): 
       obj._showdata() 

class Sum_ages():
    def sumage(num1, num2):
        print(num1 + num2)


#creat object by subclass
pongpayom = boy('pongpayom',441,'--favoritegame--')


#Single inhertance
pongpayom._showdata()
pongpayom.setName('pong')
pongpayom._showdata()


#Polymorphism
func(pongpayom)


#Composition
pong441 = Student()
pong441.showcomp()


#classmethod()
ACS.age_student = classmethod(ACS.how_old)
ACS.age_student(19)


#staticmethod
Sum_ages.sumage = staticmethod(Sum_ages.sumage)
sum = Sum_ages.sumage(19, 18)