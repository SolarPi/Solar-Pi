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

if theme == "solar pi":
    ttk = False
else:
    ttk = True

# Handlers
def ButtonHandler(press):
    option = program.getRadioButton("language")
    if press == "Exit":
        quit()
    elif press == "Go":
        if option == "Scratch (Easy)":
            Popen("/usr/local/bin/Solar Pi/Resources/Launchers/Scratch Launcher.sh")
        elif option == "Python (Intermedium/Hard)":
            webbrowser.get("chromium-browser").open("http://localhost/Advanced-Things/python/index.html")  # Launch Python starter guide
            Popen("/usr/local/bin/Solar Pi/Resources/Launchers/IDLE Launcher.sh")
            webbrowser.get("chromium-browser").open("http://localhost:81")  # Launch A Byte of Python
        elif option == "Java (Hard)":
            Popen("/usr/local/bin/Solar Pi/Resources/Launchers/BlueJ Launcher.sh")
            webbrowser.get("chromium-browser").open("http://localhost:82/java/index.htm")  # Launch Java Guide
        
    elif press == "More Info":
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
with gui("Programming", "400x325", useTtk=ttk) as program:  # 400x320
    if ttk == True:
        program.setTtkTheme(theme)
        program.ttkStyle.configure(".", background="white", foreground="black")

    program.setPadding(10, 10)
    program.setBg("white")
    #program.setResizable(canResize=False)

    # Menu
    program.addMenuList("Applications", ["Solar Pi Home", "Leafpad"], MenuHandler)
    program.addMenuList("IDEs", ["Scratch", "Python IDLE", "Thonny Python", "Java"], MenuHandler)

    # Widgets
    #program.addImage("solar_pi", "/usr/local/bin/Solar Pi/Resources/Images/Solar Pi text.gif")
    program.addImage("solar_pi", "../../Resources/Images/Solar Pi text.gif")
    program.zoomImage("solar_pi", -35)

    program.addLabel("title", "Choose a Programming Language:")
    program.addHorizontalSeparator()
    if ttk == False:
        program.setLabelBg("title", "light gray")
    #program.setLabelBg("title", "light gray")

    program.addRadioButton("language", "Scratch (Easy)")
    program.addRadioButton("language", "Python (Intermedium/Hard)")
    program.addRadioButton("language", "Java (Hard)")
    if ttk == True:
        program.addButtons(["Go", "More Info", "Exit"], ButtonHandler)
    if ttk == False:
        with program.frame("frame"):
            program.setPadding(10, 10)
            program.addButton("Go", ButtonHandler, 0, 0)
            program.addButton("More Info", ButtonHandler, 0, 1)
            program.addButton("Exit", ButtonHandler, 0, 2)

        program.setButtonRelief("Go", "groove")
        program.setButtonBg("Go", "#324581")
        program.setButtonFg("Go", "white")
        program.setButtonSticky("Go", "nesw")
        program.setButtonPadding("Go", [5, 5])
        program.setButtonRelief("More Info", "groove")
        program.setButtonBg("More Info", "#dbdce2")
        program.setButtonSticky("More Info", "nesw")
        program.setButtonRelief("Exit", "groove")
        program.setButtonBg("Exit", "#dbdce2")
        program.setButtonSticky("Exit", "nesw")
