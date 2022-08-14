from nodeAlgorithm import node
from queue import PriorityQueue

#Array = (Node1, Value, Node2)
def printNode(nodeDict:dict):
    key = nodeDict.keys()
    for i in key:
        print(nodeDict[i].dictValue + f" ({nodeDict[i].value}) ", end = "")
        for n in nodeDict[i].next:
            print((n[0], n[1].dictValue), end = "")
        print()

def recurrsion(current):
    for i in current.next:
        if i[1].value > current.value + int(i[0]):
            i[1].value = current.value + int(i[0])
            recurrsion(i[1])

def bellmanFord(start, array):
    nodeDict = {}
    for i in array:
        nodeDict[i[0]] = node(i[0])
        nodeDict[i[2]] = node(i[2])
    for i in array:
        nodeDict[i[0]].next.append((i[1], nodeDict[i[2]]))
    printNode(nodeDict)

    nodeDict[start].value = 0
    recurrsion(nodeDict[start])
    print()
    printNode(nodeDict)




