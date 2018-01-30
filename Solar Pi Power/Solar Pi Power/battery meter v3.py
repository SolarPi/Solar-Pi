from appJar import gui
from PIL import Image, ImageTk
from time import sleep

#############################################################
#  Change rectangle colour:                                 #
#  canvas.itemconfig(l[index of rectangle], fill="colour")  #
#############################################################

def show():
    sleep(1)
    app.show()

with gui(size="60x35") as app:
    #app.setSticky("nesw")
    app.setGuiPadding(0, 0)
    app.hideTitleBar()
    app.setBg("white")
    canvas = app.addCanvas("c")
    canvas.config(bd=0, highlightthickness=0)

    l = []
    count = 0
    for i in range(9):
        r = app.addCanvasRectangle("c", count, 0, 6, 35, fill="green", width=0)
        l.append(r)
        count += 6
    app.addCanvasRectangle("c", 54, 11, 7, 15, fill="grey", width=0)
    app.addCanvasImage("c", 27, 19, ImageTk.PhotoImage(file="lightning-bolt2.png"))
    app.setCanvasOverFunction("c", [app.hide, show])
