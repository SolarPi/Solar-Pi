#!/usr/bin/env python
# Solar Pi Welcome

from appJar import gui
from subprocess import Popen, call
from AutorunConfig import Autorun
from sys import exit
# from ttkthemes import ThemedStyle


# with open("/usr/local/bin/Solar Pi/Solar Pi Settings/Settings.ini", "r") as file:
#     data = file.readlines()[0]
# data = data.split(",")
# theme = data[3]

program = gui("Solar Pi Welcome", "650x400")  # When switch to ttk, change to 650x375

# program.ttkStyle = ThemedStyle(program.topLevel)
# program.ttkStyle.set_theme(theme)

#program.useTtk()

#program.setIcon("E:\\1Home\\Main\\School\\Homework\\Year 10\\Solar Pi NEW\\Solar Pi Applications & Resources\\Applications\\Python Start Screen\\Logo_NEW_2.gif")
#program.setIcon("/usr/local/bin/Solar Pi/Resources/Images/Logo_NEW_2.gif")

def ButtonHandler(press):
    tab_selected = program.getTabbedFrameSelectedTab("MainTabs")  # Fetches the current tab

    if press == "Exit" or press == "Exit3" or press == "Exit2" or press == "Exit4":  # Exits program
        exit()
    elif press == "About":  # Opens the About subwindow
        program.showSubWindow("About Solar Pi")
    elif press == "Close":  # Closes the About subwindow
        program.hideSubWindow("About Solar Pi")
    elif press == "Scratch":  # Launches Scratch
        Popen("/usr/local/bin/Solar Pi/Resources/Launchers/Scratch Launcher.sh")
    elif press == "Python":  # Launches a Python IDE
        if program.yesNoBox("Python", "Would you like to use the Thonny Python IDE instead of the IDLE?") == True:
            Popen("/usr/local/bin/Solar Pi/Resources/Launchers/Thonny Launcher.sh")
        else:
            Popen("/usr/local/bin/Solar Pi/Resources/Launchers/IDLE Launcher.sh")
    elif press == "Java":  # Launches BlueJ
        Popen("/usr/local/bin/Solar Pi/Resources/Launchers/BlueJ Launcher.sh")
    elif press == "Change Advanced Settings":  # Launches RPi settings window
        Popen("/usr/bin/rc_gui")
    elif press == "Languages":
        Popen("/usr/local/bin/Solar Pi/Resources/Launchers/language_launcher.sh")


def MenuHandler(press):
    if press == "Shutdown":
        if program.yesNoBox("Shutdown", "Are you sure that you want to shutdown your Solar Pi now?") == True:
            Popen("/usr/local/bin/Solar Pi/Resources/Launchers/Shutdown.sh")
    elif press == "Reboot":
        if program.yesNoBox("Reboot", "Are you sure that you want to reboot your Solar Pi now?") == True:
            Popen("/usr/local/bin/Solar Pi/Resources/Launchers/Reboot.sh")
    elif press == "Leafpad":
        Popen("/usr/local/bin/Solar Pi/Resources/Launchers/Leafpad Launcher.sh")
    elif press == "Start Programming":
        Programming(None)
    elif press == "Python Guides":
        PythonGuides(None)
    elif press == "Performance to Battery Life":
        PerfBattery(None)
    elif press == "All Files":
        Popen("/usr/local/bin/Solar Pi/Resources/Launchers/pcmanfm Launcher.sh")
    elif press == "Desktop":
        Popen("/usr/local/bin/Solar Pi/Resources/Launchers/Desktop Launcher.sh")
    elif press == "Documents":
        Popen("/usr/local/bin/Solar Pi/Resources/Launchers/Documents Launcher.sh")
    elif press == "Music":
        Popen("/usr/local/bin/Solar Pi/Resources/Launchers/Music Launcher.sh")
    elif press == "Pictures":
        Popen("/usr/local/bin/Solar Pi/Resources/Launchers/Pictures Launcher.sh")
    elif press == "Videos":
        Popen("/usr/local/bin/Solar Pi/Resources/Launchers/Videos Launcher.sh")

def ToolbarHandler(press):
    if press == "Off":
        Popen("/usr/bin/lxde-pi-shutdown-helper")
    elif press == "Settings":
        Popen("/usr/local/bin/Solar Pi/Resources/Launchers/Settings Launcher.sh")  # Call Settings menu
    elif press == "Files":
        Popen("/usr/local/bin/Solar Pi/Resources/Launchers/pcmanfm Launcher.sh")
    elif press == "About":
        program.showSubWindow("About Solar Pi")
    elif press == "Help":
        pass  # Call Starter guide

def PerfBattery(press):
    Popen("/usr/local/bin/Solar Pi/Resources/Launchers/Perf Battery Launcher.sh")
def Programming(press):
    Popen("/usr/local/bin/Solar Pi/Resources/Launchers/Programming Launcher.sh")
def PythonGuides(press):
    Popen("/usr/local/bin/Solar Pi/Resources/Launchers/Python Guide Launcher.sh")
def Update(press):
    box1 = program.getCheckBox("Update Operating System & Installed Programs")
    box2 = program.getCheckBox("Update appJar")
    if box1 == True:
        call("/usr/local/bin/Solar Pi/Resources/Launchers/System Update.sh")
    if box2 == True:
        call("/usr/local/bin/Solar Pi/Resources/Launchers/appJar Update.sh")
def Settings(press):
    if program.getCheckBox("Launch this application at startup") == True:
        Autorun("add")
    else:
        Autorun("remove")


program.setFont(11, font="Dejavu Sans")


# About Popup
with program.subWindow("About Solar Pi", modal=True):
    program.setPadding(5, 5)
    program.setBg("white")
    program.addImage("solar_pi_logo", "Solar Pi logo.gif")
    program.zoomImage("solar_pi_logo", -3)
    program.setLocation(250, 150)
    program.setResizable(canResize=False)
    with program.labelFrame("About"):
        program.getLabelFrameWidget("About").config(font="bold")
        program.setLabelFrameFg("About", "#2b4570")
        program.setPadding(10, 10)
        program.addMessage("about", "The Solar Pi is charity oriented project, aiming to deliver low cost Raspberry Pi based solar powered computers to developing countries. Our aim is to teach people how to code, so that they can become employed and move on financially and socially.\n\nWe hope that you enjoy your Solar Pi!")
        program.setMessageFg("about", "black")
    program.addButton("Close", ButtonHandler)


# Languages Window



# Main Window
program.setPadding(3, 3)
with program.tabbedFrame("MainTabs", colspan=4):

    program.setTabbedFrameTabExpand("MainTabs", expand=True)

    # Menu bar
    program.addMenuList("Power", ["Shutdown", "Reboot"], MenuHandler)
    program.addMenuList("Applications", ["Leafpad", "Start Programming", "Performance to Battery Life"], MenuHandler)
    program.addMenuList("Guides", ["Python Guides"], MenuHandler)
    program.addMenuList("Files", ["All Files", "Desktop", "Documents", "Music", "Pictures", "Videos"], MenuHandler)


    tools = ["Off", "Settings", "Files", "About", "Help"]
    program.addToolbar(tools, ToolbarHandler, findIcon=True)

    # Welcome Tab
    with program.tab("Welcome!"):
        program.setPadding(10, 10)
        program.addImage("logo", "Solar Pi logo.gif", colspan=2)
        program.zoomImage("logo", -2)
        program.addLabel("welcome", "Welcome to your Solar Pi!", colspan=2)  # Update translation
        program.getLabelWidget("welcome").config(font=("Dejavu Sans", "20"))
        program.addLabel("get_started", "To help you start to use your Solar Pi, click\non the button to open the starter guide -->", 2, 0)  # Update translation
        program.addButton("Get Started", ButtonHandler, 2, 1)
        #program.addLabel("label1", "Your Solar Pi is a solar powered Raspberry Pi based computer.\nStart by clicking one of the tabs above.  ^^^", colspan=2)
        program.addButtons(["About", "Languages", "Exit"], ButtonHandler, colspan=2)


    # Applications Tab
    with program.tab("Applications"):
        with program.labelFrame("Applications"):
            program.setSticky("ew")
            program.setPadding(10, 10)
            program.addLabel("applications_info", "Hover over the icons to see more information about each program.", colspan=2)

            # Start Programming
            with program.labelFrame("Start Programming", 1, 0):
                program.setPadding(10, 15)
                program.addImage("programming_icon", "Programming icon cropped.gif", 0, 0)
                program.zoomImage("programming_icon", -13)
                program.setImageTooltip("programming_icon", "This allows you to see and try the different options for programming.")
                program.addButton("Start Programming", Programming, 0, 1)

            # Performance to Battery Life
            with program.labelFrame("Performance & Battery Life Settings", 1, 1):
                program.setPadding(10, 10)
                program.addImage("perf_icon", "speedometer1600.gif", 0, 0)
                program.zoomImage("perf_icon", -37)
                program.setImageTooltip("perf_icon", "This allows you to increase the performance or battery life of your Solar Pi.")
                program.addButton("Performance & Battery Life", PerfBattery, 0, 1)

            # IDEs
            with program.labelFrame("IDEs", 2, 0, colspan=2):
                program.setPadding(10, 10)

                with program.labelFrame("Scratch", 1, 0):
                    program.setPadding(10, 10)
                    program.addImage("scratch_logo2", "scratch logo.gif", 0, 0)
                    program.zoomImage("scratch_logo2", -50)
                    program.setImageTooltip("scratch_logo2", "The Scratch 2 IDE. Create Scratch programs and games with this.")
                    program.addButton("Scratch", ButtonHandler, 0, 1)

                with program.labelFrame("Python", 1, 1):
                    program.setPadding(10, 10)
                    program.addImage("python_logo2", "Python icon.gif", 0, 0)
                    program.zoomImage("python_logo2", -4)
                    program.setImageTooltip("python_logo2", "The Python IDE. Write and run Python applications.")
                    program.addButton("Python", ButtonHandler, 0, 1)

                with program.labelFrame("Java", 1, 2):
                    program.setPadding(10, 10)
                    program.addImage("java_logo", "java logo.gif", 0, 0)
                    program.zoomImage("java_logo", -5)
                    program.setImageTooltip("java_logo", "The BlueJ Java IDE. Create Java applications.")
                    program.addButton("Java", ButtonHandler, 0, 1)


    # Guides & Tutorials Tab
    with program.tab("Guides & Tutorials"):
        with program.labelFrame("Guides & Tutorials"):
            program.setSticky("ew")
            program.setPadding(10, 10)
            program.addLabel("guides_info", "Hover over the icons to see more information about each guide/tutorial.", colspan=2)

            # Python Guides
            with program.labelFrame("Python Guides & Tutorials"):
                program.setPadding(10, 10)
                program.addImage("python_logo", "Python icon.gif", 0, 0)
                program.zoomImage("python_logo", -4)
                program.setImageTooltip("python_logo", "A collection of tutorials and Python documentation to help you learn Python.")
                program.addButton("Python Guides", PythonGuides, 0, 1)

            # Scratch Tutorial
            with program.labelFrame("Scratch Tutorial", 1, 1):
                program.setPadding(10, 10)
                program.addImage("scratch_logo", "scratch logo.gif", 0, 0)
                program.zoomImage("scratch_logo", -50)
                program.setImageTooltip("scratch_logo", "A beginner's tutorial on how to use Scratch.")
                program.addButton("Scratch Tutorial", ButtonHandler, 0, 1)

    # Settings Tab
    with program.tab("Settings"):
        with program.labelFrame("Settings"):
            program.setSticky("ew")
            program.setPadding(10, 10)
            with program.labelFrame("General Settings", 0, 0):
                program.setSticky("ew")
                program.setPadding(10, 10)
                program.addCheckBox("Launch this application at startup")
                program.setCheckBox("Launch this application at startup", ticked=True)
                program.addButton("Change Advanced Settings", ButtonHandler)
                program.addButton("Change Performance & Battery Life Settings", PerfBattery)
                program.addButton("Apply Changes", Settings)
                program.setButtonSticky("Apply Changes", "Both")
                program.setButtonBg("Apply Changes", "gray")
                program.setButtonFg("Apply Changes", "white")

            with program.labelFrame("Update", 0, 1):
                program.setSticky("ew")
                program.setPadding(10, 10)
                program.addLabel("info3", "Note: This will only work\nwith an internet connection.")
                program.addCheckBox("Update Operating System & Installed Programs")
                program.addCheckBox("Update appJar")
                program.addButton("Go", Update)
                program.setButtonBg("Go", "gray")
                program.setButtonFg("Go", "white")


#program.setBg("white")

num = 0
def updateMeter():
    global num
    program.setMeter("battery", num)
    #program.setLabel("level", str(num)+"%")
    num += 1

program.addLabel("battery", "Battery Remaining:", 1, 0)  # Update translation
#program.setLabelAlign("battery", "right")
program.setLabelAnchor("battery", "e")
program.addMeter("battery", 1, 2)
program.setMeterFill("battery", "#13d323")
program.addLabel("blank", "", 1, 3)
#program.setMeterPadding("battery", 5, 5)
program.registerEvent(updateMeter)
program.setPollTime(10000)


with open("language.txt", "r") as file:
    lang = file.readline()
    lang.rstrip("\n")


#print(lang)

program.go(language=lang)
