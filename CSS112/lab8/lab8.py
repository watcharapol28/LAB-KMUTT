class info:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    
class boss(info):
    salary = 60000
    def __init__(self, name, age):
        super().__init__(name, age)


class employee(info):
    salary = 20000
    def __init__(self, name, age):
        super().__init__(name, age)
        

class person(employee, boss):
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

    def show_salary(self):
        print("now boss have salary {}  and employee have salary {}".format(self.name, self.salary))

    @staticmethod
    def salary_increase(name):
        if status == "boss":
            boss.salary += 3000
        else :
            employee.salary += 1500
    
    @staticmethod
    def salary_decrease(name):
        if status == "boss":
            boss.salary -= 2000
        else :
            employee.salary -= 500



A1 = about("Warsss Serrr", 26, "employee")
about.salary_increase("boss")
A1.info_()
A2 = about("Eter Essey", 35, "boss")
A2.info_()
A3 = about("Warssss SEE",27 ,"boss")
A3.info_()
#print(A1.__class__.mro())