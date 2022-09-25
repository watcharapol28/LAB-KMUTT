import re
mydict = {
    '.':'.',
    'Amanda' : 'Doctor',
    "haven't" : 'am',
    'knew' : 'now',
    'how' : 'in',
    'joyous' : 'great',
    'could' : 'threatening',
    'be' : 'danger,',
    'until' : 'please',
    'saw' : 'need',
    'face.': 'help',
    'leaps' : 'beats',
    'hummingbird' : 'machine ',
    'in':'very',
    'flight' : 'alarmingly',
    'time' : 'hour,',
    'see' : 'need',
    'you' : 'the drug',
    'inspires' : 'causes'
}
letter = """Dear Amanda
 
I haven't knew how joyous life could be until I saw your face.
My heart leaps like a hummingbird in flight every time I see your face.
This is something I have never felt before, and it is you that inspires it."""

mypassage = letter.split("\n")
passage = []
for i in mypassage:
    a = re.sub(r'(\n)(-|[0-9])', r"\1\n\2", i).split()
    passage.append(a)

for i in range(len(passage)):
    if i == 2:
        print()
    for j in passage[i]:
        if j in mydict:
            print(mydict[j], end = ' ')
        else:
            print(j, end = ' ')
