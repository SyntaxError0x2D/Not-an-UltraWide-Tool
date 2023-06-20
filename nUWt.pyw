from tkinter import *
import pygetwindow as gw
import ctypes, sys, fileMangament as fm

global scaling, res, mv2, titleName

if fm.isFile():
    settings = fm.readSettings() 
else: fm.warn_noFile() ; sys.exit()

scaling = settings["scaling"]
res = settings["res"]
mv2 = settings["move_to"]
titleName = "nUWt - 16:9-fy"

override_names = ["NVIDIA GeForce Overlay", "Program Manager", "Microsoft Text Input Application", titleName]

GWL_STYLE = -16 # Constants for window styles
WS_CAPTION = 0x00C00000  # Caption style

def getOptions():
    windows = gw.getAllWindows()
    ls: list = []
    for w in windows:
        if w.title and w.title not in override_names:
            ls.append([w._hWnd, w.title])
    return(ls)

def check(hwnd):
    if hwnd in [i._hWnd for i in gw.getAllWindows()]: return(True)
    return(False)

def sauce(hwnd, mode): # Get the handle of the window you want to modify
    if not check(hwnd): return() 

    window = gw.Window(hwnd)
    #ogSize = window.size


    ### AI GENERATED!

    # Get the current window style
    style = ctypes.windll.user32.GetWindowLongPtrW(hwnd, GWL_STYLE)

    # Remove the caption style
    if mode: style = style & ~WS_CAPTION
    else: style = style | WS_CAPTION
    # Update the window style
    ctypes.windll.user32.SetWindowLongPtrW(hwnd, GWL_STYLE, style)

    # Update the window's non-client area to reflect the style change
    ctypes.windll.user32.SetWindowPos(hwnd, None, 0, 0, 0, 0, 0x0002 | 0x0040)

   # gw.Window(hwnd).size = ogSize

    window.moveTo(mv2[0],mv2[1])
    window.size = (res[0]//scaling, res[1]//scaling)

global ls
ls = getOptions()

def refresh(lsB, lastLs):
    global ls
    ls = getOptions()
    if lastLs == ls: return()
    
    lsB.delete(0, last=END)

    for item in ls:
        lsB.insert(END, item)


def refreshLoop(lsB, win):
    refresh(lsB, ls)
    win.after(250, lambda : refreshLoop(lsB, win))


win = Tk()
win.title(titleName)
win.geometry("400x300")

lsBox = Listbox(win, bg="#202123", font="arial 12", fg="white")
for item in ls:
    lsBox.insert(END, item)

refresh(lsBox, ls)

lsBox.place(x=0,y=0,relheight=1,relwidth=1)

win.bind("<Return>", lambda _ : 
         sauce(ls[lsBox.curselection()[0]][0], True))

win.bind("<BackSpace>", lambda _ :
         sauce(ls[lsBox.curselection()[0]][0], False))

win.after(250, lambda : refreshLoop(lsBox, win))
win.mainloop()
