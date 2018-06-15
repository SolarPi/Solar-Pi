#!/usr/bin/env python3

from appJar import gui
from PIL import ImageTk
from time import sleep
from threading import Thread
from SettingsRW import *

meter_show1 = getSetting("battery_meter")
animation1 = getSetting("battery_animation")

animate = animation1
percent = 50

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

def setting_watcher():
    settings_watcher = Watcher2()
    settings_watcher.run()

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
            print("Power - modified event")
            meter()  # Calls meter() when file is modified


class Watcher2:
    DIRECTORY_TO_WATCH = "/usr/local/bin/Solar Pi/Settings"  # Looks at ramdisk

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler2()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                sleep(5)
        except:
            self.observer.stop()
            print("Error")

        self.observer.join()


class Handler2(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # Take any action here when a file is first created.
            print("Received created event")  # Triggered when a file is created

        elif event.event_type == 'modified':
            # Taken any action here when a file is modified.
            print("Settings - Received modified event")
            settings()  # Calls meter() when file is modified


########################################################################################################################


def settings(first=False, animation3=False):
    global meter_show1, animation1, animate, app, mode, percent
    meter_show2 = getSetting("battery_meter")  # When triggered, fetch settings
    animation2 = getSetting("battery_animation")
    animate = animation2

    if meter_show1 != meter_show2 or first == True:  # Checks if original setting has changed
        if meter_show2 == True:  # Shows meter if hidden
            app.show()
        elif meter_show2 == False:  # Hides meter if shown
            app.hide()
        print("Do something with showing the meter")
        meter_show1 = meter_show2  # Updates original setting with current setting

    if (animation1 != animation2 and charge == True) or first == True or animation3 == True:  # Checks if original setting has changed and if we're charging
        if animation2 == True and percent < 100:  # If the animation is enabled...
            t5 = Thread(target=animation)
            t5.start()  # Start the animation
            print("setting")
        elif animation2 == False:  # If the animation is disabled...
            meter()
        print("Do something with the animation")
        animation1 = animation2

def animation():
    global animate, rec_list
    for i in range(9):
        canvas.itemconfig(rec_list[i], fill="black")
    while animate == True:
        for i in range(9):
            if animate == True:
                canvas.itemconfig(rec_list[i], fill="green")  # Fills each bar green every 1.5 secs
                sleep(1.5)
            else:
                return
        for i in range(9):
            if animate == True:
                canvas.itemconfig(rec_list[i], fill="black")  # After all bars are green, they are filled with black
            else:
                return
        sleep(1.5)
    return

def meter():
    global canvas, image, rec_list, charge, mode, animate, percent
    access = False
    while access == False:
        try:
            with open("../ramdisk/power", "r") as file:  # Attempts to open power file
                data = file.readlines()

            data = data[0]
            data = data.split(",")
            access = True

        except IOError:  # If file opening fails, try again - ramdisk may not be created yet or Power Daemon isn't running
            sleep(1)

    percent = float(data[0])  # Takes percentage
    mode = data[1]  # Gets power mode

    if mode == "B":  # If battery powered
        if charge == True:  # If battery powered and was charging
            charge = False
            animate = False
            canvas.itemconfig(image, state="hidden")  # Hide image
            for i in range(10):  # If battery was charging, attempt to update meter once animation has stopped
                meter_change(percent)
                sleep(1.5)
        else:
            meter_change(percent)  # If RPi is battery powered
    
    elif mode == "C":
        if charge == True:
            meter_change(percent, charge)
        else:
            charge = True
            meter_change(percent, charge)
            canvas.itemconfig(image, state="normal")  # Shows image
            settings(animation3=True)

        if percent >= 100 and animate == True:
            animate = False
            sleep(1)
            meter_change(percent, charge)
        elif percent < 100 and animate == True:
            settings(animation3=True)

def meter_fill(num, colour="black"):
    for i in range(num):
        canvas.itemconfig(rec_list[i], fill="green")
        bar_list.remove(i)
    for i in bar_list:
        canvas.itemconfig(rec_list[i], fill=colour)

def meter_change(percent, charge=False):
    global change, canvas, image, rec_list, bar_list
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

    elif percent > 80 and percent < 90:  # 86.6
        meter_fill(8)

    elif percent > 70 and percent < 80:  # 73.3
        meter_fill(7)

    elif percent > 55 and percent < 70:  # 60
        meter_fill(6)

    elif percent > 45 and percent < 55:  # 46.6
        meter_fill(5)

    elif percent > 25 and percent < 45:  # 33.3
        if charge == True:
            meter_fill(4)
        else:
            meter_fill(4, "#a5dd24")

    elif percent > 15 and percent < 30:  # 20
        if charge == True:
            meter_fill(3)
        else:
            meter_fill(3, "#ddc724")

    elif percent > 4 and percent < 7:  # 6.6
        if charge == True:
            meter_fill(2)
        else:
            meter_fill(2, "#dd6524")

    elif percent < 4:  # -6.6
        if charge == True:
            colour = "green"
        else:
            colour = "#dd4125"
        canvas.itemconfig(rec_list[0], fill=colour)
        bar_list.remove(0)
        for i in bar_list:
            canvas.itemconfig(rec_list[i], fill="black")

def hider():
    global meter_show1
    sleep(1)
    if meter_show1 == False:
        app.hide()

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

    t3 = Thread(target=setting_watcher)
    t3.start()

    t4 = Thread(target=hider)
    t4.start()

    settings(first=True)
    meter()
