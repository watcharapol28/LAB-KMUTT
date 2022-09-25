
# สมมุติมุ ว่ติาเราไ ว่ ด้ข้ด้ อข้มูลมาแ มู ล้วล้
no_subjects = 5
subject_room = [('CP', 1), ('ME', 2), ('PE', 1), ('CHE', 1), ('MT', 3)]
room_left = {'CP': 1, 'ME': 2, 'PE': 1, 'CHE': 1, 'MT': 3}
no_students = 6
student_regs = [('59301234521', 23.6, ['PE', 'CP', 'MT', 'CHE']),
('59300799921', 44.5, ['ME', 'CP', 'CHE', 'PE']),
('59300081621', 37.0, ['PE', 'CHE', 'MT', 'CP']),
('59300653521', 61.2, ['PE', 'MT', 'CP', 'ME']),
('59300002121', 19.4, ['CHE', 'CP', 'ME', 'CP']),
('59300048721', 7.0, ['ME', 'CP', 'CHE', 'MT'])]

sorted_student_regs = sorted(student_regs, key = lambda x : x[1], reverse = True)

match = []

for student in sorted_student_regs:
    for sc in student[2]:
        if(room_left[sc] > 0):
            amatch = dict()
            amatch['id'] =  student[0]
            amatch['subject'] = sc
            match.append(amatch)
            room_left[sc] -= 1
            break
print(match)
sorted_match = sorted(match, key = lambda x : x['id'])
print(sorted_match)

for i in sorted_match:
    print(f"{i['id']} {i['subject']}")

