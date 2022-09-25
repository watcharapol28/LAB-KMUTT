def reverse(d):
    d2 = {}
    for i in d:
        d2[d[i]] = i
    print(d,d2)
    return d2 
    
 # d เป็น dict ที่มี value ไม่ซ ้ากนั
 # คืน dict ใหม่ที่เก็บ key,value ที่ค่าเป็น value,key ของ d ที่ได้รับ

def keys(d, v):
    lst = []
    for i in d:
        if d[i] == v:
            lst.append(i)
    return lst
 # คืนลิสต์ที่เก็บค่าของ keys ใน d (เรียงยังไงก็ได้) ที่มีค่า value เท่ากับ v

exec(input().strip())
