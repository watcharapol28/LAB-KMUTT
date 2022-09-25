graph = {}
n = int(input("How many line : "))
for i in range(n):
    x, y, w = input("Input 2 point and weight :").split()
    if not x in graph:
        graph[x] = []
    if not y in graph:
        graph[y] = []
    value = dict()
    value[y] = int (w)
    graph[x].append(value) 
    value = dict()
    value[x] = int (w)
    graph[y].append(value)

s, t = input("Input start and end point : ").split()


"""
for i in graph:
    print("i =", i, end =' ')
    l = len(graph[i])
    if l != 0:
        for j in range(l):             #this dict 2nd such graph[i] = { y : w }    use j for check and get y value
            print("  j =", j ,sep =' ')
            #print(graph[i][j])
            for k in graph[i][j]:
                print(k)                        # 2nd point and use graph[i][j][k] for weight
"""