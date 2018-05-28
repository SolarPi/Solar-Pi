#!/usr/bin/env python3

##############################
#  Needs to be run as root!  #
##############################

from appJar import gui
import sys
import fileinput
from subprocess import Popen, call
from AutorunConfig import Autorun
from threading import Thread
from time import sleep
from SettingsRW import *

# Add translations for all

# Fetch settings in Settings.ini
clock_speed = getSetting("clock")
battery_meter = getSetting("battery")
launch_welcome = getSetting("welcome")
theme = getSetting("theme")


# Button Events
def ButtonHandler(press):

    if press == "More Info":  # If user clicks More Info
        # Infobox showing info
        app.infoBox("More Information", "This program modifies a text file to change the clock speed of the processor.\nThe number shown on the slider marks the maximum clock speed of the CPU in MHz.\nIf the clock speed is low, the Raspberry Pi will draw less power with lower performance, if the clock speed is high, it will draw more power with more performance.\n\nNote: The default value is 1200MHz.")

    elif press == "Change Advanced Settings":
        Popen("/usr/bin/rc_gui")  # Runs Raspberry Pi Configuration

    elif press == "Languages":
        Popen("/usr/local/bin/Solar Pi/Resources/Launchers/language_launcher.sh")  # Runs Languages program

def SolarPiTheme():
    # Sets Solar Pi theme for application
    app.setTtkTheme("plastik")
    app.setTtkTheme("clam")

    # Highlighted button
    app.ttkStyle.configure("H.TButton", background="#324581", foreground="white", bordercolor="#687396")
    app.ttkStyle.map("H.TButton", background=[("pressed", "#172141"), ("active", "#4059a9")])

    # Regular button
    app.ttkStyle.configure("TButton", background="#dbdce2", bordercolor="#687396")

    # Fix CheckButton background
    app.ttkStyle.map("TCheckbutton", background=[("active", "white")])

    app.setButtonStyle("Apply ", "H.TButton")  # Set highlight button style to apply button

    app.ttkStyle.configure("Horizontal.TScale", troughcolor="light grey", sliderthickness="1", borderwidth="0", sliderrelief="flat")

    app.ttkStyle.configure("TLabelframe", bordercolor="#687396")  # LabelFrame border colour

    app.setBg("white")


def ClockChange(clock):
    # Opens and modifies config.txt file
    for line in fileinput.input(["/boot/config.txt"], inplace=True):
        if line.strip().startswith("arm_freq="):  # Searches for "arm_freq="
            line = "arm_freq=" + str(clock) + "\n"  # Replaces line with clock speed selected
        sys.stdout.write(line)  # Writes back to file

def ApplySettings(press):
    # Fetches data from widgets
    clock_speed = int(app.getEntry("Max Clock Speed: "))
    battery_meter = app.getCheckBox("Show battery meter")
    launch_welcome = app.getCheckBox("Launch the Solar Pi Welcome application at startup")
    theme = app.getOptionBox("Themes")
    if theme == "Solar Pi":
        SolarPiTheme()

    elif theme == "Black":
        app.setTtkTheme("black")

    else:
        # Sets options for other themes
        theme = theme.lower()
        app.setTtkTheme(theme)  # Sets theme
        app.ttkStyle.configure(".", background="white", foreground="black")  # Sets additional options for theme
        app.setLabelFrameStyle("Settings", "TFrame")  # Ensures that LabelFrame background is white
        app.ttkStyle.map("TCheckbutton", background=[("active", "white")])

    app.setFont(family="piboto")
    app.ttkStyle.configure(".", font=("piboto"))

    app.setScale("slider", clock_speed)  # Sets slider to value in entry

    setSetting("clock", str(clock_speed))
    setSetting("battery", str(battery_meter))
    setSetting("welcome", str(launch_welcome))
    if theme == "Solar Pi":
        setSetting("theme", "Solar Pi")
    else:
        setSetting("theme", theme.lower())

    Autorun("welcome", launch_welcome, "/home/pi/.config/autostart/Welcome Launcher.desktop")  # Takes programropriate action for running Welcome at startup

    Autorun("battery", battery_meter, "/home/pi/.config/autostart/Battery Meter Launcher.desktop")  # Takes programropriate action for running Battery meter at startup

    ClockChange(clock_speed)  # Modifies /boot/config.txt to change max clock

    # After settings have been changed
    if app.yesNoBox("Restart", "Your Solar Pi needs to be restarted in order for these changes to take effect.\nWould you like to restart now?") == True:  # Message to user to restart RPi
        Popen("/usr/local/bin/Solar Pi/Resources/Launchers/Reboot.sh")


def SetItems(clock_speed, battery_meter, launch_welcome, theme):  # Procedure to set controls
    app.setScale("slider", clock_speed)
    app.setCheckBox("Show battery meter", battery_meter)
    app.setCheckBox("Launch the Solar Pi Welcome application at startup", launch_welcome)
    if theme == "Solar Pi":
        app.setOptionBox("Themes", theme)
    else:
        app.setOptionBox("Themes", theme[0].upper() + theme[1:])


def Defaults(press):  # Procedure to reset to default
    setSetting("clock", "1200")
    setSetting("battery", "True")
    setSetting("welcome", "True")
    setSetting("theme", "Solar Pi")

    SolarPiTheme()  # Sets Solar Pi theme for application
    app.setFont(family="piboto")
    app.ttkStyle.configure(".", font=("piboto"))

    SetItems(1200, True, True, "Solar Pi")  # Sets controls to default

    Autorun("welcome", True, "/home/pi/.config/autostart/Welcome Launcher.desktop")  # Creates .desktop file for welcome

    Autorun("battery", True, "/home/pi/.config/autostart/Battery Meter Launcher.desktop")  # Creates .desktop file for battery meter

    ClockChange(1200)  # Changes max clock speed to 1200 MHz

    # Prompts user to restart to apply changes
    if app.yesNoBox("Restart", "Your Solar Pi needs to be restarted in order for these changes to take effect.\nWould you like to restart now?"):
        Popen("/usr/local/bin/Solar Pi/Resources/Launchers/Reboot.sh")

# Runs update scripts
def Update(press):
    if app.getCheckBox("Update Operating System & Installed Programs") == True:
        call("/usr/local/bin/Solar Pi/Resources/Launchers/System Update.sh")
    if app.getCheckBox("Update appJar") == True:
        call("/usr/local/bin/Solar Pi/Resources/Launchers/appJar Update.sh")

kill = False
def MeterUpdate():
    global kill
    i = 0
    while True:
        print(kill)
        if kill == True:
            app.queueFunction(app.setMeter, "update_meter", 0)
            break
        for i in range(1, 51):
            print(kill)
            i = i * 2
            app.queueFunction(app.setMeter, "update_meter", i)
            sleep(0.05)
            if kill == True:
                app.queueFunction(app.setMeter, "update_meter", 0)
                break


def update2(press):  # TODO: Fix threading issues
    global kill
    t = Thread(target=MeterUpdate)
    t.start()
    kill = False
    app.showSubWindow("Updating your Solar Pi")
    print("hi")

def stop():
    global kill
    kill = True
    app.hideSubWindow("Updating your Solar Pi")

# Sets entry based on scale changes
def ScaleChange(value):
    value = str(int(app.getScale("slider")))
    app.setEntry("Max Clock Speed: ", value)

# Sets scale based on entry
def EntryScaleChange(value):
    value = int(app.getEntry("Max Clock Speed: "))
    if value > 1200:  # Ensure that values are between 1200 and 600
        value = 1200
    elif value < 600:
        value = 600
    app.setScale("slider", value)
    print(value)


# Unicode symbols
TICK = "\u2714"
CROSS = "\u274C"
RESTORE = "\u21BA"

########################
#     Code for GUI     #
########################

with gui("Settings", useTtk=True) as app:
    app.setResizable(False)

    # Configures themes
    if theme == "Solar Pi":
        custom = True

    elif theme == "black":
        custom = False
        app.setTtkTheme(theme)

    else:
        custom = False
        app.setTtkTheme(theme)
        app.ttkStyle.configure(".", background="white", foreground="black")
        app.ttkStyle.map("TCheckbutton", background=[("active", "white")])
        app.setBg("white")

    pages = [" Performance & Power", " Updates", " Other Settings"]  # Sets settings pages

    def change(listName):
        app.getFrameWidget(app.listBox("list")[0]).lift()

    with app.labelFrame("Settings", sticky="nws", stretch="none", padding=[10, 10]):  # Create LabelFrame
        lb = app.listBox("list", pages, change=change,
                         activestyle="none", selectbackground="#687396", selectforeground="white",
                         selectmode=app.SINGLE, relief=app.FLAT)  # Create ListBox # selectborderwidth=5, relief=app.FLAT, selectrelief=app.FLAT
        app.configure(sticky="news", stretch="both")
        app.getListBoxWidget("list").config(font=("piboto", 14, "normal"))

        with app.frame(pages[0], 0, 1, sticky="new"):  # Create frame for each page
            app.setPadding(4, 4)

            app.addLabel("perf_title", "Performance & Power")
            app.getLabelWidget("perf_title").config(font=("piboto", 14, "normal"))

            app.addHorizontalSeparator(colspan=2)

            app.addLabel("title", "Change the CPU Clock Speed:", 2, 0, colspan=2)
            app.setLabelSticky("title", "ew")

            # Entry to display and enter clock speed
            app.addLabelNumericEntry("Max Clock Speed: ", 3, 0)
            app.setEntry("Max Clock Speed: ", str(clock_speed))
            app.setEntryMaxLength("Max Clock Speed: ", 4)
            app.setEntrySubmitFunction("Max Clock Speed: ", EntryScaleChange)
            app.addLabel("scale", "MHz", 3, 1)
            app.setLabelSticky("scale", "nws")

            # Scale
            app.addScale("slider", 4, 0)
            app.setScaleChangeFunction("slider", ScaleChange)
            app.setScaleSticky("slider", "ew")
            app.setScaleRange("slider", 600, 1200, curr=None)  # Changes scale range
            app.addButton("More Info", ButtonHandler, 4, 1)
            # Label
            app.addLabel("Info", "◄ Greater Battery Life       Performance ►", colspan=2)

            # Buttons
            app.addHorizontalSeparator(colspan=2)
            app.addCheckBox("Show battery meter", colspan=2)
            # app.setCheckBoxStyle("Show standalone battery meter", "TCheckbox")

        with app.frame(pages[1], 0, 1, sticky="new"):  # Code for second page
                app.setPadding(5, 5)
                app.addLabel("updates_title", "Updates")
                app.getLabelWidget("updates_title").config(font=("piboto", 14, "normal"))
                app.addHorizontalSeparator()
                #app.addLabel("update_info", "Note: This will only work with an internet connection.")
                #app.addCheckBox("Update Operating System & Installed Programs")
                #app.addCheckBox("Update appJar")
                #app.addButton("Update System", Update
                app.addLabel("update_info", "Please insert the update USB stick into the Solar Pi.\nPress 'Update' once you have done this.")
                app.addButton("Update", update2)

        with app.frame(pages[2], 0, 1, sticky="new"):  # Code for third page
                app.setPadding(5, 5)
                app.addLabel("other_title", "Other Settings")
                app.getLabelWidget("other_title").config(font=("piboto", 14, "normal"))
                app.addHorizontalSeparator(colspan=2)
                app.addCheckBox("Launch the Solar Pi Welcome application at startup", colspan=2)
                app.addLabel("themes", "Themes for Solar Pi apps:", 3, 0)
                themes = ["Solar Pi", "Plastik", "Arc", "Black", "Winxpblue"]
                app.addOptionBox("Themes", themes, 3, 1)
                app.addButton("Change Advanced Settings", ButtonHandler, 4, 0)
                app.addButton("Languages", ButtonHandler, 4, 1)
                app.setButtonSticky("Languages", "ew")
                app.setButtonSticky("Change Advanced Settings", "ew")

        app.configure(sticky="se", stretch="column")
        app.selectListItemAtPos("list", 0, callFunction=True)


    # Buttons to apply, restore defaults and exit
    with app.frame("frame3"):
        app.setPadding(10, 5)
        app.addImageButton("Apply ", ApplySettings, "../Resources/Images/tick.gif", 0, 0, align="right")
        app.addImageButton(" Restore Defaults ", Defaults, "../Resources/Images/restore.gif", 0, 1, align="right")
        app.addImageButton("Exit ", quit, "../Resources/Images/cross.gif", 0, 2, align="right")

    # Second window for updates
    with app.subWindow("Updating your Solar Pi", modal=True):
        app.setResizable(False)
        app.setStopFunction(stop)
        with app.frame("frame23"):
            app.setPadding(10, 10)
            app.addSplitMeter("update_meter")
            app.setMeterFill("update_meter", ["green", "white"])
            app.setMeterSticky("update_meter", "ew")
            app.addLabel("update_info2", "Please wait while we check the USB...")


    # Configure themes
    if custom == True:
        SolarPiTheme()  # Sets theme to Solar Pi theme
    else:
        app.setLabelFrameStyle("Settings", "TFrame")  # Ensures that LabelFrame background is white

    app.setFont(family="piboto")
    app.ttkStyle.configure(".", font=("piboto"))

    if theme == "black":
        app.setListBoxBg("list", "#424242")
        app.setListBoxFg("list", "white")


    SetItems(clock_speed, battery_meter, launch_welcome, theme)  # Sets controls to currently selected settings
