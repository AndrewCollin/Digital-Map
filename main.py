import pickle
import tkinter as tk
from tkinter import messagebox
from DijkstraAlgorithm import Dijkstra
from BellmanAlgorithm import bellmanFord


#array = [("A",1,"B"),("A",1,"C"),("C",1,"B"),("B",1,"D"),("B",10,"E"),("B",1,"F"),("D",10,"E"),("F",1,"E")]
#Dijkstra("A","E",array)

def runTK():
    window = tk.Tk()
    def exitGraph():
        window.destroy()

    def error():
        answerEntry["text"] =  "Please fill out all entries"

    def saveData():
        saveArray = []
        saveArray.append(int(userEntry.get()))
        for i in entryArray:
            saveArray.append((i[0].get(), i[1].get(), i[2].get()))
        saveArray.append((startNodeEntry.get(), endNodeEntry.get()))
        pickle.dump(saveArray, open("saveTable.dat", "wb"))

    def startGraph():
        saveData()
        DiInputArray = []
        Di = True
        for i in entryArray:
            if i[0].get() != "":
                if int(i[1].get()) < 0:
                    Di = False
                    if varDi.get() == 1:
                        messagebox.showerror("Value Error", "Dijkstra can't run with negative values")
                        DiButton.deselect()
                        return
                if len(i[0].get()) == 0 or len(i[1].get()) == 0 or len(i[2].get()) == 0:
                    error()
                    return
                DiInputArray.append((i[0].get(), int(i[1].get()), i[2].get()))

        if len(startNodeEntry.get()) == 0 or len(endNodeEntry.get()) == 0:
            error()
            return
        if Di and varDi.get() == 1:
            dict = Dijkstra(startNodeEntry.get(), endNodeEntry.get(), DiInputArray)
            reverseArray = []
            current = dict[endNodeEntry.get()]
            while (not current.START):
                reverseArray.insert(0,current.dictValue)
                current = current.before
            reverseArray.insert(0, current.dictValue)

            s = ""
            for i in reverseArray:
                if i == reverseArray[-1]:
                    s = s + i
                    break
                s = s + i + "->"

            answerEntry['text'] = s
        if varBe.get() == 1:
            bellmanFord(startNodeEntry.get(), DiInputArray)

    def createLabel():
        window.configure(bg = "grey10")
        number = userEntry.get()
        dividedNum = 0
        if not number.isdigit():
            messagebox.showerror("Error", "Please enter an integer")
            return
        number = int(number)
        numArray = [number]
        if number > 40:
            messagebox.showerror("Value Error", "Please enter a smaller integer")
            return

        if len(deleteArray) > 0:
            for i in deleteArray:
                i.destroy()
            for i in entryArray:
                for n in i:
                    n.destroy()
            entryArray.clear()

        if number > 20:
            numArray = [20, number - 20]
            dividedNum = 1
        tempFrame = tk.Frame(bottomFrame, bg = "grey10")
        for n in range(dividedNum + 1):
            for i in range(numArray[n]):
                nodeFrame = tk.Frame(tempFrame,bg = "grey10")
                entry1 = tk.Entry(nodeFrame, width = 5, bg = "grey50", fg = "WHITE", highlightthickness = 0)
                label1 = tk.Label(nodeFrame, text = "---", bg = "grey10", fg = "WHITE")
                entry2 = tk.Entry(nodeFrame, width = 5, bg = "grey50", fg = "WHITE", highlightthickness = 0)
                label2 = tk.Label(nodeFrame, text = "-->", bg = "grey10", fg = "WHITE")
                entry3 = tk.Entry(nodeFrame, width = 5, bg = "grey50", fg = "WHITE", highlightthickness = 0)
                entryArray.append((entry1, entry2, entry3, label1, label2))
                entry1.grid(row = 0, column = 0)
                label1.grid(row = 0,column = 1)
                entry2.grid(row = 0,column = 2)
                label2.grid(row = 0,column = 3)
                entry3.grid(row = 0,column = 4)
                nodeFrame.grid(column = n, row = i, padx = 10)
                deleteArray.append(nodeFrame)
        tempFrame.pack()
        deleteArray.append(tempFrame)

    def loadData(loadedArray):
        userEntry.insert(0, loadedArray[0])
        createLabel()
        for i in range(len(entryArray)):
            entryArray[i][0].insert(0, loadedArray[i+1][0])
            entryArray[i][1].insert(0, loadedArray[i + 1][1])
            entryArray[i][2].insert(0, loadedArray[i + 1][2])
        startNodeEntry.insert(0,loadedArray[-1][0])
        endNodeEntry.insert(0,loadedArray[-1][1])



    window.resizable(False, False)
    window.configure(bg = "grey20")
    topLabel = tk.Label(window, bg = "grey20")
    entryLabel = tk.Label(topLabel, text = "Enter the amount of edge(s) you have", bg = "grey20", fg = "WHITE", font = ("Courier", 20))
    userEntry = tk.Entry(topLabel, width = 4, highlightthickness = 0, bg = "grey50", fg = "WHITE")
    entryLabel.pack(pady = 10)
    userEntry.pack(pady = (0,10))
    entryArray = []
    deleteArray = []
    userEntry.bind("<Return>", lambda x: createLabel())
    topLabel.pack(ipadx = 10, ipady = 10, fill = tk.X)
    bottomFrame = tk.Frame(window,bg = "grey10")
    bottomFrame.pack(padx = 10, pady = 10)
    Footer = tk.Frame(window, bg = "grey20")
    testLabel = tk.Label(Footer, text = "Press start to find the optimal route", bg = "grey20", fg = "WHITE")
    startButton = tk.Button(Footer, text = "Start", bg = "grey10", fg = "BLACK", font = ("Courier",20),
                            command = startGraph)
    answerEntry = tk.Label(Footer, bg = "grey9", width = 50, fg = "White", font = ("Courier", 15))
    testLabel.grid(row = 0, column = 0, columnspan = 2, pady = 10)
    tk.Label(Footer, text = "Starting Node:", bg = "grey20", fg = "White",font = ("Courier", 15)).grid(row = 1, column = 0)
    startNodeEntry = tk.Entry(Footer, width = 6, bg = "grey10", fg = "WHITE", highlightthickness = 0)
    startNodeEntry.grid(row = 1, column = 1)
    tk.Label(Footer, text = "Ending Node:", bg = "grey20", fg = "White",font = ("Courier", 15)).grid(row = 2, column = 0)
    endNodeEntry = tk.Entry(Footer, width = 6, bg = "grey10", fg = "White", highlightthickness = 0)
    endNodeEntry.grid(row = 2, column = 1)
    varDi = tk.IntVar()
    varBe = tk.IntVar()
    DiButton = tk.Checkbutton(Footer, text = "Dijkstra", variable = varDi, onvalue = 1, offvalue = 0, bg = "grey20", fg = "white")
    DiButton.grid(row = 1, column = 2, sticky = tk.W)
    BeButton = tk.Checkbutton(Footer, text = "Bellman", variable=varBe, onvalue = 1, offvalue = 0, bg = "grey20", fg = "white")
    BeButton.grid(row=2, column=2, sticky = tk.W)
    exitButton = tk.Button(Footer, text = "Exit", bg = "grey10", fg = "BLACK", font = ("Courier",20),
                            command = exitGraph)
    startButton.grid(row = 3, column = 1, columnspan = 2, pady = 10, padx = (20,0), sticky = "we")
    answerEntry.grid(row = 3, column = 3, columnspan = 2)
    exitButton.grid(row = 3, column = 0, sticky = "ew")
    Footer.pack(ipady = 10, ipadx = 10, fill = tk.X)
    loadedArray = pickle.load(open("saveTable.dat", "rb"))
    if len(loadedArray) != 0:
        loadData(loadedArray)
    window.mainloop()

runTK()



