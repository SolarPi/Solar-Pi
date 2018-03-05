#!/usr/bin/env python
# Solar Pi Welcome

from appJar import *
from subprocess import Popen, call
from AutorunConfig import Autorun
from sys import exit

program = gui("Solar Pi Welcome", "600x350")
#program.setIcon("E:\\1Home\\Main\\School\\Homework\\Year 10\\Solar Pi NEW\\Solar Pi Applications & Resources\\Applications\\Python Start Screen\\Logo_NEW_2.gif")
#program.setIcon("/usr/local/bin/Solar Pi/Resources/Images/Logo_NEW_2.gif")

def ButtonHandler(press):
    tab_selected = program.getTabbedFrameSelectedTab("MainTabs")  # Fetches the current tab
    if press == "Exit" or press == "Exit3" or press == "Exit2" or press == "Exit4":
        exit()
    elif press == "Close":
        program.hideSubWindow("About Solar Pi")
    elif press == "About":
        program.showSubWindow("About Solar Pi")
    elif press == "Start Programming":
        Popen("/usr/local/bin/Solar Pi/Resources/Launchers/Programming Launcher.sh")
    elif press == "Performance to Battery Life":
        Popen("/usr/local/bin/Solar Pi/Resources/Launchers/Perf Battery Launcher.sh")
    elif press == "Python Guides":
        Popen("/usr/local/bin/Solar Pi/Resources/Launchers/Python Guide Launcher.sh")
    elif press == "Apply Changes":
        if program.getCheckBox("Launch this application at startup") == True:
            Autorun("add")
        else:
            Autorun("remove")
    elif press == "Change Performance\n& Battery Life Settings":
        Popen("/usr/local/bin/Solar Pi/Resources/Launchers/Perf Battery Launcher.sh")
    elif press == "Go":
        box1 = program.getCheckBox("Update Operating System\n& Installed Programs")
        box2 = program.getCheckBox("Update appJar")
        if box1 == True:
            call("/usr/local/bin/Solar Pi/Resources/Launchers/System Update.sh")
        if box2 == True:
            call("/usr/local/bin/Solar Pi/Resources/Launchers/appJar Update.sh")
    elif press == "Scratch":
        Popen("/usr/local/bin/Solar Pi/Resources/Launchers/Scratch Launcher.sh")
    elif press == "Python":
        if program.yesNoBox("Python", "Would you like to use the Thonny Python IDE instead of the IDLE?") == True:
            Popen("/usr/local/bin/Solar Pi/Resources/Launchers/Thonny Launcher.sh")
        else:
            Popen("/usr/local/bin/Solar Pi/Resources/Launchers/IDLE Launcher.sh")
    elif press == "Java":
        Popen("/usr/local/bin/Solar Pi/Resources/Launchers/BlueJ Launcher.sh")
    elif press == "Change Advanced Settings":
        Popen("/usr/bin/rc_gui")


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
        Popen("/usr/local/bin/Solar Pi/Resources/Launchers/Programming Launcher.sh")
    elif press == "Performance to Battery Life":
        Popen("/usr/local/bin/Solar Pi/Resources/Launchers/Perf Battery Launcher.sh")
    elif press == "Python Guides":
        Popen("/usr/local/bin/Solar Pi/Resources/Launchers/Python Guide Launcher.sh")
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


# About Popup
program.startSubWindow("About Solar Pi", modal=True)
program.setPadding(5, 5)
program.setBg("white")
program.addImage("solar_pi_logo", "Solar Pi logo.gif")
program.zoomImage("solar_pi_logo", -3)
program.setLocation(250, 150)
program.setResizable(canResize=False)
program.startLabelFrame("About")
program.setPadding(10, 10)
program.addMessage("about", "The Solar Pi is charity oriented project, aiming to deliver low cost Raspberry Pi based solar powered computers to developing countries. Our aim is to teach people how to code, so that they can become employed and move on financially and socially.\n\nWe hope that you enjoy your Solar Pi!")
program.stopLabelFrame()
program.addButton("Close", ButtonHandler)
program.stopSubWindow()

# Main Window
program.setPadding(3, 3)
# program.addImage("logo1", "E:\\1Home\\Main\\School\\Homework\\Year 10\\Solar Pi NEW\\Solar Pi Applications & Resources\\Applications\\Python Start Screen\\Solar Pi text.gif")
# #program.addImage("logo1", "/usr/local/bin/Solar Pi/Resources/Images/Solar Pi text.gif")
# program.zoomImage("logo1", -45)
program.startTabbedFrame("MainTabs")

# Menu bar
program.addMenuList("Power", ["Shutdown", "Reboot"], MenuHandler)
program.addMenuList("Applications", ["Leafpad", "Start Programming", "Performance to Battery Life"], MenuHandler)
program.addMenuList("Guides", ["Python Guides"], MenuHandler)
program.addMenuList("Files", ["All Files", "Desktop", "Documents", "Music", "Pictures", "Videos"], MenuHandler)


# Welcome Tab
program.startTab("Welcome!")
program.setPadding(10, 10)
program.addLabel("welcome", "Welcome to the")
program.getLabelWidget("welcome").config(font="50")
program.addImage("logo", "Solar Pi logo.gif")
program.zoomImage("logo", -2)

program.addLabel("label1", "Your Solar Pi is a solar powered Raspberry Pi based computer.\nStart by clicking one of the tabs above.  ^^^")
program.addButtons(["About", "Exit"], ButtonHandler)

program.stopTab()

# Applications Tab
program.startTab("Applications")
program.startLabelFrame("Applications")
program.setSticky("ew")
program.setPadding(10, 10)
program.addLabel("applications_info", "Hover over the icons to see more information about each program.", colspan=2)

# Start Programming
program.startLabelFrame("Start Programming", 1, 0)
program.setPadding(10, 15)
program.addImage("programming_icon", "Programming icon cropped.gif", 0, 0)
program.zoomImage("programming_icon", -13)
program.setImageTooltip("programming_icon", "This allows you to see and try the different options for programming.")
program.addButton("Start Programming", ButtonHandler, 0, 1)
program.stopLabelFrame()

# Performance to Battery Life
program.startLabelFrame("Performance to Battery Life Selector", 1, 1)
program.setPadding(10, 10)
program.addImage("perf_icon", "speedometer1600.gif", 0, 0)
program.zoomImage("perf_icon", -37)
program.setImageTooltip("perf_icon", "This allows you to increase the performance or battery life of your Solar Pi.")
program.addButton("Performance to Battery Life", ButtonHandler, 0, 1)
program.stopLabelFrame()

# IDEs
program.startLabelFrame("IDEs", 2, 0, colspan=2)
program.setPadding(10, 10)

program.startLabelFrame("Scratch", 1, 0)
program.setPadding(10, 10)
program.addImage("scratch_logo2", "scratch logo.gif", 0, 0)
program.zoomImage("scratch_logo2", -50)
program.setImageTooltip("scratch_logo2", "The Scratch 2 IDE. Create Scratch programs and games with this.")
program.addButton("Scratch", ButtonHandler, 0, 1)
program.stopLabelFrame()

program.startLabelFrame("Python", 1, 1)
program.setPadding(10, 10)
program.addImage("python_logo2", "Python icon.gif", 0, 0)
program.zoomImage("python_logo2", -4)
program.setImageTooltip("python_logo2", "The Python IDE. Write and run Python applications.")
program.addButton("Python", ButtonHandler, 0, 1)
program.stopLabelFrame()

program.startLabelFrame("Java", 1, 2)
program.setPadding(10, 10)
program.addImage("java_logo", "java logo.gif", 0, 0)
program.zoomImage("java_logo", -5)
program.setImageTooltip("java_logo", "The BlueJ Java IDE. Create Java applications.")
program.addButton("Java", ButtonHandler, 0, 1)
program.stopLabelFrame()

program.stopLabelFrame()

program.stopLabelFrame()
program.stopTab()


# Guides & Tutorials Tab
program.startTab("Guides & Tutorials")
program.startLabelFrame("Guides & Tutorials")
program.setSticky("ew")
program.setPadding(10, 10)
program.addLabel("guides_info", "Hover over the icons to see more information about each guide/tutorial.", colspan=2)

# Python Guides
program.startLabelFrame("Python Guides & Tutorials")
program.setPadding(10, 10)
program.addImage("python_logo", "Python icon.gif", 0, 0)
program.zoomImage("python_logo", -4)
program.setImageTooltip("python_logo", "A collection of tutorials and Python documentation to help you learn Python.")
program.addButton("Python Guides", ButtonHandler, 0, 1)
program.stopLabelFrame()

# Scratch Tutorial
program.startLabelFrame("Scratch Tutorial", 1, 1)
program.setPadding(10, 10)
program.addImage("scratch_logo", "scratch logo.gif", 0, 0)
program.zoomImage("scratch_logo", -50)
program.setImageTooltip("scratch_logo", "A beginner's tutorial on how to use Scratch.")
program.addButton("Scratch Tutorial", ButtonHandler, 0, 1)
program.stopLabelFrame()

program.stopLabelFrame()
program.stopTab()


# Settings Tab
program.startTab("Settings")
program.startLabelFrame("Settings")
program.setSticky("ew")
program.setPadding(10, 10)

program.startLabelFrame("General Settings", 0, 0)
program.setSticky("ew")
program.setPadding(10, 10)
program.addCheckBox("Launch this application at startup")
program.setCheckBox("Launch this application at startup", ticked=True)
program.addButton("Change Advanced Settings", ButtonHandler)
program.addButton("Change Performance\n& Battery Life Settings", ButtonHandler)
program.addButton("Apply Changes", ButtonHandler)
program.setButtonSticky("Apply Changes", "Both")
program.setButtonBg("Apply Changes", "gray")
program.setButtonFg("Apply Changes", "white")
program.stopLabelFrame()

program.startLabelFrame("Update", 0, 1)
program.setSticky("ew")
program.setPadding(10, 10)
program.addLabel("info3", "Note: This will only work\nwith an internet connection.")
program.addCheckBox("Update Operating System\n& Installed Programs")
program.addCheckBox("Update appJar")
program.addButton("Go", ButtonHandler)
program.setButtonBg("Go", "gray")
program.setButtonFg("Go", "white")
program.stopLabelFrame()


program.stopLabelFrame()
program.stopTab()

program.stopTabbedFrame()

program.go()
