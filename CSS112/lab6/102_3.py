x = input()
Dict = {}
for i in x:
    if i in Dict:
        Dict[i] = Dict[i] + 1
    else:
        Dict[i] = 1
print(Dict)