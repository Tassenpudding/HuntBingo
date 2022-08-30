import sys, getopt
import tkinter.messagebox
from tkinter import *
from HBUI import HBUI
import logging

def read_file(path):
    bingocases = []

    f = open(path, "r", encoding = 'utf8')
    lines = f.readlines()
    for line in lines:
        line = line.replace("\n","")
        bingocases.append(line)

    logging.info(f"file ({path}) read successfully")
    logging.info(f"found {len(bingocases)} entries")
    return bingocases

def parseArgs(argv):
    try:
        optlist, args = getopt.getopt(argv[1:], "f:", ["file="])
    except getopt.GetoptError:
        logging.error("couldn't parse console arguments")
        sys.exit(2)

    path = ""

    for opt, arg in optlist:
        if opt == "-f":
            path = arg

    logging.info("filename {path} fetched from argument list")

    return path #, arg2, arg3

def main():
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
    # handle arguments
    path = parseArgs(sys.argv)
    # fetch list of all possible bingo-events from path
    bingocases = read_file(path)
    # create UI and feed bingo-events into object
    hbui = HBUI(bingocases)
    hbui.CreateWindow()

if __name__=="__main__":
    main()