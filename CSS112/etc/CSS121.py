#################################################################################################################################
#MST Kruskal's
path = []
def mst(graph, sum = 0):
    check = {}
    test = {}                              #create dict for get 2 point in g[][0]
    for i in range(len(graph)):
        test[graph[i][0]] = graph[i][1]
    for (u, v), w in test.items():
        # print(u,v,w) 
        if not (u and v in check):
            sum += w
            check[u] = u
            check[v] = u
            #print("u = ",u,"\tv = ",v,"\theadU = ",check[u],"\theadV = ",check[v],"\tsum = ",sum,sep='')
        elif not u in check:
            sum += w
            check[u] = check[v] 
        elif not v in check:
            sum += w
            check[v] = check[u] 
            #print("u = ",u,"\tv = ",v,"\theadU = ",check[u],"\theadV = ",check[v],"\tsum = ",sum,sep='')
        elif check[u] != check [v]:
            sum += w
            #print("u = ",u,"\tv = ",v,"\theadU = ",check[u],"\theadV = ",check[v],"\tsum = ",sum,sep='')
            for i in check:
                if check[i] == check[v]: #or check[u]:
                    check[i] = check[u]
        else : continue
        ls = [u,v]
        path.append(ls)  
#    print(check)
    return sum


graph = edges = {}
n = int(input("How many line : "))
for i in range(n):
    s, t, w = input("Input 2 point and weight : ").split()
    edges[s,t] = int(w)
#print(edges)
sort_edges = sorted(edges.items(), key=lambda x: x[1])
#for i in range(len(sort_edges)):
#    graph[sort_edges[i][0]] = sort_edges[i][1]
#print(sort_edges,graph)
weight = mst(sort_edges)
print("   - Minimum spanning tree - ")
for i in path:
    print("\t  ",i[0]," -- ",i[1])
print("\tWeight  = ", weight)

#################################################################################################################################
"""
input   
s t w
1 5 4
1 4 1
5 4 9
1 2 2
2 4 3
4 3 5
3 2 3
3 6 8
6 2 7
"""