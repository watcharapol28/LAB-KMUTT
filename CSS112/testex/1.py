#no_subjects = 5
#subject_room = [('CP', 1), ('ME', 2), ('PE', 1), ('CHE', 1), ('MT', 3)]
#room_left = {'CP': 1, 'ME': 2, 'PE': 1, 'CHE': 1, 'MT': 3}
#no_students = 6
#student_regs = [('59301234521', 23.6, ['PE', 'CP', 'MT', 'CHE']),
#('59300799921', 44.5, ['ME', 'CP', 'CHE', 'PE']),
#('59300081621', 37.0, ['PE', 'CHE', 'MT', 'CP']),
#('59300653521', 61.2, ['PE', 'MT', 'CP', 'ME']),
#('59300002121', 19.4, ['CHE', 'CP', 'ME', 'CP']),
#('59300048721', 7.0, ['ME', 'CP', 'CHE', 'MT'])]
no_subjects = int(input())
subject_room = list()
for i in range(no_subjects):
    x ,y = input().split()
    subject_room.append((x,int(y)))

room_left = dict(subject_room)
#print(room_left)
no_students = int(input())

student_regs = list()

for i in range(no_students):
    x = input().split(" ")
    student_regs.append((x[0],float(x[1]),list(x[2:])))

sorted_student_regs = sorted(student_regs, key = lambda x : x[1], reverse = True)

#print(sorted_student_regs)
lst = list()

for i in sorted_student_regs:
    n = 0
    #print(room_left[i[2][n]])
    while room_left[i[2][n]] == 0: #room_left ตัวที่ต้องการ = 0ไหม หากเท่ากับก็จะข้ามไปเช็คลำดับต่อไป
        n += 1
    lst.append((i[0], i[2][n])) #ลิสต์ ไอดีและ คณะที่ได้
    room_left[i[2][n]] -= 1 #room_left ตัวที่ต้องการลบออก 1

lst = sorted(lst) #เรียงตาม id

for i in lst:
    print(i[0],i[1]) #แสดงผล


"""
5
CP 1
ME 2
PE 1
CHE 1
MT 3
6
59301234521 23.6 PE CP MT CHE
59300799921 44.5 ME CP CHE PE
59300081621 37 PE CHE MT CP
59300653521 61.2 PE MT CP ME
59300002121 19.4 CHE CP ME CP
59300048721 7 ME CP CHE MT 
"""