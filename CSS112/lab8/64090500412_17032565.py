#โรงพยาบาล Felling Good

#สร้าง class ชื่อ Hotpital
class Hotpital:
    
    #สร้างฟังก์ชันสำหรับกำหนดค่าเริ่มต้น หรือ method ชื่อ 
    #public attribute 
    HotpitalName = "Felling Good"
    def __init__(self, name, salary, duty):#Constructor
        self.name = name 
        self.salary = salary
        self.duty = duty
        
    #public method 
    def getShow(self):
        print("\nซื่อ : ", self.name)
        print("เงินเดือน: ", self.salary)
        print("หน้าที่: ", self.duty)
        
    def sum_salary(self, overtime=0):#ฟังก์ชันสำหรับคำนวนรวมเงินเดือน
        self.overtime = (overtime*200)*216 #คำนวน ot ตามจำนวนชั่วโมงที่ทำงาน / 5วันรวม 1 ปี
        return (self.salary*12) + self.overtime 
    
    
    
class Docter(Hotpital):#สร้าง class ชื่อ Docter สืบทอดคุณสมบัติจาก class Hotpital
    dutyName = "แพทย์"
    def __init__(self, name,salary, department, clinic,level):
        super().__init__(name, salary, self.dutyName)
        self.clinic = clinic
        self.department = department
        self.level = level
        
    def getShow(self):#ฟังก์ชันสำหรับแสดงข้อมูล
        super().getShow()
        print("แผนก: ", self.department)
        print("ระดับ: ", self.level)
        print("รายได้จากการเปิดคลินิก: ", self.clinic)
        print("รายได้ต่อปี: ", self.sum_salary()+self.clinic,  "บาท")
        print('\n','-'*50)
        
        
class Nurse(Hotpital):#สร้าง class ชื่อ Nurse สืบทอดคุณสมบัติจาก class Hotpital
    dutyName = "พยาบาล"
    def __init__(self, name, salary, building, ot_time):
        super().__init__(name, salary, self.dutyName)
        self.overtime = ot_time
        self.building = building
        
    
    
    def getShow(self):#ฟังก์ชันสำหรับแสดงข้อมูล
        super().getShow()
        print("อาคาร: ", self.building)
        print("รายได้ต่อปี: ", self.sum_salary(self.overtime), "บาท")
        print("Over time / Year: ", self.overtime, "บาท")
        print('\n','-'*50)
        
    
class Nusring_assistant(Hotpital):#สร้าง class ชื่อ Nusring_assistant สืบทอดคุณสมบัติจาก class Hotpital
    dutyName = "พยาบาลผู้ช่วย"
    def __init__(self, name, salary, room, ot_time):
        super().__init__(name, salary, self.dutyName)
        self.room = room
        self.overtime = ot_time
        
    def getShow(self):#ฟังก์ชันสำหรับแสดงข้อมูล
        super().getShow()
        print("ห้อง: ", self.room)
        print("รายได้ต่อปี: ", self.sum_salary(self.overtime), "บาท")
        print("Over time / Year: ", self.overtime, "บาท")
        print('\n','-'*50)
        


#สร้าง object 
print('\n',Hotpital.HotpitalName.center(20, '+'))
docter = Docter('ประจักษ์ ศิรินันท์', 59000, 'ศัลยแพทย์', 80000, 'หัวหน้า')
docter.getShow()
nurse = Nurse('เพ็ญศรี สุวรรณา', 50000, 1, 4)
nurse.getShow()
nursing_assistant = Nusring_assistant('เปาวเรส ดีงาท', 35000, 'ห้องจ่ายยา', 3)
nursing_assistant.getShow()