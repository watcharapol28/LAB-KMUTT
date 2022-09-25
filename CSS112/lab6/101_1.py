#ตอบคำถาม
#1.1 Dictionary
#1.2 Dictionary หรือ Boolean
#1.3 Dictionary + Tuple
#1.4 Tuple
#1.5 List หรือ Dictionary สามารถเปลี่ยนแปลงค่าได้

cp_count = 0
com_pro = {}
depratment = {}
phone = {}
phone_series = {}
phone_last_num = [0 for i in range(10)]
n = int(input("how many students in your class : "))
#example input : 3

for i in range(n):
    print("########### STUDENT", i + 1, "###########")
    print("Pls input 1.ID number, 2.Department, 3.Garde compro(if not registered key -1)")
    x = input(": ").split()
    #example input : 64090500421 Math B+
    id_std, depart_std, grade_std = x 
    if grade_std != '-1':
        com_pro[int(id_std)] = grade_std
        cp_count += 1
    if not depart_std in depratment:
        depratment[depart_std] = (int(id_std),)
    else:
        depratment[depart_std] += (int(id_std),)
    ph_series = input("in put your Phone series : ").split(",")
    #example input : Nokia, sumsung
    for i in ph_series:
        if not id_std in phone_series:
            phone_series[id_std] = (i, )
        else:
            phone_series[id_std] += (i, )
    ph = str(input("in put your Phone numbers : "))
    #example input : 0886669990
    phone_last_num[int(ph[len(ph) - 1])] += 1
    print()

print("Students in compro class have", cp_count, "peoples")
print("ID Students in compro class :",com_pro)
for i in depratment:
    print("ID Student in", i, "department :",depratment[i])
print("Last number in phone numbers")
mx = -1
num = 0
for i in range(10):
    print(i,"have", phone_last_num[i],"peoples")
    if mx < phone_last_num[i]:
        mx = phone_last_num[i]
        num = i
print("Last number have many peoples used is:",num ,"have" ,mx,"peoples")

    


            
