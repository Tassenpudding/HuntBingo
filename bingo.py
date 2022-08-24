import sys, getopt
import tkinter.messagebox
from tkinter import *

from HBUI import HBUI

def read_file(path):
    bingocases = []

    f = open(path,"r")
    lines = f.readlines()
    for line in lines:
        line = line.replace("\n","")
        bingocases.append(line)

    return bingocases

def parseArgs(argv):
    try:
        optlist, args = getopt.getopt(argv[1:], "f:", ["file="])
    except getopt.GetoptError:
        print('error when parsing args')
        sys.exit(2)

    path = ""

    for opt, arg in optlist:
        if opt == "-f":
            path = arg

    return path #, arg2, arg3

def main():
    # handle arguments
    path = parseArgs(sys.argv)
    # fetch list of all possible bingo-events from path
    bingocases = read_file(path)
    # create UI and feed bingo-events into object
    hbui = HBUI(bingocases)
    hbui.CreateWindow()

if __name__=="__main__":
    main()