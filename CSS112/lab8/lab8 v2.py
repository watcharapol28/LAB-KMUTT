class info:
    def __init__(self, name ,age):
        self.name = name
        self.age = age
        self.salary = 0


class boss(info):
    salary = 60000
    def __init__(self, name, age):
        super().__init__(name, age)


class employee(info):
    salary = 20000
    def __init__(self, name, age):
        super().__init__(name, age)


class person(boss, employee):
    def __init__(self, name, age, status):
        super().__init__(name, age)
        self.status = status
        if status == employee.__name__:
            self.salary = employee.salary
        else:
            self.salary = boss.salary


class about(person):

    def info_(self):
        print("{} have {} years old ,Now his status is {} in company and his salary is {} ".format(self.name, self.age, self.status, self.salary))  

    @staticmethod
    def salary_increase(status, price):
        if status == "boss":
            boss.salary += price
        else :
            employee.salary += price
    
    @staticmethod
    def salary_decrease(status, price):
        if status == "boss":
            boss.salary -= price
        else :
            employee.salary -= price

    @classmethod
    def increase_person(cls, name, price):
        name.salary += price
    
    @classmethod
    def decrease_person(cls, name, price):
        name.salary -= price


"""
about.salary_increase("boss",3000)
pingpong = about("Pingpong Pangpang", 20, "boss")
pingpong.info_()
about.salary_decrease("boss",3000)
pingpong.info_()
print()

meow = about("Meow Meow",5 , "boss")
meow.info_()
about.increase_person(meow, 3000)
meow.info_()
print()

about.salary_decrease("employee",6000)
sor = about("Sor S",15 ,"employee")
sor.info_()
about.decrease_person(sor, 3000)
sor.info_()
"""