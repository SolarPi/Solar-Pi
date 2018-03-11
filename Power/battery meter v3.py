#!/usr/bin/env python3

from appJar import gui
from PIL import ImageTk
from time import sleep
from threading import Thread


#############################################################
#  Change rectangle colour:                                 #
#  canvas.itemconfig(l[index of rectangle], fill="colour")  #
#############################################################

################################################################################################
#  Code for Watcher from (rest of code is my own):                                             #
#  https://www.michaelcho.me/article/using-pythons-watchdog-to-monitor-changes-to-a-directory  #
################################################################################################

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


def batt_watcher():
    # Create instance of Watcher class
    w = Watcher()
    w.run()

class Watcher:
    DIRECTORY_TO_WATCH = "/usr/local/bin/Solar Pi/ramdisk"  # Looks at ramdisk

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
            print("Received created event")  # Triggered when a file is created

        elif event.event_type == 'modified':
            # Taken any action here when a file is modified.
            print("Received modified event")
            meter()  # Calls meter() when file is modified


def meter():
    global canvas, image, rec_list, charge
    try:
        with open("../ramdisk/power", "r") as file:  # Attempts to open power file
            data = file.readlines()
            
    except IOError:  # If file opening fails, try again - ramdisk may not be created yet or Power Daemon isn't running
        sleep(1)
        meter()

    data = data[0]
    data = data.split(",")
    percent = float(data[0])  # Takes percentage
    mode = data[1]  # Gets power mode

    if mode == "B":  # If battery powered
        if charge == True:  # If battery powered and was charging
            charge = False
            canvas.itemconfig(image, state="hidden")  # Hide image
            for i in range(10):  # If battery was charging, attempt to update meter once animation has stopped
                meter_change(percent)
                sleep(1.5)
        else:
            meter_change(percent)  # If RPi is battery powered
    
    elif mode == "C":
        if charge == True:
            pass
        else:
            charge = True
            t1 = Thread(target=charging)  # If RPi is charging, start animation
            t1.start()


def meter_change(percent):
    global change, canvas, image, rec_list
    bar_list = []  # Create list for bars in meter
    for i in range(9):
        bar_list.append(i)  # Construct list with numbers from 0 to 8

    # TODO: Test algorithm with bar_list

    #########################################
    #  Fills meter with appropriate colour  #
    #########################################

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
    global charge, rec_list
    for i in range(9):
        canvas.itemconfig(rec_list[i], fill="black")
    while charge == True:
        canvas.itemconfig(image, state="normal")  # Shows image
        for i in range(9):
            if charge == True:
                canvas.itemconfig(rec_list[i], fill="green")  # Fills each bar green every 1.5 secs
                sleep(1.5)
            else:
                break
        for i in range(9):
            if charge == True:
                canvas.itemconfig(rec_list[i], fill="black")  # After all bars are green, they are filled with black
            else:
                break
        sleep(1.5)
    

def show():
    sleep(1)
    app.show()

charge = False

##########################
#  GUI of battery meter  #
##########################

with gui(size="60x35") as app:
    # Set GUI options
    app.setGuiPadding(0, 0)
    app.setLocation(0, 565)
    app.hideTitleBar()
    app.setBg("white")
    canvas = app.addCanvas("c")
    canvas.config(bd=0, highlightthickness=0)

    rec_list = []
    count = 0
    for i in range(9):
        r = app.addCanvasRectangle("c", count, 0, 6, 35, fill="green", width=0)  # Add rectangles for bars
        rec_list.append(r)  # Adds rectangles to list
        count += 6
    app.addCanvasRectangle("c", 54, 11, 7, 15, fill="grey", width=0)
    image = app.addCanvasImage("c", 27, 19, ImageTk.PhotoImage(file="../Resources/Images/lightning-bolt2.png"))  # Charging image
    app.setCanvasOverFunction("c", [app.hide, show])  # Hide window when mouse over it

    canvas.itemconfig(image, state="hidden")  # Hide image

    t2 = Thread(target=batt_watcher)
    t2.start()  # Start the battery watcher in a new thread

    meter()
