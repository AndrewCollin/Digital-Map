from nodeAlgorithm import node

def printGraph(dic:dict):
    keyArray = dic.keys()
    lastNode = None
    for i in keyArray:
        print(i + " -> ", end = "")
        for n in dic[i].next:
            print((n[0],n[1].dictValue), end = "")
        if dic[i].START:
            print("  (START)", end = "")
        elif dic[i].END:
            lastNode = dic[i]
            print("  (END)", end = "")
        print()

    print("---------------")

    current = lastNode
    while (not current.START):
        print(current.dictValue + "<---", end = "")
        current = current.before
    print(current.dictValue)



def recursionD(current: node):
    for i in range(len(current.next)):
        n = current.next[i][1]
        v = current.next[i][0]

        if n.value > current.value + v:
            n.value = current.value + v
            n.before = current
            recursionD(n)


#Takes this tuple format (name1, value, name2).
def Dijkstra(start, end, array):
    dic = {}
    startNode = None
    for i in range(len(array)):
        dic[array[i][0]] = node(array[i][0])
        dic[array[i][2]] = node(array[i][2])
    for i in range(len(array)):
        dic[array[i][0]].next.append((array[i][1], dic[array[i][2]]))
        dic[array[i][2]].next.append((array[i][1], dic[array[i][0]]))
        if start == dic[array[i][0]].dictValue:
            dic[array[i][0]].START = True
            startNode = dic[array[i][0]]
            startNode.value = 0
        elif end == dic[array[i][2]].dictValue:
            dic[array[i][2]].END = True

    recursionD(startNode)
    printGraph(dic)
    return dic