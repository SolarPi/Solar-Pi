from appJar import gui
from time import sleep
from threading import Thread
from PIL import Image, ImageTk

def over(param):
    program.hide()

def leave(param):
    sleep(1)
    program.show()


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
    global change
    try:
        with open("../ramdisk/power", "r") as file:
            data = file.readlines()
        data = data[0]
        data = data.split(",")
        percent = float(data[0])
        change = False
        if data[1] == "B":
            program.hideCanvas("canvas")
            #program.hideLabel("flash")
            if percent >= 100:  # 100
                program.setLabelBg(["1", "2", "3", "4", "5", "6", "7", "8", "9"], "green")
            elif percent > 80 and percent < 90:  # 87.5
                program.setLabelBg(["1", "2", "3", "4", "5", "6", "7", "8"], "green")
                program.setLabelBg("9", "black")
            elif percent > 70 and percent < 80:  # 75
                program.setLabelBg(["1", "2", "3", "4", "5", "6", "7"], "green")
                program.setLabelBg(["8", "9"], "black")
            elif percent > 55 and percent < 70:  # 62
                program.setLabelBg(["1", "2", "3", "4", "5", "6"], "green")
                program.setLabelBg(["7", "8", "9"], "black")
            elif percent > 45 and percent < 55:  # 50
                program.setLabelBg(["1", "2", "3", "4", "5"], "green")
                program.setLabelBg(["6", "7", "8", "9"], "black")
            elif percent > 25 and percent < 45:  # 37
                program.setLabelBg(["1", "2", "3", "4"], "#a5dd24")
                program.setLabelBg(["5", "6", "7", "8", "9"], "black")
            elif percent > 20 and percent < 30:  # 25
                program.setLabelBg(["1", "2", "3"], "#ddc724")
                program.setLabelBg(["4", "5", "6", "7", "8", "9"], "black")
            elif percent > 7 and percent < 17:  # 12.5
                program.setLabelBg(["1", "2"], "#dd6524")
                program.setLabelBg(["3", "4", "5", "6", "7", "8", "9"], "black")
            elif percent > 4 and percent < 7:  # 5.5
                program.setLabelBg("1", "#dd4125")
                program.setLabelBg(["2", "3", "4", "5", "6", "7", "8", "9"], "black")
            elif percent < 4:
                program.setLabelBg(["1", "2", "3", "4", "5", "6", "7", "8", "9"], "black")

        elif data[1] == "C":
            #program.setLabelBg(["4", "5", "6", "7", "8", "9"], "black")
            #program.setLabelBg(["1", "2", "3"], "orange")
            #program.showLabel("flash")
            program.showCanvas("canvas")
            change = True
            t2 = Thread(target=label_change)
            t2.start()

    except IOError:
        sleep(1)
        meter()
            


def batt_watcher():
    w = Watcher()
    w.run()

change = False

def label_change():
    global change
    while change == True:
        program.setLabelBg(["1", "2", "3", "4", "5", "6", "7", "8", "9"], "black")
        for i in range(1, 10):
            program.setLabelBg(str(i), "green")
            sleep(1.5)
        program.setLabelBg(["1", "2", "3", "4", "5", "6", "7", "8", "9"], "black")
        sleep(1.5)
        


with gui("meter", "85x40") as program:
    program.hideTitleBar()
    program.setLocation(0, 562)
    program.setSticky("nesw")
    program.setGuiPadding(0, 0)
    with program.frame("frame"):
        #program.setPadding(1, 1)
        program.setBg("white")

        for i in range(1, 10):
            program.addLabel(str(i), "", 0, i-1)
            program.setLabelBg(str(i), "green")

        program.addLabel("10", " ", 0, 9)
        program.setLabelBg("10", "grey")
        program.setLabelSticky("10", "w")

##        program.addFlashLabel("flash", "", 0, 0, colspan=9)
##        program.setLabelSticky("flash", "nesw")
##        program.setLabelBg("flash", "green")
##        program.hideLabel("flash")

        #program.addImage("bolt", "../Resources/Images/lightning bolt.gif", 0, 2, colspan=5)
        #program.zoomImage("bolt", -7)
        #program.setImageSticky("bolt", "")
        #program.setImageBg("bolt", "black") #"#21c62c"
        #program.hideImage("bolt")

        program.addCanvas("canvas", 0, 2, colspan=5)
        #program.setCanvasBg("canvas", "black")
        program.addCanvasImage("canvas", 35, 20, ImageTk.PhotoImage(file="../Resources/Images/lightning bolt.gif"))
        program.hideCanvas("canvas")

    program.setFrameOverFunction("frame", [over, leave])
    meter()
    

    t = Thread(target=batt_watcher)
    t.start()
