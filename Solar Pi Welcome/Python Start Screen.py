#!/usr/bin/env python3
# Solar Pi Welcome

from appJar import gui
from subprocess import Popen, call
#from AutorunConfig import Autorun
from sys import exit
from SettingsGet import LaunchWelcome
import webbrowser
from AutorunConfig import Autorun


with open("../Solar Pi Settings/Settings.ini", "r") as file:  # Read Settings.ini file
    data = file.readlines()[0]
data = data.split(",")
theme1 = data[3]

if theme1 == "Solar Pi":
    custom = True
else:
    custom = False

program = gui("Solar Pi Welcome", useTtk=True)
program.setResizable(False)
#program.setLocation("CENTER")

if custom == True:
    program.setTtkTheme("plastik")
    program.setTtkTheme("clam")
    #program.ttkStyle.configure(".", font="10")

    # Custom Notebook
    program.ttkStyle.configure("TNotebook", background="white")
    program.ttkStyle.map("TNotebook.Tab", background=[("selected", "#76a928")],  # Selected tab
                foreground=[("selected", "white")])
    program.ttkStyle.configure("TNotebook.Tab", background="#dbdce2", foreground="black")  # Unselected tab

    # Custom buttons

    # Highlighted button
    program.ttkStyle.configure("H.TButton", background="#324581", foreground="white", bordercolor="#687396")
    program.ttkStyle.map("H.TButton", background=[("pressed", "#172141"), ("active", "#4059a9")])

    # Regular button
    program.ttkStyle.configure("TButton", background="#dbdce2", bordercolor="#687396")

    program.ttkStyle.map("TCheckbutton", background=[("active", "white")])

elif custom == False:
    program.setTtkTheme(theme1)

# Event Handler for buttons
def ButtonHandler(press):
    #tab_selected = program.getTabbedFrameSelectedTab("MainTabs")  # Fetches the current tab

    if press == "Exit" or press == "Exit3" or press == "Exit2" or press == "Exit4":  # Exits program
        exit()  # Quits program
    elif press == " About":  # Opens the About subwindow
        program.showSubWindow("About Solar Pi")
    elif press == "Close":  # Closes the About subwindow
        program.hideSubWindow("About Solar Pi")
    elif press == "Scratch":  # Launches Scratch
        Popen("/usr/local/bin/Solar Pi/Resources/Launchers/Scratch Launcher.sh")
    elif press == "Python":  # Launches a Python IDE
        if program.yesNoBox("Python", "Would you like to use the Thonny Python IDE instead of the IDLE?") == True:
            Popen("/usr/local/bin/Solar Pi/Resources/Launchers/Thonny Launcher.sh")  # Launches Thonny
        else:
            Popen("/usr/local/bin/Solar Pi/Resources/Launchers/IDLE Launcher.sh")  # Launches IDLE
    elif press == "Java":  # Launches BlueJ
        Popen("/usr/local/bin/Solar Pi/Resources/Launchers/BlueJ Launcher.sh")
    elif press == "Change Advanced Settings":  # Launches RPi settings window
        Popen("/usr/bin/rc_gui")
    elif press == "  Languages":
        Popen("/usr/local/bin/Solar Pi/Resources/Launchers/language_launcher.sh")  # Launches settings for display language
    elif press == "Get Started":
        program.getNotebookWidget("MainTabs").select([1])  # Sets selected note/tab to Get Started

    elif press == "Charging":
        program.getNotebookWidget("MainTabs").select([2])  # Set selected note/tab to Charging


# Menu event handler
def MenuHandler(press):
    if press == "Shutdown":
        if program.yesNoBox("Shutdown", "Are you sure that you want to shutdown your Solar Pi now?") == True:
            Popen("/usr/local/bin/Solar Pi/Resources/Launchers/Shutdown.sh")  # Shuts down RPi
    elif press == "Reboot":
        if program.yesNoBox("Reboot", "Are you sure that you want to reboot your Solar Pi now?") == True:
            Popen("/usr/local/bin/Solar Pi/Resources/Launchers/Reboot.sh")  # Reboots RPi
    elif press == "Leafpad":
        Popen("/usr/local/bin/Solar Pi/Resources/Launchers/Leafpad Launcher.sh")  # Launches Leafpad
    elif press == "Start Programming":
        Programming(None)
    elif press == "Python Guides":
        PythonGuides(None)
    elif press == "Performance to Battery Life":
        PerfBattery(None)
    elif press == "All Files":
        Popen("/usr/local/bin/Solar Pi/Resources/Launchers/pcmanfm Launcher.sh")  # Launches file manager
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
        webbrowser.get("chromium-browser").open("http://localhost/solar-pi-apps/index.html#solar-pi-welcome")

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
    Popen("/usr/local/bin/Solar Pi/Resources/Launchers/Settings Launcher.sh")

def Guides(press):
    webbrowser.get("chromium-browser").open("http://localhost/")  # Launch guides here

def PythonIntro(press):  # RPi Python Introduction
    webbrowser.get("chromium-browser").open("http://localhost/Advanced-Things/python/index.html")
def Glossary(press):  # Programming Glossary
    webbrowser.get("chromium-browser").open("http://localhost/Glossaries/programming-glossary/index.html")
def ByteofPython(press):  # Byte of Python
    webbrowser.get("chromium-browser").open("http://localhost:81/")
def Java(press):  # Google's Python Tutorial
    webbrowser.get("chromium-browser").open("http://localhost:82/java/index.htm")


#program.setFont(11, font="Dejavu Sans")


# About Popup
with program.subWindow("About Solar Pi", modal=True):
    #program.setBg("white")
    with program.frame("frame7"):  # Rename to frame6 to remove right hand button column on Welcome tab
        program.setPadding(5, 5)
        program.setBg("white")
        program.addImage("solar_pi_logo", "../Resources/Images/Solar Pi logo.gif")
        program.zoomImage("solar_pi_logo", -3)
        program.setResizable(canResize=False)
        with program.labelFrame("About"):
            program.setBg("white")
            program.setPadding(10, 10)
            program.addMessage("about", "The Solar Pi is charity oriented project, aiming to deliver low cost Raspberry Pi based solar powered computers to developing countries. Our aim is to teach people how to code, so that they can become employed and move on financially and socially.\n\nWe hope that you enjoy your Solar Pi!")
            program.setMessageBg("about", "white")
        program.addButton("Close", ButtonHandler)
        program.setButtonSticky("Close", "")
        if custom == True:
            program.setButtonStyle("Close", "H.TButton")

# Menu bar
program.addMenuList("Power", ["Shutdown", "Reboot"], MenuHandler)
program.addMenuList("Applications", ["Leafpad", "Start Programming", "Performance to Battery Life"], MenuHandler)
program.addMenuList("Guides", ["Python Guides"], MenuHandler)
program.addMenuList("Files", ["All Files", "Desktop", "Documents", "Music", "Pictures", "Videos"], MenuHandler)


tools = ["Off", "Settings", "Files", "About", "Help"]
program.addToolbar(tools, ToolbarHandler, findIcon=True)
#if theme1 == "Solar Pi":
#    var = program.widgetManager.group(program.Widgets.Toolbar)
#    var["Off"].config(fg="#dbdce2")
#program.setToolbarFg("white")

# Main Window
program.setPadding(3, 3)

with program.notebook("MainTabs", colspan=2):
    with program.note("Welcome!"):
        program.setPadding(10, 10)
        with program.frame("frame4", 0, 0, colspan=3):
            program.addLabel("text4", "Welcome to your  ", 0, 0)
            program.setLabelAlign("text4", "right")
            program.getLabelWidget("text4").config(font=("Dejavu Sans", "20"))
            program.addImage("logo text1", "../Resources/Images/Solar Pi text small.gif", 0, 1)
            program.zoomImage("logo text1", -2)
            program.setImageSticky("logo text1", "nsw")

        with program.frame("frame5", 1, 0):
            program.setPadding(10, 10)
            if custom == True:
                program.addImageButton("Get Started", ButtonHandler, "../Resources/Images/md-play.gif", align="left", row=1, column=0)
            else:
                program.addIconButton("Get Started", ButtonHandler, "md-play", align="left", row=1, colspan=0)
            program.setButtonSticky("Get Started", "nesw")
            program.addImageButton(" Docs", Guides, "../Resources/Images/docs icon.gif", align="left", row=2, column=0)
            program.setButtonSticky(" Docs", "nesw")
            program.addIconButton(" About", ButtonHandler, "about", align="left", row=3, column=0)
            program.setButtonSticky(" About", "nesw")
        program.addImage("logo5", "../Resources/Images/Logo_NEW_2 small.gif", 1, 1, rowspan=3)
        program.zoomImage("logo5", -4)

        with program.frame("frame6", 1, 2):
            program.setPadding(10, 10)
            program.addImageButton("  Programming", Programming, "../Resources/Images/Programming icon small.gif",
                                   align="left", row=1, column=2)
            program.setButtonSticky("  Programming", "nesw")
            program.addIconButton(" Settings", Settings, "settings", align="left", row=2, column=2)
            program.setButtonSticky(" Settings", "nesw")
            program.addImageButton("  Languages", ButtonHandler, "../Resources/Images/languages small.gif",
                                   align="left", row=3, column=2)
            program.setButtonSticky("  Languages", "nesw")


        if custom == True:
            program.setButtonStyle("Get Started", "H.TButton")


    with program.note("Starter Guide"):

        program.setPadding(10, 10)
        program.addLabel("title", "Solar Pi Starter Guide", colspan=2)
        program.getLabelWidget("title").config(font=("Dejavu Sans", "15"))
        program.setLabelSticky("title", "ew")
        program.setLabelAlign("title", "center")
        program.addLabel("info1", "Your Solar Pi has a touchscreen. This means that\nyou can use your finger to touch the screen\nand control the computer.")
        program.addImage("desktop", "../Resources/Images/Desktop.gif", 1, 1, rowspan=2)
        program.zoomImage("desktop", -7)
        #program.addLabel("info1", "Your Solar Pi is a Raspberry Pi based\ncomputer. It can do almost anything you\nwant, if you know how to program it.\nWe aim to teach you how to use a computer\nand how to code, so that you have an\nadvantage over others when you get\nemployed.")
        program.addLabel("info2", "•  The image on the right is of the Solar Pi desktop.\n•  There is a bar at the top, showing you what\nwindows are open.\n•  At the top left, there is a button to open a\nmenu. From here, you can open all the\napplications that are installed on your Solar Pi.")

        with program.frame("frame"):
            program.addLabel("info4", "Read more:  ", 0, 0)
            program.setLabelAlign("info4", "right")
            program.addButton("Charging", ButtonHandler, 0, 1)

        if custom == True:
            program.setButtonStyle("Charging", "H.TButton")


    with program.note("Charging"):

        #program.setPadding(10, 10)
        program.addLabel("title5", "Charging your Solar Pi", colspan=3)
        program.getLabelWidget("title5").config(font=("Dejavu Sans", "15"))
        program.setLabelSticky("title5", "ew")
        program.setLabelAlign("title5", "center")
        text = """The battery meter below this page and in the
bottom left of the display shows how much power
is left in the batteries of your Solar Pi.
A full bar (100%) means most power, and an empty
bar (0%) means no power left.

When the battery meter gets close to 0% and your
Solar Pi shuts down, you need to charge it.
To do this, fold out the solar panels, and make
sure that the Solar Pi is facing the sun.
You will then need to wait for a few hours until it is
charged up.
Once your Solar Pi is charged, the battery meter
should show 100%."""
        program.addLabel("info5", text)
        program.setLabelAlign("info5", "center")
        #program.getLabelWidget("info5").config(font=("Piboto", "13"))

        program.addLabel("read", "Read more:", 1, 1)
        program.setLabelAnchor("read", "e")
        program.addButton("Starter Guide", Guides, 1, 2)
        program.setButtonSticky("Starter Guide", "")

        if custom == True:
            program.setButtonStyle("Starter Guide", "H.TButton")


    # Applications Tab
    with program.note("Applications"):

        with program.labelFrame("Applications"):
            program.setSticky("ew")
            program.setPadding(10, 10)
            program.addLabel("applications_info", "Hover over the icons to see more information about each program.", colspan=2)

            # Start Programming
            with program.labelFrame("Start Programming", 1, 0):
                program.setPadding(10, 15)
                program.addImage("programming_icon", "../Resources/Images/Programming icon cropped.gif", 0, 0)
                program.zoomImage("programming_icon", -13)
                program.setImageTooltip("programming_icon", "This allows you to see and try the different options for programming.")
                program.addButton("Start Programming", Programming, 0, 1)

            # Performance to Battery Life
            with program.labelFrame("Solar Pi Settings", 1, 1):
                program.setPadding(10, 10)
                program.addImage("settings", "../Resources/Images/settings icon.gif", 0, 0)
                program.zoomImage("settings", -5)
                program.setImageTooltip("settings", "This allows you to change the settings for your Solar Pi.")
                program.addButton("Solar Pi Settings", Settings, 0, 1)

            # IDEs
            with program.labelFrame("IDEs", 2, 0, colspan=2):
                program.setPadding(10, 10)
                program.setSticky("nesw")

                with program.labelFrame("Scratch", 1, 0):
                    program.setPadding(10, 10)
                    program.addImage("scratch_logo2", "../Resources/Images/scratch logo.gif", 0, 0)
                    program.zoomImage("scratch_logo2", -50)
                    program.setImageTooltip("scratch_logo2", "The Scratch 2 IDE. Create Scratch programs and games with this.")
                    program.addButton("Scratch", ButtonHandler, 0, 1)

                with program.labelFrame("Python", 1, 1):
                    program.setPadding(10, 10)
                    program.addImage("python_logo2", "../Resources/Images/Python icon.gif", 0, 0)
                    program.zoomImage("python_logo2", -4)
                    program.setImageTooltip("python_logo2", "The Python IDE. Write and run Python applications.")
                    program.addButton("Python", ButtonHandler, 0, 1)

                with program.labelFrame("Java", 1, 2):
                    program.setPadding(10, 10)
                    program.addImage("java_logo", "../Resources/Images/java logo.gif", 0, 0)
                    program.zoomImage("java_logo", -5)
                    program.setImageTooltip("java_logo", "The BlueJ Java IDE. Create Java applications.")
                    program.addButton("Java", ButtonHandler, 0, 1)

        if custom == True:
            program.setButtonStyle("Start Programming", "H.TButton")


    # Guides & Tutorials Tab
    with program.note("Guides & Tutorials"):

        with program.labelFrame("Guides & Tutorials"):
            program.setSticky("ew")
            program.setPadding(10, 10)
            program.addLabel("guides_info", "Hover over the icons to see more information about each resource.", 0, 0, colspan=2)
            #    program.addImage("python", "../Resources/Images/Python icon.gif", 0, 1)
             #   program.zoomImage("python", -2)

            # RPi Foundation Python Tutorial
            with program.labelFrame("Introduction to Python", 1, 0):
                program.setPadding(10, 10)
                program.addImage("python2", "../Resources/Images/Python icon.gif", 0, 0)
                program.zoomImage("python2", -4)
                program.setImageTooltip("python2", "An introduction to Python, written by the Raspberry Pi Foundation")
                program.addButton("Python Intro", PythonIntro, 0, 1)

            # Programming Glossary
            with program.labelFrame("Programming Glossary", 1, 1):
                program.setPadding(10, 10)
                program.addImage("programming_icon2", "../Resources/Images/Programming icon cropped.gif", 0, 0)
                program.zoomImage("programming_icon2", -10)
                program.setImageTooltip("programming_icon2", "Gives you definitions of words that you might not have heard before")
                program.addButton("Glossary", Glossary, 0, 1)

            # A Byte of Python
            with program.labelFrame("A Byte of Python", 2, 0):
                program.setPadding(10, 10)
                program.addImage("python3", "../Resources/Images/Python icon.gif", 0, 0)
                program.zoomImage("python3", -4)
                program.setImageTooltip("python3", "A popular Ebook that teaches you Python")
                program.addButton("A Byte of Python", ByteofPython, 0, 1)

            # Google Python Tutorial
            with program.labelFrame("Java Guide", 2, 1):
                program.setPadding(10, 10)
                program.addImage("java_logo2", "../Resources/Images/java logo.gif", 0, 0)
                program.zoomImage("java_logo2", -5)
                program.setImageTooltip("java_logo2", "A guide on Java to help you get to know the basics of Java 8")
                program.addButton("Java Guide", Java, 0, 1)


        if custom == True:
            program.setButtonStyle("Python Intro", "H.TButton")



def Startup(param):
    value = program.getCheckBox("Launch at startup")
    with open("../Solar Pi Settings/Settings.ini", "r") as file:
        data = file.readlines()
    data = data[0]
    data = data.split(",")
    clock = data[0]
    battery = data[1]
    welcome = str(value)
    theme = data[3]

    data = clock + "," + battery + "," + welcome + "," + theme
    with open("../Solar Pi Settings/Settings.ini", "w") as file:
        file.write(data)
    
    Autorun("welcome", value, "/home/pi/.config/autostart/Welcome Launcher.desktop")

program.setPadding(5, 5)
program.addCheckBox("Launch at startup", 1, 0)
program.setCheckBox("Launch at startup", ticked=LaunchWelcome())
program.setCheckBoxChangeFunction("Launch at startup", Startup)


num = 0
def updateMeter():
    global num
    program.setMeter("battery", num)
    #program.setLabel("level", str(num)+"%")
    num += 1
with program.frame("battery", 1, 1):
    program.addLabel("battery", "Battery Remaining: ", 0, 0)  # Update translation
    #program.setLabelAlign("battery", "right")
    program.setLabelAnchor("battery", "e")
    program.addMeter("battery", 0, 2)
    program.setMeterFill("battery", "#13d323")
    program.addLabel("blank", "", 0, 3)
    #program.setMeterPadding("battery", 5, 5)
    program.registerEvent(updateMeter)
    program.setPollTime(10000)


with open("language.txt", "r") as file:
    lang = file.readline()
    lang.rstrip("\n")

#print(lang)
#program.setLabelFrameStyle("-", "TFrame")
#program.setLabelFrameStyle("", "TFrame")
#program.ttkStyle.configure(".", background="white", foreground="black")
program.ttkStyle.configure("TLabelframe", background="white")

if custom == False:
    program.setLabelFrameStyle("Applications", "TFrame")
    program.setLabelFrameStyle("Start Programming", "TFrame")
    program.setLabelFrameStyle("Solar Pi Settings", "TFrame")
    program.setLabelFrameStyle("IDEs", "TFrame")
    program.setLabelFrameStyle("Scratch", "TFrame")
    program.setLabelFrameStyle("Python", "TFrame")
    program.setLabelFrameStyle("Java", "TFrame")
    program.setLabelFrameStyle("Guides & Tutorials", "TFrame")
    program.setLabelFrameStyle("Introduction to Python", "TFrame")
    program.setLabelFrameStyle("Programming Glossary", "TFrame")
    program.setLabelFrameStyle("A Byte of Python", "TFrame")
    program.setLabelFrameStyle("Java Guide", "TFrame")
    program.setLabelFrameStyle("About", "TFrame")

#print(program.ttkStyle.lookup("TFrame", "bordercolor"))

program.go(language=lang)
