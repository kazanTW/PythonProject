import tkinter as tk
import pathlib
import sys
import os

def blank(string):
    blank = tk.Frame(string, width=20, height=50)
    blank.pack()

flag = 0
node = 0
def numWork():
    global flag
    global node
    file = pathlib.Path('~/temp.txt').touch(exist_ok=True)
    temp = pathlib.Path('~/temp.txt').expanduser()

def numInt(n, m):
    try:
        if m[0] == '+':
            string = int(n) + int(m[1:])
        elif m[0]== '-':
            string = int(n) - int(m[1:])
        elif m[0] == 'x':
            string = int(n) * int(m[1:])
        elif m[0] == '/':
            string = int(n) / int(m[1:])

        temp = pathlib.Path('~/temp.txt').expanduser()
        temp.write_text('\n' + str(string) + '\n')
    except:
        temp = pathlib.Path('~/temp.txt').expanduser()
        temp.write_text('\nError')

def numFloat(n, m):
    try:
        if m[0] == '+':
            string = float(n) + float(m[1:])
        elif m[0]== '-':
            string = float(n) - float(m[1:])
        elif m[0] == 'x':
            string = float(n) * float(m[1:])
        elif m[0] == '/':
            string = float(n) / float(m[1:])
        
        if flag == 0:
            temp = pathlib.Path('~/temp.txt').expanduser()
            temp.write_text('\n' + str(string) + '\n')
        else:
            temp = pathlib.Path('~/temp.txt').expanduser()
            temp.write_text('\n' + str(string))
    except:
        temp = pathlib.Path('~/temp.txt').expanduser()
        temp.write_text('\nError')

def decimal(n):