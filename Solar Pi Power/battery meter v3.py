from appJar import gui
from PIL import Image, ImageTk
from time import sleep
from threading import Thread

# TODO: Test everything!!

#############################################################
#  Change rectangle colour:                                 #
#  canvas.itemconfig(l[index of rectangle], fill="colour")  #
#############################################################

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class Watcher:
    DIRECTORY_TO_WATCH = "/usr/local/bin/Solar Pi/ramdisk"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                sleep(5)
        except:
            self.observer.stop()
            print("Error")

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # Take any action here when a file is first created.
            print("Received created event")

        elif event.event_type == 'modified':
            # Taken any action here when a file is modified.
            print("Received modified event")
            meter()


def meter():
    global change, canvas, image, rec_list
    try:
        with open("../ramdisk/power", "r") as file:
            data = file.readlines()
        data = data[0]
        data = data.split(",")
        percent = float(data[0])
        if change == True:
            change = False
            for i in range(10):
                meter_change(percent)
                sleep(1)
        else:
            change = False
        
        elif data[1] == "C":
            global change
            change = True
            t1 = Thread(target=charging)
            t1.start()
            
    except IOError:
        sleep(1)
        meter()

def meter_change(percent):
    global change, canvas, image, rec_list
    bar_list = []
    for i in range(9):
        bar_list.append(i)

    if data[1] == "B":
        canvas.itemconfig(image, state="hidden")

        # TODO: Test algorithm with bar_list
        if percent >= 100:  # 100
            for i in range(9):
                canvas.itemconfig(rec_list[i], fill="green")
        elif percent > 80 and percent < 90:  # 87.5
            for i in range(8):
                canvas.itemconfig(rec_list[i], fill="green")
                bar_list.remove(i)
            for i in bar_list:
                canvas.itemconfig(rec_list[i], fill="black")
        elif percent > 70 and percent < 80:  # 75
            for i in range(7):
                canvas.itemconfig(rec_list[i], fill="green")
                bar_list.remove(i)
            for i in bar_list:
                canvas.itemconfig(rec_list[i], fill="black")
        elif percent > 55 and percent < 70:  # 62
            for i in range(6):
                canvas.itemconfig(rec_list[i], fill="green")
                bar_list.remove(i)
            for i in bar_list:
                canvas.itemconfig(rec_list[i], fill="black")
        elif percent > 45 and percent < 55:  # 50
            for i in range(5):
                canvas.itemconfig(rec_list[i], fill="green")
                bar_list.remove(i)
            for i in bar_list:
                canvas.itemconfig(rec_list[i], fill="black")
        elif percent > 25 and percent < 45:  # 37
            for i in range(4):
                canvas.itemconfig(rec_list[i], fill="#a5dd24")
                bar_list.remove(i)
            for i in bar_list:
                canvas.itemconfig(rec_list[i], fill="black")
        elif percent > 20 and percent < 30:  # 25
            for i in range(3):
                canvas.itemconfig(rec_list[i], fill="#ddc724")
                bar_list.remove(i)
            for i in bar_list:
                canvas.itemconfig(rec_list[i], fill="black")
        elif percent > 7 and percent < 17:  # 12.5
            for i in range(2):
                canvas.itemconfig(rec_list[i], fill="#dd6524")
                bar_list.remove(i)
            for i in bar_list:
                canvas.itemconfig(rec_list[i], fill="black")
        elif percent > 4 and percent < 7:  # 5.5
            canvas.itemconfig(rec_list[0], fill="#dd4125")
            bar_list.remove(0)
            for i in bar_list:
                canvas.itemconfig(rec_list[i], fill="black")
        elif percent < 4:  # Basically empty
            for i in range(9):
                canvas.itemconfig(rec_list[i], fill="black")


def charging():
    global change, rec_list
    while change == True:
        canvas.itemconfig(image, state="normal")
            for i in range(9):
                canvas.itemconfig(rec_list[i], fill="green")
                sleep(1.5)
            for i in range(9):
                canvas.itemconfig(rec_list[i], fill="black")
            sleep(1.5)
    

def show():
    sleep(1)
    app.show()

def batt_watcher():
    w = Watcher()
    w.run()

change = False

with gui(size="60x35") as app:
    #app.setSticky("nesw")
    app.setGuiPadding(0, 0)
    app.hideTitleBar()
    app.setBg("white")
    canvas = app.addCanvas("c")
    canvas.config(bd=0, highlightthickness=0)

    rec_list = []
    count = 0
    for i in range(9):
        r = app.addCanvasRectangle("c", count, 0, 6, 35, fill="green", width=0)
        rec_list.append(r)
        count += 6
    app.addCanvasRectangle("c", 54, 11, 7, 15, fill="grey", width=0)
    image = app.addCanvasImage("c", 27, 19, ImageTk.PhotoImage(file="lightning-bolt2.png"))
    app.setCanvasOverFunction("c", [app.hide, show])

    canvas.itemconfig(image, state="hidden")

    t2 = Thread(target=batt_watcher)
    t2.start()
