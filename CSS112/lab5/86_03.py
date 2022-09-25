import string
alphabet = [i for i in string.ascii_lowercase]
x = input()
ans = ''
for i in x:
    if i.lower() in alphabet:
        ans += i
print(ans)

