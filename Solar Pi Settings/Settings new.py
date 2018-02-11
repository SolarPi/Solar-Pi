#!/usr/bin/env python3

from appJar import gui
import sys
import fileinput
from subprocess import Popen, call
import os
from AutorunConfig import Autorun
from SettingsGet import *
from threading import Thread
from time import sleep

# Add translations for all

# Fetch settings in Settings.ini
clock_speed = Clock()
battery_meter = BatteryMeter()
launch_welcome = LaunchWelcome()
theme = Theme()


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
        Popen("/usr/local/bin/Solar Pi/Resources/Launchers/language_launcher.sh")  # Runs Languages program

def SolarPiTheme():
    # Sets Solar Pi theme for application
    program.setTtkTheme("plastik")
    program.setTtkTheme("clam")
    #program.ttkStyle.configure(".", font="10")

    # Highlighted button
    program.ttkStyle.configure("H.TButton", background="#324581", foreground="white", bordercolor="#687396")
    program.ttkStyle.map("H.TButton", background=[("pressed", "#172141"), ("active", "#4059a9")])

    # Regular button
    program.ttkStyle.configure("TButton", background="#dbdce2", bordercolor="#687396")

    # Fix CheckButton background
    program.ttkStyle.map("TCheckbutton", background=[("active", "white")])

    #program.setButtonStyle("More Info", "H.TButton")
    #program.setButtonStyle("Update System", "H.TButton")
    program.setButtonStyle("Apply ", "H.TButton")  # Set highlight button style to apply button

    program.ttkStyle.configure("Horizontal.TScale", troughcolor="light grey", sliderthickness="1", borderwidth="0", sliderrelief="flat")

    program.ttkStyle.configure("TLabelframe", bordercolor="#687396")  # LabelFrame border colour

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

    elif theme == "Black":
        program.setTtkTheme("black")

    else:
        # Sets options for other themes
        theme = theme.lower()
        program.setTtkTheme(theme)  # Sets theme
        program.ttkStyle.configure(".", background="white", foreground="black")  # Sets additional options for theme
        program.setLabelFrameStyle("Performance & Power", "TFrame")
        program.setLabelFrameStyle("Other Settings", "TFrame")
        program.setLabelFrameStyle("Updates", "TFrame")
        program.ttkStyle.map("TCheckbutton", background=[("active", "white")])

    program.setScale("slider", clock_speed)  # Sets slider to value in entry

    Autorun("welcome", launch_welcome, "/home/pi/.config/autostart/Welcome Launcher.desktop")  # Takes programropriate action for running Welcome at startup

    Autorun("battery", battery_meter, "/home/pi/.config/autostart/Battery Meter Launcher.desktop")  # Takes programropriate action for running Battery meter at startup

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

kill = False
def MeterUpdate():
    global kill
    i = 0
    while True:
        print(kill)
        if kill == True:
            program.queueFunction(program.setMeter, "update_meter", 0)
            break
        for i in range(1, 51):
            print(kill)
            i = i * 2
            program.queueFunction(program.setMeter, "update_meter", i)
            sleep(0.05)
            if kill == True:
                program.queueFunction(program.setMeter, "update_meter", 0)
                break


def update2(press):  # TODO: Fix threading issues
    global kill
    t = Thread(target=MeterUpdate)
    t.start()
    kill = False
    program.showSubWindow("Updating your Solar Pi")
    print("hi")

def stop():
    global kill
    kill = True
    program.hideSubWindow("Updating your Solar Pi")

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

########################
#     Code for GUI     #
########################

with gui("Settings", useTtk=True) as program:
    #program.setResizable(False)

    # Configures themes
    if theme == "Solar Pi":
        custom = True

    elif theme == "black":
        custom = False
        program.setTtkTheme(theme)

    else:
        custom = False
        program.setTtkTheme(theme)
        program.ttkStyle.configure(".", background="white", foreground="black")
        program.ttkStyle.map("TCheckbutton", background=[("active", "white")])
        program.setBg("white")
    #program.setResizable(canResize=False)
    #program.ttkStyle.configure("TLabelframe.Label", background="white")
    #program.ttkStyle.configure("TScale", background="white")
    #program.ttkStyle.configure("TFrame", background="white")
    #program.ttkStyle.configure("TCheckbutton", background="white")

    pages = [" Performance & Power", " Updates", " Other Settings"]  # Sets settings pages

    def change(listName):
        program.getFrameWidget(program.listBox("list")[0]).lift()

    with program.labelFrame("Settings", sticky="nws", stretch="none", padding=[10, 10]):  # Create LabelFrame
        lb = program.listBox("list", pages, change=change,
                         activestyle="none", selectbackground="#687396", font=("ubuntu", 13, "normal"))  # Create ListBox
        program.configure(sticky="news", stretch="both")

        for pos, page in enumerate(pages):  # Iterate through pages
            with program.frame(page, 0, 1, sticky="new") as f:  # Create frame for each page
                if pos == 0:  # Code for first page
                    program.setPadding(4, 4)

                    program.addLabel("perf_title", "Performance & Power")
                    program.getLabelWidget("perf_title").config(font=("ubuntu", 14, "normal"))

                    program.addHorizontalSeparator(colspan=2)

                    program.addLabel("title", "Change the CPU Clock Speed:", 2, 0, colspan=2)
                    #program.getLabelWidget("title").config(font=("ubuntu", 12, "normal"))
                    program.setLabelSticky("title", "ew")

                    #program.addHorizontalSeparator(colspan=2)

                    # Entry to display and enter clock speed
                    program.addLabelNumericEntry("Max Clock Speed: ", 3, 0)
                    program.setEntry("Max Clock Speed: ", str(clock_speed))
                    program.setEntryMaxLength("Max Clock Speed: ", 4)
                    program.setEntrySubmitFunction("Max Clock Speed: ", EntryScaleChange)
                    program.addLabel("scale", "MHz", 3, 1)
                    program.setLabelSticky("scale", "nws")

                    # Scale
                    program.addScale("slider", 4, 0)
                    program.setScaleChangeFunction("slider", ScaleChange)
                    program.setScaleSticky("slider", "ew")
                    program.setScaleRange("slider", 600, 1200, curr=None)  # Changes scale range
                    # program.setScaleIncrement("slider", 100)
                    program.addButton("More Info", ButtonHandler, 4, 1)
                    # Label
                    program.addLabel("Info", "◄ Greater Battery Life       Performance ►", colspan=2)

                    # Buttons
                    program.addHorizontalSeparator(colspan=2)
                    program.addCheckBox("Show battery meter in corner", colspan=2)
                    # program.setCheckBoxStyle("Show standalone battery meter", "TCheckbox")

                elif pos == 1:  # Code for second page
                    program.setPadding(5, 5)
                    program.addLabel("updates_title", "Updates")
                    program.getLabelWidget("updates_title").config(font=("ubuntu", 14, "normal"))
                    program.addHorizontalSeparator()
                    #program.addLabel("update_info", "Note: This will only work with an internet connection.")
                    #program.addCheckBox("Update Operating System & Installed Programs")
                    #program.addCheckBox("Update appJar")
                    #program.addButton("Update System", Update
                    program.addLabel("update_info", "Please insert the update USB stick into the Solar Pi.\nPress 'Update' once you have done this.")
                    program.addButton("Update", update2)


                elif pos == 2:  # Code for third page
                    program.setPadding(5, 5)
                    program.addLabel("other_title", "Other Settings")
                    program.getLabelWidget("other_title").config(font=("ubuntu", 14, "normal"))
                    program.addHorizontalSeparator(colspan=2)
                    program.addCheckBox("Launch the Solar Pi Welcome application at startup", colspan=2)
                    program.addLabel("themes", "Themes for Solar Pi programs:", 3, 0)
                    themes = ["Solar Pi", "Plastik", "Arc", "Black", "Winxpblue"]
                    # program.setTtkTheme("arc")
                    # program.setTtkTheme("clam")
                    # themes = program.getTtkThemes()
                    program.addOptionBox("Themes", themes, 3, 1)
                    program.addButton("Change Advanced Settings", ButtonHandler, 4, 0)
                    program.addButton("Languages", ButtonHandler, 4, 1)
                    program.setButtonSticky("Languages", "ew")
                    program.setButtonSticky("Change Advanced Settings", "ew")

        program.configure(sticky="se", stretch="column")
        program.selectListItemAtPos("list", 0, callFunction=True)


    # Buttons to apply, restore defaults and exit
    with program.frame("frame3"):
        program.setPadding(10, 5)
        program.addImageButton("Apply ", ApplySettings, "../Resources/Images/tick.gif", 0, 0, align="right")
        program.addImageButton(" Restore Defaults ", Defaults, "../Resources/Images/restore.gif", 0, 1, align="right")
        #program.setButtonSticky(" Restore Defaults ", "e")
        program.addImageButton("Exit ", ButtonHandler, "../Resources/Images/cross.gif", 0, 2, align="right")

    # Second window for updates
    with program.subWindow("Updating your Solar Pi", modal=True):
        program.setResizable(False)
        program.setStopFunction(stop)
        with program.frame("frame23"):
            program.setPadding(10, 10)
            program.addSplitMeter("update_meter")
            program.setMeterFill("update_meter", ["green", "white"])
            program.setMeterSticky("update_meter", "ew")
            program.addLabel("update_info2", "Please wait while we check the USB...")

    # Configure themes
    if custom == True:
        SolarPiTheme()  # Sets theme to Solar Pi theme
    else:
        program.setLabelFrameStyle("Settings", "TFrame")  # Ensures that LabelFrame background is white

    if theme == "black":
        program.setListBoxBg("list", "#424242")
        program.setListBoxFg("list", "white")


    SetItems(clock_speed, battery_meter, launch_welcome, theme)  # Sets controls to currently selected settings
