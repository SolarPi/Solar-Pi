#!/usr/bin/env python

from appJar import gui
import sys
import fileinput
from subprocess import Popen, call
from ttkthemes import ThemedStyle
import os
from AutorunConfig import Autorun
from SettingsGet import *

# Add translations for all

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
        Popen("/usr/bin/rc_gui")

    elif press == "Languages":
        Popen("/usr/local/bin/Solar Pi/Resources/Launchers/language_launcher.sh")

def ClockChange(clock):
    # Opens and modifies config.txt file
    for line in fileinput.input(["/boot/config.txt"], inplace=True):
        if line.strip().startswith("arm_freq="):  # Searches for "arm_freq="
            line = "arm_freq=" + str(clock) + "\n"  # Replaces line with clock speed selected
        sys.stdout.write(line)  # Writes back to file

def ApplySettings(press):
    clock_speed = int(program.getEntry("Max Clock Speed: "))
    battery_meter = program.getCheckBox("Show standalone battery meter")
    launch_welcome = program.getCheckBox("Launch the Solar Pi Welcome application at startup")
    theme = program.getOptionBox("Themes").lower()

    program.setScale("slider", clock_speed)

    program.setTtkTheme(theme)

    if battery_meter == True:
        pass

    Autorun(launch_welcome)  # Takes appropriate action for running Welcome at startup

    ClockChange(clock_speed)

    data = str(clock_speed) + "," + str(battery_meter) + "," + str(launch_welcome) + "," + theme
    with open("Settings.ini", "w") as file:
        file.write(data)  # Writes settings to file

    # After settings have been changed
    if program.yesNoBox("Restart", "Your Solar Pi needs to be restarted in order for these changes to take effect.\nWould you like to restart now?") == True:  # Message to user to restart RPi
        Popen("/usr/local/bin/Solar Pi/Resources/Launchers/Reboot.sh")


def SetItems(clock_speed, battery_meter, launch_welcome, theme):  # Procedure to set controls
    program.setScale("slider", clock_speed)
    program.setCheckBox("Show standalone battery meter", battery_meter)
    program.setCheckBox("Launch the Solar Pi Welcome application at startup", launch_welcome)
    program.setOptionBox("Themes", theme[0].upper() + theme[1:])


def Defaults(press):  # Procedure to reset to default
    with open("Settings.ini", "w") as file:
        file.write("1200,True,True,plastik")

    SetItems(1200, True, True, "plastik")

    Autorun(True)

    ClockChange(1200)

    program.setTtkTheme("plastik")

    if program.yesNoBox("Restart", "Your Solar Pi needs to be restarted in order for these changes to take effect.\nWould you like to restart now?"):
        Popen("/usr/local/bin/Solar Pi/Resources/Launchers/Reboot.sh")


def Update(press):
    if program.getCheckBox("Update Operating System & Installed Programs") == True:
        call("/usr/local/bin/Solar Pi/Resources/Launchers/System Update.sh")
    if program.getCheckBox("Update appJar") == True:
        call("/usr/local/bin/Solar Pi/Resources/Launchers/appJar Update.sh")
        

def ScaleChange(value):
    value = int(program.getScale("slider"))
    program.setEntry("Max Clock Speed: ", value)

def EntryScaleChange(value):
    value = int(program.getEntry("Max Clock Speed: "))
    if value > 1200:
        value = 1200
    elif value < 600:
        value = 600
    program.setScale("slider", value)
    print(value)


TICK = "\u2714"
CROSS = "\u274C"
RESTORE = "\u21BA"


with gui("Settings", useTtk=True) as program:
    program.setTtkTheme(theme)
    #program.setBg("white")
    #program.setResizable(canResize=False)

    with program.labelFrame("Performance & Power", 0, 0, colspan=2):
        
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
        program.addCheckBox("Show standalone battery meter", colspan=2)


    with program.labelFrame("Updates", 0, 2):
        program.setPadding(5, 5)
        program.addLabel("info3", "Note: This will only work\nwith an internet connection.")
        program.addCheckBox("Update Operating System &\nInstalled Programs")
        program.addCheckBox("Update appJar")
        program.addButton("Update System", Update)


    with program.labelFrame("Other Settings", 1, 0, colspan=2):
        program.setPadding(5, 5)
        program.addCheckBox("Launch the Solar Pi Welcome application at startup", 0, colspan=2)
        program.addLabel("themes", "Themes for Solar Pi apps:", 1, 0)
        themes = ["Plastik", "Arc", "Clam", "Clearlooks", "Radiance"]
        program.addOptionBox("Themes", themes, 1, 1)  # Touch friendly???
        program.addButton("Change Advanced Settings", ButtonHandler, 2, 0)
        program.addButton("Languages", ButtonHandler, 2, 1)
        program.setButtonSticky("Languages", "ew")
        program.setButtonSticky("Change Advanced Settings", "ew")


    #program.addButton("Apply", ApplySettings, 5, 0)
    #program.addButton("Exit", ButtonHandler, 5, 1)
    #program.addButtons(["Apply  " + TICK, "Restore Defaults  " + RESTORE, "Exit  " + CROSS], [ApplySettings, Defaults, ButtonHandler], colspan=3)
    #program.addImageButton("Button  ", ButtonHandler, "tick.gif", align="right")
    
    program.addImageButton("Apply ", ApplySettings, "tick.gif", 4, 0, align="right")
    program.addImageButton(" Restore Defaults ", Defaults, "restore.gif", 4, 1, align="right")
    program.setButtonSticky(" Restore Defaults ", "e")
    program.addImageButton("Exit ", ButtonHandler, "cross.gif", 4, 2, align="right")




    SetItems(clock_speed, battery_meter, launch_welcome, theme)  # Sets controls to currently selected settings
