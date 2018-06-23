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
battery_meter = getSetting("battery_meter")
animation = getSetting("battery_animation")
launch_welcome = getSetting("welcome")
cow = getSetting("cow")
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

    if getSetting("language") == "spanish":
        app.setButtonStyle("Aplicar ", "H.TButton")
    else:
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

def Cowsay(show_cow):
    if show_cow == False:
        with open("/home/pi/.bashrc", "r") as f:
            d = f.readlines()
        with open("/home/pi/.bashrc", "w") as f:
            for line in d:
                if line.rstrip("\n") == "\"/usr/local/bin/Solar Pi/cowscript.sh\"" or line.rstrip("\n") == "# Cowsay!!":
                    pass
                else:
                    f.write(line)

    elif show_cow == True and getSetting("cow") == False:
        with open("/home/pi/.bashrc", "a") as f:
            cow_command = "# Cowsay!!\n\"/usr/local/bin/Solar Pi/cowscript.sh\""
            f.write(cow_command)

def ApplySettings(press):
    # Sets slider and entry value
    EntryScaleChange()
    ScaleChange()

    # Fetches data from widgets
    clock_speed = int(app.getScale("slider"))
    battery_meter = app.getCheckBox("Show battery meter")
    animation = app.getCheckBox("Show charging animation")
    launch_welcome = app.getCheckBox("Launch the Solar Pi Welcome application at startup")
    cow = app.getCheckBox("Show cowsay at terminal launch")
    theme = app.getOptionBox("Themes")

    # Configures theme
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

    # Sets font
    app.setFont(family="piboto")
    app.ttkStyle.configure(".", font=("piboto"))

    # Fetches previous setting
    clock_old = getSetting("clock")

    # Writes settings to Settings.ini file
    setSetting("clock", str(clock_speed))
    setSetting("battery_meter", str(battery_meter))
    setSetting("battery_animation", str(animation))
    setSetting("welcome", str(launch_welcome))
    Cowsay(cow)  # Configures cowsay
    setSetting("cow", str(cow))
    
    if theme == "Solar Pi":
        setSetting("theme", "Solar Pi")
    else:
        setSetting("theme", theme.lower())

    # Configures apps that run at startup
    Autorun("welcome", launch_welcome, "/home/pi/.config/autostart/Welcome Launcher.desktop")  # Takes programropriate action for running Welcome at startup

    #Autorun("battery", battery_meter, "/home/pi/.config/autostart/Battery Meter Launcher.desktop")  # Takes programropriate action for running Battery meter at startup

    ClockChange(clock_speed)  # Modifies /boot/config.txt to change max clock

    # After settings have been changed
    if clock_old != str(clock_speed):  # Only ask if clock speed has changed
        if app.yesNoBox("Restart", "Your Solar Pi needs to be restarted in order for these changes to take effect.\nWould you like to restart now?") == True:  # Message to user to restart RPi
            Popen("/usr/local/bin/Solar Pi/Resources/Launchers/Reboot.sh")


def SetItems(clock_speed, battery_meter, animation, launch_welcome, cow, theme):  # Procedure to set controls
    app.setScale("slider", clock_speed)
    app.setCheckBox("Show battery meter", battery_meter)
    app.setCheckBox("Show charging animation", animation)
    app.setCheckBox("Launch the Solar Pi Welcome application at startup", launch_welcome)
    app.setCheckBox("Show cowsay at terminal launch", cow)
    if theme == "Solar Pi":
        app.setOptionBox("Themes", theme)
    else:
        app.setOptionBox("Themes", theme[0].upper() + theme[1:])


def Defaults(press):  # Procedure to reset to default
    SetItems(clock_speed=1200, battery_meter=True, animation=True, launch_welcome=True, cow=True, theme="Solar Pi")  # Sets controls to default
    ApplySettings("Bananas")

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
def ScaleChange(value=None):
    value = str(int(app.getScale("slider")))
    app.setEntry("Max Clock Speed: ", value)

# Sets scale based on entry
def EntryScaleChange(value=None):
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

    pages = [" Performance & Power", " Other Settings", " Updates"]  # Sets settings pages
    if getSetting("language") == "spanish":
        pages = [" Rendimiento y potencia", " Otros ajustes", " Actualizaciones"]

    def change(listName):
        app.getFrameWidget(app.listBox("list")[0]).lift()

    with app.labelFrame("Settings", sticky="nws", stretch="none", padding=[10, 10]):  # Create LabelFrame
        lb = app.listBox("list", pages, change=change,
                         activestyle="none", selectbackground="#687396", selectforeground="white",
                         selectmode=app.SINGLE, relief=app.FLAT)  # Create ListBox # selectborderwidth=5, relief=app.FLAT, selectrelief=app.FLAT
        app.configure(sticky="news", stretch="both")
        app.getListBoxWidget("list").config(font=("piboto", 14, "normal"))
        app.setListBoxGroup("list", group=True)

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
            with app.frame("power", colspan=2):
                app.addCheckBox("Show battery meter", 0, 0)
                app.addCheckBox("Show charging animation", 0, 1)
            # app.setCheckBoxStyle("Show standalone battery meter", "TCheckbox")

        with app.frame(pages[1], 0, 1, sticky="new"):  # Code for third page
            app.setPadding(5, 5)
            app.addLabel("other_title", "Other Settings")
            app.getLabelWidget("other_title").config(font=("piboto", 14, "normal"))
            app.addHorizontalSeparator(colspan=2)
            app.addCheckBox("Launch the Solar Pi Welcome application at startup", colspan=2)
            app.addCheckBox("Show cowsay at terminal launch", colspan=2)
            app.addLabel("themes", "Themes for Solar Pi apps:", 4, 0)
            themes = ["Solar Pi", "Plastik", "Arc", "Winxpblue"]  # Black
            app.addOptionBox("Themes", themes, 4, 1)
            app.addButton("Change Advanced Settings", ButtonHandler, 5, 0)
            app.addButton("Languages", ButtonHandler, 5, 1)
            app.setButtonSticky("Languages", "ew")
            app.setButtonSticky("Change Advanced Settings", "ew")

        with app.frame(pages[2], 0, 1, sticky="new"):  # Code for second page
            app.setPadding(5, 5)
            app.addLabel("updates_title", "Updates")
            app.getLabelWidget("updates_title").config(font=("piboto", 14, "normal"))
            app.addHorizontalSeparator()
            app.addLabel("update_info", "Please insert the update USB stick into the Solar Pi.\nPress 'Update' once you have done this.")
            app.addButton("Update", update2)

        app.configure(sticky="se", stretch="column")
        app.selectListItemAtPos("list", 0, callFunction=True)


    # Buttons to apply, restore defaults and exit
    with app.frame("frame3"):
        app.setPadding(10, 5)
        if getSetting("language") == "spanish":
            app.addImageButton("Aplicar ", ApplySettings, "../Resources/Images/tick.gif", 0, 0, align="right")
            app.addImageButton(" Defecto ", Defaults, "../Resources/Images/restore.gif", 0, 1, align="right")
            app.addImageButton("Salida ", quit, "../Resources/Images/cross.gif", 0, 2, align="right")

        else:
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


    SetItems(clock_speed, battery_meter, animation, launch_welcome, cow, theme)  # Sets controls to currently selected settings

    app.changeLanguage(getSetting("language"))
