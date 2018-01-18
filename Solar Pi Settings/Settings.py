#!/usr/bin/env python

from appJar import gui
import sys
import fileinput
from subprocess import Popen, call
#from ttkthemes import ThemedStyle
import os
from AutorunConfig import Autorun
from SettingsGet import *

# Add translations for all

# Fetch settinga in Settings.ini
clock_speed = Clock()
battery_meter = BatteryMeter()
launch_welcome = LaunchWelcome()
theme = Theme()


# Reads Settings.ini file
# with open("Settings.ini", "r") as file:
#     data = file.readlines()[0]
# data = data.split(",")
# clock_speed = data[0]
# if data[1] == "False":
#         battery_meter = False
# elif data[1] == "True":
#         battery_meter = True
# if data[2] == "False":
#         launch_welcome = False
# elif data[2] == "True":
#         launch_welcome = True
# theme = data[3]


# Button Events
def ButtonHandler(press):
    if press == "Exit ":  # If user clicks Exit
        quit()

    elif press == "More Info":  # If user clicks More Info
        # Infobox showing info
        program.infoBox("More Information", "This program modifies a text file to change the clock speed of the processor.\nThe number shown on the slider marks the maximum clock speed of the CPU in MHz.\nIf the clock speed is low, the Raspberry Pi will draw less power with lower performance, if the clock speed is high, it will draw more power with more performance.\n\nNote: The default value is 1200MHz.")

    elif press == "Change Advanced Settings":
        Popen("/usr/bin/rc_gui")  # Runs Raspberry Pi Configuration

    elif press == "Languages":
        Popen("/usr/local/bin/Solar Pi/Resources/Launchers/language_launcher.sh")  # Runs Languages app

def SolarPiTheme():
    program.setTtkTheme("plastik")
    program.setTtkTheme("clam")
    #program.ttkStyle.configure(".", font="10")

    program.ttkStyle.configure("H.TButton", background="#324581", foreground="white", bordercolor="#687396")
    program.ttkStyle.map("H.TButton", background=[("pressed", "#172141"), ("active", "#4059a9")])

    # Regular button
    program.ttkStyle.configure("TButton", background="#dbdce2", bordercolor="#687396")

    program.ttkStyle.map("TCheckbutton", background=[("active", "white")])

    program.setButtonStyle("More Info", "H.TButton")
    program.setButtonStyle("Update System", "H.TButton")
    program.setButtonStyle("Apply ", "H.TButton")

    program.setBg("white")

def ClockChange(clock):
    # Opens and modifies config.txt file
    for line in fileinput.input(["/boot/config.txt"], inplace=True):
        if line.strip().startswith("arm_freq="):  # Searches for "arm_freq="
            line = "arm_freq=" + str(clock) + "\n"  # Replaces line with clock speed selected
        sys.stdout.write(line)  # Writes back to file

def ApplySettings(press):
    # Fetches data from widgets
    clock_speed = int(program.getEntry("Max Clock Speed: "))
    battery_meter = program.getCheckBox("Show battery meter in corner")
    launch_welcome = program.getCheckBox("Launch the Solar Pi Welcome application at startup")
    theme = program.getOptionBox("Themes")
    if theme == "Solar Pi":
        SolarPiTheme()

    else:
        theme = theme.lower()
        program.setTtkTheme(theme)  # Sets theme
        program.ttkStyle.configure(".", background="white", foreground="black")  # Sets additional options for theme

    program.setScale("slider", clock_speed)  # Sets slider to value in entry

    Autorun("welcome", launch_welcome, "/home/pi/.config/autostart/Welcome Launcher.desktop")  # Takes appropriate action for running Welcome at startup

    Autorun("battery", battery_meter, "/home/pi/.config/autostart/Battery Meter Launcher.desktop")  # Takes appropriate action for running Battery meter at startup

    ClockChange(clock_speed)  # Modifies /boot/config.txt to change max clock

    data = str(clock_speed) + "," + str(battery_meter) + "," + str(launch_welcome) + "," + theme
    with open("Settings.ini", "w") as file:
        file.write(data)  # Writes settings to file

    # After settings have been changed
    if program.yesNoBox("Restart", "Your Solar Pi needs to be restarted in order for these changes to take effect.\nWould you like to restart now?") == True:  # Message to user to restart RPi
        Popen("/usr/local/bin/Solar Pi/Resources/Launchers/Reboot.sh")


def SetItems(clock_speed, battery_meter, launch_welcome, theme):  # Procedure to set controls
    program.setScale("slider", clock_speed)
    program.setCheckBox("Show battery meter in corner", battery_meter)
    program.setCheckBox("Launch the Solar Pi Welcome application at startup", launch_welcome)
    if theme == "Solar Pi":
        program.setOptionBox("Themes", theme)
    else:
        program.setOptionBox("Themes", theme[0].upper() + theme[1:])


def Defaults(press):  # Procedure to reset to default
    with open("Settings.ini", "w") as file:
        file.write("1200,True,True,plastik")  # Writes default settings to file

    SetItems(1200, True, True, "Solar Pi")  # Sets controls to default

    Autorun("welcome", True, "/home/pi/.config/autostart/Welcome Launcher.desktop")  # Creates .desktop file for welcome

    Autorun("battery", True, "/home/pi/.config/autostart/Battery Meter Launcher.desktop")  # Creates .desktop file for battery meter

    ClockChange(1200)  # Changes max clock speed to 1200 MHz

    SolarPiTheme()  # Sets Solar Pi theme for application

    # Prompts user to restart to apply changes
    if program.yesNoBox("Restart", "Your Solar Pi needs to be restarted in order for these changes to take effect.\nWould you like to restart now?"):
        Popen("/usr/local/bin/Solar Pi/Resources/Launchers/Reboot.sh")

# Runs update scripts
def Update(press):
    if program.getCheckBox("Update Operating System & Installed Programs") == True:
        call("/usr/local/bin/Solar Pi/Resources/Launchers/System Update.sh")
    if program.getCheckBox("Update appJar") == True:
        call("/usr/local/bin/Solar Pi/Resources/Launchers/appJar Update.sh")
        
# Sets entry based on scale changes
def ScaleChange(value):
    value = str(int(program.getScale("slider")))
    program.setEntry("Max Clock Speed: ", value)

# Sets scale based on entry
def EntryScaleChange(value):
    value = int(program.getEntry("Max Clock Speed: "))
    if value > 1200:  # Ensure that values are between 1200 and 600
        value = 1200
    elif value < 600:
        value = 600
    program.setScale("slider", value)
    print(value)


# Unicode symbols
TICK = "\u2714"
CROSS = "\u274C"
RESTORE = "\u21BA"


# GUI code
with gui("Settings", useTtk=True) as program:
    program.setResizable(False)
    if theme == "Solar Pi":
        custom = True

    else:
        custom = False
        program.setTtkTheme(theme)
        program.ttkStyle.configure(".", background="white", foreground="black")
    program.setBg("white")
    #program.setResizable(canResize=False)
    #program.ttkStyle.configure("TLabelframe.Label", background="white")
    #program.ttkStyle.configure("TScale", background="white")
    #program.ttkStyle.configure("TFrame", background="white")
    #program.ttkStyle.configure("TCheckbutton", background="white")
    

    with program.labelFrame("Performance & Power", 0, 0, colspan=2):

        program.setLabelFrameStyle("Performance & Power", "TFrame")
        
        # Title

        program.setPadding(4, 4)

        program.addLabel("title", "Clock Speed Changer", colspan=2)
        program.setLabelSticky("title", "ew")

        program.addScale("slider", 1, 0)
        program.setScaleFunction("slider", ScaleChange)
        program.setScaleSticky("slider", "ew")
        program.setScaleRange("slider", 600, 1200, curr=None)  # Changes scale range
        #program.setScaleIncrement("slider", 100)
        program.addButton("More Info", ButtonHandler, 1, 1)

        program.addLabelNumericEntry("Max Clock Speed: ", 2, 0)
        program.setEntry("Max Clock Speed: ", str(clock_speed))
        program.setEntryMaxLength("Max Clock Speed: ", 4)
        program.setEntrySubmitFunction("Max Clock Speed: ", EntryScaleChange)
        program.addLabel("scale", "MHz", 2, 1)
        program.setLabelSticky("scale", "nws")

        # Scale

        # Label
        program.addLabel("Info", "◄ Greater Battery Life       Performance ►", colspan=2)

        # Buttons
        program.addLabel("filler1", "")
        program.addCheckBox("Show battery meter in corner", colspan=2)
        #program.setCheckBoxStyle("Show standalone battery meter", "TCheckbox")

    with program.labelFrame("Updates", 0, 2):
        program.setPadding(5, 5)
        program.setLabelFrameStyle("Updates", "TFrame")
        program.addLabel("info3", "Note: This will only work\nwith an internet connection.")
        program.addCheckBox("Update Operating System &\nInstalled Programs")
        program.addCheckBox("Update appJar")
        program.addButton("Update System", Update)


    with program.labelFrame("Other Settings", 1, 0, colspan=2):
        program.setLabelFrameStyle("Other Settings", "TFrame")
        program.setPadding(5, 5)
        program.addCheckBox("Launch the Solar Pi Welcome application at startup", 0, colspan=2)
        program.addLabel("themes", "Themes for Solar Pi apps:", 1, 0)
        themes = ["Solar Pi", "Plastik", "Arc", "Clearlooks", "Radiance"]
        program.addOptionBox("Themes", themes, 1, 1)  # Touch friendly???
        program.addButton("Change Advanced Settings", ButtonHandler, 2, 0)
        program.addButton("Languages", ButtonHandler, 2, 1)
        program.setButtonSticky("Languages", "ew")
        program.setButtonSticky("Change Advanced Settings", "ew")


    #program.addButton("Apply", ApplySettings, 5, 0)
    #program.addButton("Exit", ButtonHandler, 5, 1)
    #program.addButtons(["Apply  " + TICK, "Restore Defaults  " + RESTORE, "Exit  " + CROSS], [ApplySettings, Defaults, ButtonHandler], colspan=3)
    #program.addImageButton("Button  ", ButtonHandler, "tick.gif", align="right")

    # with program.frame("frame", colspan=2):
    #     program.setPadding(10, 10)
    #     program.addImageButton("Apply ", ApplySettings, "tick.gif", 0, 0, align="right")
    #     program.addImageButton(" Restore Defaults ", Defaults, "restore.gif", 0, 1, align="right")
    #     #program.setButtonSticky(" Restore Defaults ", "e")
    #     program.addImageButton("Exit ", ButtonHandler, "cross.gif", 0, 2, align="right")

    program.addImageButton("Apply ", ApplySettings, "tick.gif", 2, 0, align="right")
    program.addImageButton(" Restore Defaults ", Defaults, "restore.gif", 2, 1, align="right")
    program.setButtonSticky(" Restore Defaults ", "e")
    program.addImageButton("Exit ", ButtonHandler, "cross.gif", 2, 2, align="right")

    if custom == True:
        SolarPiTheme()



    SetItems(clock_speed, battery_meter, launch_welcome, theme)  # Sets controls to currently selected settings
