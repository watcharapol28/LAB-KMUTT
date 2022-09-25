char = str(input())
if char.isupper():
    print("All Capital Letter")
else:
    print("All Small Letter" if char.islower() else "Mix")