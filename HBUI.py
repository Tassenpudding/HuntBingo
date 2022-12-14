import tkinter.messagebox
from random import random
from tkinter import *

class HBUI:
    tk = Tk()
    buttonsWidth, buttonsHeight = 5, 5
    buttons = [5, 5]
    bingocases = []
    bingocaseUsed = []
    bingo = False

    def GetBingoText(self):
        index = int((len(self.bingocases) - 1) * random())
        if self.bingocaseUsed[index]:
            return self.GetBingoText()
        self.bingocaseUsed[index] = True
        return self.bingocases[index]

    def __init__(self, __bingocases : list):
        self.bingocases = __bingocases
        self.bingocaseUsed = [False for i in range(len(__bingocases))]
        self.buttons = [["" for x in range(self.buttonsWidth)] for y in range(self.buttonsHeight)]
        self.tk.resizable(False, False)

    def CheckBingo(self, x, y):
        bingoX = True
        bingoY = True
        bingoDiag1 = True
        bingoDiag2 = True
        for i in range(0, 5):
            bingoX &= self.buttons[x][i]['state'] == "disabled"
            bingoY &= self.buttons[i][y]['state'] == "disabled"
            bingoDiag1 &= self.buttons[i][i]['state'] == "disabled"
            bingoDiag2 &= self.buttons[i][4 - i]['state'] == "disabled"

        if not self.bingo and (bingoX or bingoY or bingoDiag1 or bingoDiag2):
            tkinter.messagebox.showinfo("Erfolg", "Ein wildes Bingo")
            self.bingo = True


    def ButtonCallback(self, x, y):
        currentButton = self.buttons[x][y]
        currentButton.configure(state=DISABLED)
        currentButton.configure(bg = "lightgreen")
        self.CheckBingo(x, y)

    def CreateWindow(self):
        self.tk.title('Hunt Bingo')
        self.tk.geometry('500x500')

        for x in range(0, 5):
            for y in range(0, 5):
                bingotext = self.GetBingoText()
                self.buttons[x][y] = Button(self.tk, text = bingotext, width = 13, height = 5,command=lambda x=x, y=y: self.ButtonCallback(x,y), wraplength = 90)
                self.buttons[x][y].place(x=x*100,y=y*100)

        self.tk.mainloop()
