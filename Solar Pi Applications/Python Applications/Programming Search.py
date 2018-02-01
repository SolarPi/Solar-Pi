#!/usr/bin/env python3
# Programming Search Application

# Import Modules
from appJar import *
from os import system
from subprocess import Popen
import webbrowser

with open("../../Solar Pi Settings/Settings.ini", "r") as file:
    data = file.readlines()[0]
data = data.split(",")
theme = data[3]

custom = theme == "Solar Pi"

# Handlers
def ButtonHandler(press):
    option = program.getRadioButton("language")
    if press == "Exit ":
        quit()
    elif press == "Go  ":
        if option == "Scratch (Easy)":
            Popen("/usr/local/bin/Solar Pi/Resources/Launchers/Scratch Launcher.sh")
        elif option == "Python (Intermedium/Hard)":
            webbrowser.get("chromium-browser").open("http://localhost/Advanced-Things/python/index.html")  # Launch Python starter guide
            webbrowser.get("chromium-browser").open("http://localhost:81")  # Launch A Byte of Python
            Popen("/usr/local/bin/Solar Pi/Resources/Launchers/IDLE Launcher.sh")
        elif option == "Java (Hard)":
            Popen("/usr/local/bin/Solar Pi/Resources/Launchers/BlueJ Launcher.sh")
            webbrowser.get("chromium-browser").open("http://localhost:82/java/index.htm")  # Launch Java Guide
        
    elif press == " More Info  ":
        if option == "Scratch (Easy)":
            program.infoBox("Scratch", "Scratch teaches you the logic of programming in an easy to understand way. This will set a firm foundation for beginners.")
        elif option == "Python (Intermedium/Hard)":
            program.infoBox("Python", "Python is one of the most commonly used programming languages. It was actually used to code this program! The syntax of Python is very simple, and you can start off by making simple command line programs and move on to learn OOP (Object Oriented Programming) in this too.")
        elif option == "Java (Hard)":
            program.infoBox("Java", "Java is a high level OOP (Object Oriented Programming) language. You can write web apps as well as regular applications with this.")

def MenuHandler(press):
    if press == "Solar Pi Home":
        Popen("/usr/local/bin/Solar Pi/Resources/Launchers/Welcome Launcher.sh")
    elif press == "Leafpad":
        Popen("/usr/local/bin/Solar Pi/Resources/Launchers/Leafpad Launcher.sh")
    elif press == "Scratch":
        Popen("/usr/local/bin/Solar Pi/Resources/Launchers/Scratch Launcher.sh")
    elif press == "Python IDLE":
        Popen("/usr/local/bin/Solar Pi/Resources/Launchers/IDLE Launcher.sh")
    elif press == "Thonny Python":
        Popen("/usr/local/bin/Solar Pi/Resources/Launchers/Thonny Launcher.sh")
    elif press == "Java":
        Popen("/usr/local/bin/Solar Pi/Resources/Launchers/blueJ Launcher.sh")

def ToolbarHandler(press):
    if press == "Help":
        webbrowser.get("chromium-browser").open("http://localhost/solar-pi-apps/index.html#start-programming")  # Launch guides here

# GUI Parameters
with gui("Programming", useTtk=True) as program:  # 400x320 # "420x290"
    program.setResizable(False)

    if custom == True:
        program.setTtkTheme("plastik")
        program.setTtkTheme("clam")
        #program.ttkStyle.configure(".", font="10")

        program.ttkStyle.configure("H.TButton", background="#324581", foreground="white", bordercolor="#687396")
        program.ttkStyle.map("H.TButton", background=[("pressed", "#172141"), ("active", "#4059a9")])
        # Regular button
        program.ttkStyle.configure("TButton", background="#dbdce2", bordercolor="#687396")
        # Radiobutton
        program.ttkStyle.map("TRadiobutton", background=[("active", "white")])
    else:
        program.setTtkTheme(theme)
        if theme != "black":
            program.ttkStyle.configure(".", background="white", foreground="black")
            program.ttkStyle.map("TRadiobutton", background=[("active", "white")])

    #program.setResizable(canResize=False)

    # Menu
    program.addMenuList("Applications", ["Solar Pi Home", "Leafpad"], MenuHandler)
    program.addMenuList("IDEs", ["Scratch", "Python IDLE", "Thonny Python", "Java"], MenuHandler)

    # Widgets

    program.setPadding(10, 10)
    program.addImage("solar_pi", "../../Resources/Images/Solar Pi text.gif")
    program.zoomImage("solar_pi", -35)

    #program.addLabel("title", "Choose a Programming Language:")
    #program.addHorizontalSeparator()
    #program.setLabelBg("title", "light gray")

    with program.labelFrame("Choose a Programming Language:"):
        program.setSticky("ew")
        program.setPadding(10, 5)
        program.addRadioButton("language", "Scratch (Easy)")
        program.addRadioButton("language", "Python (Intermedium/Hard)")
        program.addRadioButton("language", "Java (Hard)")

    with program.frame("frame"):
        program.setPadding(10, 10)
        if custom == True or theme == "black":
            program.addImageButton("Go  ", ButtonHandler, "../../Resources/Images/go white.gif", 0, 0, align="right")
            program.setButtonStyle("Go  ", "H.TButton")
        else:
            program.addImageButton("Go  ", ButtonHandler, "../../Resources/Images/go black.gif", 0, 0, align="right")
            program.setLabelFrameStyle("Choose a Programming Language:", "TFrame")
        program.addImageButton(" More Info  ", ButtonHandler, "../../Resources/Images/more info.gif", 0, 1, align="right")
        program.addImageButton("Exit ", ButtonHandler, "../../Resources/Images/cross.gif", 0, 2, align="right")

    if theme != "black":
        program.setBg("white")


