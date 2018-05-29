#!/usr/bin/env python3
# Programming Search Application

# Import Modules
from appJar import gui
from subprocess import Popen
import webbrowser
from SettingsRW import *

theme = getSetting("theme")

custom = theme == "Solar Pi"

# Handlers
def ButtonHandler(press):
    option = app.getRadioButton("language")
    if press == "Exit ":
        quit()
    elif press == "Go  ":
        if option == "Scratch (Easy)":
            Popen("/usr/local/bin/Solar Pi/Resources/Launchers/scratch launcher.sh")
        elif option == "Python (Intermedium/Hard)":
            webbrowser.get("chromium-browser").open("http://localhost/Advanced-Things/python/index.html")  # Launch Python starter guide
            webbrowser.get("chromium-browser").open("http://localhost:81")  # Launch A Byte of Python
            Popen("/usr/local/bin/Solar Pi/Resources/Launchers/thonny launcher.sh")
        elif option == "Java (Hard)":
            Popen("/usr/local/bin/Solar Pi/Resources/Launchers/bluej Launcher.sh")
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

    if custom == True:
        app.setTtkTheme("plastik")
        app.setTtkTheme("clam")
        #app.ttkStyle.configure(".", font="10")
        # Highlighted button
        app.ttkStyle.configure("H.TButton", background="#324581", foreground="white", bordercolor="#687396")
        app.ttkStyle.map("H.TButton", background=[("pressed", "#172141"), ("active", "#4059a9")])

        # Regular button
        app.ttkStyle.configure("TButton", background="#dbdce2", bordercolor="#687396")

        # Radiobutton
        app.ttkStyle.map("TRadiobutton", background=[("active", "white")])

        # LabelFrame
        app.ttkStyle.configure("TLabelframe", bordercolor="#687396")
    else:
        app.setTtkTheme(theme)
        if theme != "black":
            app.ttkStyle.configure(".", background="white", foreground="black")
            app.ttkStyle.map("TRadiobutton", background=[("active", "white")])

    app.setFont(family="piboto")
    app.ttkStyle.configure(".", font=("piboto"))

    # Menu
    #app.addMenuList("Applications", ["Solar Pi Home", "Leafpad"], MenuHandler)
    #app.addMenuList("IDEs", ["Scratch", "Python IDLE", "Thonny Python", "Java"], MenuHandler)

    # Widgets

    app.setPadding(10, 10)
    app.addImage("solar_pi", "../Resources/Images/Solar Pi text small.gif")

    with app.labelFrame("Choose a Programming Language:"):
        app.setSticky("ew")
        app.setPadding(10, 5)
        app.addLabel("info", "Click 'More Info' to see a short explanation, and click 'Go' to\nlaunch the IDE and see some resources that might help you.")

        app.addHorizontalSeparator()

        app.addRadioButton("language", "Scratch (Easy)")
        app.addRadioButton("language", "Python (Intermedium/Hard)")
        app.addRadioButton("language", "Java (Hard)")

    with app.frame("frame"):
        app.setPadding(10, 10)
        if custom == True or theme == "black":
            app.addImageButton("Go  ", ButtonHandler, "../Resources/Images/go white.gif", 0, 0, align="right")
            app.setButtonStyle("Go  ", "H.TButton")
        else:
            app.addImageButton("Go  ", ButtonHandler, "../Resources/Images/go black.gif", 0, 0, align="right")
            app.setLabelFrameStyle("Choose a Programming Language:", "TFrame")
        app.addImageButton(" More Info  ", ButtonHandler, "../Resources/Images/more info.gif", 0, 1, align="right")
        app.addImageButton("Exit ", ButtonHandler, "../Resources/Images/cross.gif", 0, 2, align="right")

    if theme != "black":
        app.setBg("white")
