#!/usr/bin/env python3
# Programming Search Application

# Import Modules
from appJar import gui
from subprocess import Popen
import webbrowser
from SettingsRW import *
from time import sleep
from threading import Thread

theme1 = getSetting("theme")

try:
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler

    class Watcher:
        DIRECTORY_TO_WATCH = "/usr/local/bin/Solar Pi/Settings"  # Looks at settings

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
                settings()  # Calls meter() when file is modified

except:
    pass

def settings(first=False):
    global app, theme1, theme2

    theme2 = getSetting("theme")

    if theme1 != theme2 or first == True:
        if theme2 == "Solar Pi":
            app.setTtkTheme("plastik")
            app.setTtkTheme("clam")
            # app.ttkStyle.configure(".", font="10")
            # Highlighted button
            app.ttkStyle.configure("H.TButton", background="#324581", foreground="white", bordercolor="#687396")
            app.ttkStyle.map("H.TButton", background=[("pressed", "#172141"), ("active", "#4059a9")])

            # Regular button
            app.ttkStyle.configure("TButton", background="#dbdce2", bordercolor="#687396")

            # Radiobutton
            app.ttkStyle.map("TRadiobutton", background=[("active", "white")])

            # LabelFrame
            app.ttkStyle.configure("TLabelframe", bordercolor="#687396")

            app.showButton("Go")
            app.hideButton("go")

            app.setBg("white")
            app.ttkStyle.configure(".", foreground="black")

        elif theme2 == "black":
            app.setTtkTheme(theme2)
            app.showButton("Go")
            app.hideButton("go")

        else:
            app.setTtkTheme(theme2)
            app.ttkStyle.map("TRadiobutton", background=[("active", "white")])
            app.ttkStyle.configure(".", background="white", foreground="black")
            app.setLabelFrameStyle("Choose a Programming Language:", "TFrame")

            app.showButton("go")
            app.hideButton("Go")

            app.setBg("white")
            app.setFg("black")

        app.setFont(family="pibotolt")
        app.ttkStyle.configure(".", font="pibotolt")
        app.ttkStyle.configure("TButton", font=("open sans", 12, "normal"))
        app.ttkStyle.configure("TLabelframe.Label", font=("open sans", 12, "normal"))
        app.ttkStyle.configure("Frame.TLabel", font=("open sans", 12, "normal"))

        theme1 = theme2


# Handlers
def ButtonHandler(press):
    option = app.getRadioButton("language")
    if press == "Exit ":
        quit()
    elif press.lower() == "go":
        if option == "Scratch (Easy)":
            Popen("/usr/local/bin/Solar Pi/Resources/Launchers/scratch launcher.sh")
        elif option == "Python (Intermedium/Hard)":
            webbrowser.get("chromium-browser").open("http://localhost/Advanced-Things/python/index.html")  # Launch Python starter guide
            webbrowser.get("chromium-browser").open("http://localhost:81")  # Launch A Byte of Python
            Popen("/usr/local/bin/Solar Pi/Resources/Launchers/thonny launcher.sh")
        elif option == "Java (Hard)":
            Popen("/usr/local/bin/Solar Pi/Resources/Launchers/bluej launcher.sh")
            webbrowser.get("chromium-browser").open("http://localhost:82/java/index.htm")  # Launch Java Guide
        
    elif press == " More Info  ":
        if option == "Scratch (Easy)":
            app.infoBox("Scratch", "Scratch teaches you the logic of programming in an easy to understand way. Great if you're a beginner!.")
        elif option == "Python (Intermedium/Hard)":
            app.infoBox("Python", "Python is one of the most commonly used programming languages. It was actually used to code this program! Python is beginner friendly, so it's a good one to start out with.")
        elif option == "Java (Hard)":
            app.infoBox("Java", "Java is a bit more complicated than Python, so it's a good challenge if you want to take your skills further.")


def ToolbarHandler(press):
    if press == "Help":
        webbrowser.get("chromium-browser").open("http://localhost/solar-pi-apps/index.html#start-programming")  # Launch guides here

# GUI Parameters
with gui("Start Coding", useTtk=True) as app:  # 400x320 # "420x290"
    app.setResizable(False)

    # Menu
    #app.addMenuList("Applications", ["Solar Pi Home", "Leafpad"], MenuHandler)
    #app.addMenuList("IDEs", ["Scratch", "Python IDLE", "Thonny Python", "Java"], MenuHandler)

    # Widgets

    app.setPadding(10, 10)
    app.addImage("solar_pi", "../Resources/Images/Solar Pi text small.gif")

    with app.labelFrame("Choose a Programming Language:"):
        app.setSticky("ew")
        app.setPadding(10, 5)
        app.addLabel("info", "Click 'More Info' to see a short explanation, and click 'Go' to launch\nthe coding program and view some resources that might help you.")

        app.addHorizontalSeparator()

        app.addRadioButton("language", "Scratch (Easy)")
        app.addRadioButton("language", "Python (Intermedium/Hard)")
        app.addRadioButton("language", "Java (Hard)")

    programming = app.addLabel("programming", "Choose a Programming Language:")
    app.setLabelStyle("programming", "Frame.TLabel")
    app.getLabelFrameWidget("Choose a Programming Language:").config(labelwidget=programming)

    with app.frame("frame"):
        app.setPadding(10, 10)

        app.addNamedButton("Go  ", "Go", ButtonHandler, 0, 0)
        app.setButtonImage("Go", "../Resources/Images/go white.gif", align="right")
        app.setButtonStyle("Go", "H.TButton")

        app.addNamedButton("Go  ", "go", ButtonHandler, 0, 0)
        app.setButtonImage("go", "../Resources/Images/go black.gif", align="right")
        app.setButtonStyle("go", "H.TButton")

        if theme1 == "Solar Pi" or theme1 == "black":
            app.hideButton("go")
        else:
            app.hideButton("Go")

        #app.addImageButton("Go  ", ButtonHandler, "../Resources/Images/go white.gif", 0, 0, align="right")
        #app.setButtonStyle("Go  ", "H.TButton")

        #app.addImageButton("Go  ", ButtonHandler, "../Resources/Images/go black.gif", 0, 0, align="right")

        app.addImageButton(" More Info  ", ButtonHandler, "../Resources/Images/more info.gif", 0, 1, align="right")
        app.addImageButton("Exit ", ButtonHandler, "../Resources/Images/cross.gif", 0, 2, align="right")

    if theme1 != "black":
        app.setBg("white")

    try:
        w = Watcher()
        t = Thread(target=w.run)
        t.start()
    except:
        pass

    settings(True)
