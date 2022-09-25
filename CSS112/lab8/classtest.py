#รหัสนศ , ชื่อ นามสกุล 
import pandas as pd
#สร้าง class ชื่อ Acs
class Acs: 
    #สร้างฟังก์ชันสำหรับกำหนดค่าเริ่มต้น หรือ method ชื่อ 
    #public attribute ค
    def __init__(self, code, name, email):#Constructor
        self.code = code
        self.name = name
        self.email = email
    
    #public method 
    def getShow(self):
        # self.code = input("Enter code: ")
        # self.name = input("Enter name: ")
        print("Code Student: ", self.code)
        print("Name Student: ", self.name)
        print("Email Student: ", self.email)
       
#สร้าง object ชื่อ acs
s = []
while True:
    
    acs = Acs(input("Enter code: "), input("Enter name: "), input("Enter email: "))      
    a = input("Enter Y to continue or N to exit: ")
    if a == "N":
        s.append(acs.code)
        s.append(acs.name)
        s.append(acs.email)
        break
    elif a == "Y":
        s.append(acs.code)
        s.append(acs.name)
        s.append(acs.email)      
        pass
    

     
    # acs.getShow()
# a = 
# b = 
#acs = Acs(input("Enter code: "), input("Enter name: "), input("Enter email: "))
print("ข้อมูลนักศึกษา".center(50, "-"))
acs.getShow()
print(s)
# acs = Acs(a, b)
#acs.getShow()   
