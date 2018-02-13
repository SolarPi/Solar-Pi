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

app = gui("Solar Pi Welcome", useTtk=True)
app.setResizable(False)
#app.setLocation("CENTER")

if theme1 == "Solar Pi":
    msgFg = "black"
    msgBg = "white"
    solar_theme = True
else:
    solar_theme = False
    app.setTtkTheme(theme1)
    msgFg = "white"
    msgBg = "#424242"
    if theme1 != "black":
        app.ttkStyle.configure(".", foreground="black", background="white")
        app.ttkStyle.map("TCheckbutton", background=[("active", "white")])
        app.setBg("white")
        msgFg = "black"
        msgBg = "white"

if solar_theme == True:
    app.setTtkTheme("plastik")
    app.setTtkTheme("clam")
    #app.ttkStyle.configure(".", font="10")

    # Custom Notebook
    app.ttkStyle.configure("TNotebook", background="white", bordercolor="#687396")
    app.ttkStyle.map("TNotebook.Tab", background=[("selected", "#76a928")],  # Selected tab
                foreground=[("selected", "white")])
    app.ttkStyle.configure("TNotebook.Tab", background="#dbdce2", foreground="black", bordercolor="#687396")  # Unselected tab

    # Custom buttons

    # Highlighted button
    app.ttkStyle.configure("H.TButton", background="#324581", foreground="white", bordercolor="#687396")
    app.ttkStyle.map("H.TButton", background=[("pressed", "#172141"), ("active", "#4059a9")])

    app.ttkStyle.map("TCheckbutton", background=[("active", "white")])

    # Regular button
    app.ttkStyle.configure("TButton", background="#dbdce2", bordercolor="#687396")

    app.ttkStyle.map("TLabelFrame", border=[("active", "black")])

    app.ttkStyle.configure("TLabelframe", bordercolor="#687396")

title_font = ("ubuntu", 14, "normal")
app.ttkStyle.configure("H.TLabel", background="#687396", foreground="white", padding=[10, 10]) # #dbdce2, #687396
app.ttkStyle.configure("Info.TLabel", padding=[10, 10])

# Event Handler for buttons
def ButtonHandler(press):
    #tab_selected = app.getTabbedFrameSelectedTab("MainTabs")  # Fetches the current tab
    press = press.lower()

    if press == "Exit" or press == "Exit3" or press == "Exit2" or press == "Exit4":  # Exits program
        exit()  # Quits program
    elif press == " about": app.showSubWindow("About Solar Pi")  # Opens the About subwindow
    elif press == "close": app.hideSubWindow("About Solar Pi")  # Closes the About subwindow
    elif press == "libreoffice_close": app.hideSubWindow("Libreoffice")

    #elif press == "scratch": Popen("../Resources/Launchers/Scratch Launcher.sh")  # Launches Scratch
    #elif press == "python":  # Launches a Python IDE
        #Popen("../Resources/Launchers/Thonny Launcher.sh")  # Launches Thonny
    #elif press == "java": Popen("../Resources/Launchers/BlueJ Launcher.sh")  # Launches BlueJ
    elif press == "change advanced settings": Popen("/usr/bin/rc_gui")  # Launches RPi settings window
    elif press == "  languages": Popen("../Resources/Launchers/language_launcher.sh")  # Launches settings for display language

    elif press == "get started": app.getNotebookWidget("MainTabs").select([1])  # Sets selected note/tab to Get Started
    elif press == "charging": app.getNotebookWidget("MainTabs").select([2])  # Set selected note/tab to Charging
    else:
        Popen("../Resources/Launchers/" + press + " launcher.sh")


# Menu event handler
def MenuHandler(press):
    if press == "Shutdown":
        if app.yesNoBox("Shutdown", "Are you sure that you want to shutdown your Solar Pi now?") == True:
            Popen("../Resources/Launchers/Shutdown.sh")  # Shuts down RPi
    elif press == "Reboot":
        if app.yesNoBox("Reboot", "Are you sure that you want to reboot your Solar Pi now?") == True:
            Popen("../Resources/Launchers/Reboot.sh")  # Reboots RPi
    #elif press == "Leafpad":
     #   Popen("../Resources/Launchers/Leafpad Launcher.sh")  # Launches Leafpad
    elif press == "Start Programming":
        Programming(None)
    elif press == "Python Guides":
        PythonGuides(None)
    elif press == "Performance to Battery Life":
        PerfBattery(None)
    elif press == "All Files":
        Popen("../Resources/Launchers/pcmanfm Launcher.sh")  # Launches file manager
    else:
        Popen("../Resources/Launchers/" + press + " Launcher.sh")
    # elif press == "Desktop":
    #     Popen("../Resources/Launchers/Desktop Launcher.sh")
    # elif press == "Documents":
    #     Popen("../Resources/Launchers/Documents Launcher.sh")
    # elif press == "Music":
    #     Popen("../Resources/Launchers/Music Launcher.sh")
    # elif press == "Pictures":
    #     Popen("../Resources/Launchers/Pictures Launcher.sh")
    # elif press == "Videos":
    #     Popen("../Resources/Launchers/Videos Launcher.sh")

def ToolbarHandler(press):
    if press == "Off":
        Popen("/usr/bin/lxde-pi-shutdown-helper")
    elif press == "Settings":
        Popen("../Resources/Launchers/Settings Launcher.sh")  # Call Settings menu
    elif press == "Files":
        Popen("../Resources/Launchers/pcmanfm Launcher.sh")
    elif press == "About":
        app.showSubWindow("About Solar Pi")
    elif press == "Help":
        webbrowser.get("chromium-browser").open("http://localhost/solar-pi-apps/index.html#solar-pi-welcome")

def PerfBattery(press):
    Popen("../Resources/Launchers/Perf Battery Launcher.sh")
def Programming(press):
    Popen("../Resources/Launchers/Programming Launcher.sh")
def PythonGuides(press):
    Popen("../Resources/Launchers/Python Guide Launcher.sh")
# def Update(press):
#     box1 = app.getCheckBox("Update Operating System & Installed Programs")
#     box2 = app.getCheckBox("Update appJar")
#     if box1 == True:
#         call("../Resources/Launchers/System Update.sh")
#     if box2 == True:
#         call("../Resources/Launchers/appJar Update.sh")
def Settings(press):
    Popen("../Resources/Launchers/Settings Launcher.sh")

def Libreoffice(press):
    press = press.lower()
    if press == "libreoffice":
        app.showSubWindow("Libreoffice")
    else:
        Popen("../Resources/Launchers/" + press + "launcher.sh")  # TODO: Create launchers

def Docs(press):
    webbrowser.get("chromium-browser").open("http://localhost/")  # Launch guides here

def PythonIntro(press):  # RPi Python Introduction
    webbrowser.get("chromium-browser").open("http://localhost/Advanced-Things/python/index.html")
def Glossary(press):  # Programming Glossary
    webbrowser.get("chromium-browser").open("http://localhost/Glossaries/programming-glossary/index.html")
def ByteofPython(press):  # Byte of Python
    webbrowser.get("chromium-browser").open("http://localhost:81/")
def Java(press):  # Google's Python Tutorial
    webbrowser.get("chromium-browser").open("http://localhost:82/java/index.htm")


#app.setFont(11, font="Dejavu Sans")

# About Popup
with app.subWindow("About Solar Pi", modal=True):
    app.setResizable(canResize=False)
    #app.setBg("white")
    with app.frame("frame7"):  # Rename to frame6 to remove right hand button column on Welcome tab
        app.setPadding(10, 10)
        #app.setBg("white")
        app.addImage("solar_pi_logo", "../Resources/Images/Solar Pi logo.gif")
        app.zoomImage("solar_pi_logo", -3)
        with app.labelFrame("About"):
            #app.setBg("white")
            app.setPadding(10, 10)
            app.addMessage("about", "The Solar Pi is charity oriented project, aiming to deliver low cost Raspberry Pi based solar powered computers to developing countries. Our aim is to teach people how to code, so that they can become employed and move on financially and socially.\n\nWe hope that you enjoy your Solar Pi!")
            app.setMessageBg("about", msgBg)
            app.setMessageFg("about", msgFg)
        app.addButton("Close", ButtonHandler)
        app.setButtonSticky("Close", "")
        if solar_theme == True:
            app.setButtonStyle("Close", "H.TButton")

with app.subWindow("Libreoffice", modal=True):
    app.setResizable(False)
    with app.frame("frame23"):
        app.setPadding(10, 10)
        with app.labelFrame("Libreoffice"):
            app.setPadding(10, 10)
            with app.frame("writer", 0, 0):
                app.setPadding(10, 10)
                app.addImage("writer", "../Resources/Images/writer.gif", 0, 0)
                app.setImageTooltip("writer", "A simple, easy to use word processor.")
                app.addButton("Writer", Libreoffice, 0, 1)
            with app.frame("calc", 0, 1):
                app.setPadding(10, 10)
                app.addImage("calc", "../Resources/Images/calc.gif", 0, 0)
                app.setImageTooltip("calc", "Quickly make speadsheets and crunch numbers.")
                app.addButton("Calc", Libreoffice, 0, 1)
            with app.frame("impress", 1, 0):
                app.setPadding(10, 10)
                app.addImage("impress", "../Resources/Images/impress.gif", 0, 0)
                app.setImageTooltip("impress", "Create presentations!")
                app.addButton("Impress", Libreoffice, 0, 1)
            with app.frame("Draw", 1, 1):
                app.setPadding(10, 10)
                app.addImage("draw", "../Resources/Images/draw.gif", 0, 0)
                app.setImageTooltip("draw", "Show off your art skills!")
                app.addButton("Draw", Libreoffice, 0, 1)
        app.addNamedButton("Close", "libreoffice_close", ButtonHandler)
        app.setButtonSticky("libreoffice_close", "")
        if solar_theme == True:
            app.setButtonStyle("libreoffice_close", "H.TButton")


# Menu bar
app.addMenuList("Power", ["Shutdown", "Reboot"], MenuHandler)
app.addMenuList("Applications", ["Leafpad", "Start Programming", "Performance to Battery Life"], MenuHandler)
app.addMenuList("Guides", ["Python Guides"], MenuHandler)
app.addMenuList("Files", ["All Files", "Desktop", "Documents", "Music", "Pictures", "Videos"], MenuHandler)


tools = ["Off", "Settings", "Files", "About", "Help"]
app.addToolbar(tools, ToolbarHandler, findIcon=True)
#if theme1 == "Solar Pi":
#    var = app.widgetManager.group(app.Widgets.Toolbar)
#    var["Off"].config(fg="#dbdce2")
#app.setToolbarFg("white")


# Main Window
app.setPadding(3, 3)

with app.notebook("MainTabs", colspan=2):
    with app.note("Welcome!"):
        app.setPadding(10, 10)
        with app.frame("frame4", 0, 0, colspan=3):
            app.addLabel("text4", "Welcome to your  ", 0, 0)
            app.setLabelAlign("text4", "right")
            app.getLabelWidget("text4").config(font=("ubuntu", "20"))
            app.addImage("logo text1", "../Resources/Images/Solar Pi text small.gif", 0, 1)
            app.zoomImage("logo text1", -2)
            app.setImageSticky("logo text1", "nsw")

        with app.frame("frame5", 1, 0):
            app.setPadding(10, 10)
            if solar_theme == True or theme1 == "black":
                app.addImageButton("Get Started", ButtonHandler, "../Resources/Images/md-play.gif", align="left", row=1, column=0)
            else:
                app.addIconButton("Get Started", ButtonHandler, "md-play", align="left", row=1, colspan=0)
            app.setButtonSticky("Get Started", "nesw")
            app.addImageButton(" Docs", Docs, "../Resources/Images/docs icon.gif", align="left", row=2, column=0)
            app.setButtonSticky(" Docs", "nesw")
            app.addIconButton(" About", ButtonHandler, "about", align="left", row=3, column=0)
            app.setButtonSticky(" About", "nesw")
        app.addImage("logo5", "../Resources/Images/Logo_NEW_2 small.gif", 1, 1, rowspan=3)
        app.zoomImage("logo5", -4)

        with app.frame("frame6", 1, 2):
            app.setPadding(10, 10)
            app.addImageButton("  Coding", Programming, "../Resources/Images/Programming icon small.gif",
                                   align="left", row=1, column=2)
            app.setButtonSticky("  Coding", "nesw")
            app.addIconButton(" Settings", Settings, "settings", align="left", row=2, column=2)
            app.setButtonSticky(" Settings", "nesw")
            app.addImageButton("  Languages", ButtonHandler, "../Resources/Images/languages small.gif",
                                   align="left", row=3, column=2)
            app.setButtonSticky("  Languages", "nesw")


        if solar_theme == True:
            app.setButtonStyle("Get Started", "H.TButton")


    with app.note("Starter Guide"):
        with app.scrollPane("scroll1"):
            app.addLabel("starter_title", "Solar Pi Starter Guide", colspan=2)
            app.getLabelWidget("starter_title").config(font=title_font)
            app.setLabelStyle("starter_title", "H.TLabel")
            #app.setLabelSticky("title", "ew")
            #app.setLabelAlign("title", "center")
            #app.addLabel("info1", "Your Solar Pi has a touchscreen. This means that\nyou can use your finger to touch the screen\nand control the computer.")

            with app.frame("frame19"):
                app.setPadding(10, 10)
                app.addImage("desktop", "../Resources/Images/Desktop.gif", 0, 1)
                app.zoomImage("desktop", -7)
                #app.addLabel("info1", "Your Solar Pi is a Raspberry Pi based\ncomputer. It can do almost anything you\nwant, if you know how to program it.\nWe aim to teach you how to use a computer\nand how to code, so that you have an\nadvantage over others when you get\nemployed.")
                #app.addLabel("info2", "

                starter_info = """Your Solar Pi has a touchscreen. This means that you can use your finger to touch the screen and control the computer.
        
•  The image on the right is of the Solar Pi desktop.
•  There is a bar at the top, showing you what windows are open.
•  At the top left, there is a button to open a menu. From here, you can see and run all of the applications that are installed on your Solar Pi."""
                app.addMessage("starter_info", starter_info, 0, 0)
                app.setMessageBg("starter_info", msgBg)
                app.setMessageFg("starter_info", msgFg)
                app.setMessageSticky("starter_info", "nesw")

                with app.frame("frame"):
                    app.addLabel("info4", "Read more:  ", 0, 0)
                    app.setLabelAlign("info4", "right")
                    app.addNamedButton("Docs", "docs", ButtonHandler, 0, 1)

            app.addHorizontalSeparator()

            app.addLabel("charging_title", "Charging your Solar Pi", colspan=3)
            app.setLabelStyle("charging_title", "H.TLabel")
            app.getLabelWidget("charging_title").config(font=title_font)
            #app.setLabelSticky("title5", "ew")
            #app.setLabelAlign("title5", "center")
            with app.frame("frame20"):
                app.setPadding(10, 10)
                app.setStretch("columns")
                charge_info = """The battery meter below this page and in the bottom left of the display shows how much power is left in the batteries of your Solar Pi. A full bar (100%) means most power, and an empty bar (0%) means no power left.
When the battery meter gets close to 0% and your Solar Pi shuts down, you need to charge it. To do this, fold out the solar panels, and make sure that the Solar Pi is facing the sun. You will then need to wait for a few hours until it is charged up.
Once your Solar Pi is charged, the battery meter should show 100%."""
                # app.addLabel("info5", text)
                # app.setLabelAlign("info5", "center")
                # app.getLabelWidget("info5").config(font=("Piboto", "13"))

                app.addMessage("charge_info", charge_info)
                app.setMessageBg("charge_info", msgBg)
                app.setMessageFg("charge_info", msgFg)

                with app.frame("frame21"):
                    app.addLabel("read", "Read more:", 0, 0)
                    app.setLabelAnchor("read", "e")
                    app.addButton("Starter Guide", Docs, 0, 1)
                    app.setButtonSticky("Starter Guide", "")

            if solar_theme == True:
                app.setButtonStyle("docs", "H.TButton")
                app.setButtonStyle("Starter Guide", "H.TButton")


#     with app.note("Charging"):
#
#         #app.setPadding(10, 10)
#         app.addLabel("title5", "Charging your Solar Pi", colspan=3)
#         app.getLabelWidget("title5").config(font=("Dejavu Sans", "15"))
#         app.setLabelSticky("title5", "ew")
#         app.setLabelAlign("title5", "center")
#         charge_info = """The battery meter below this page and in the bottom left of the display shows how much power is left in the batteries of your Solar Pi. A full bar (100%) means most power, and an empty bar (0%) means no power left.
# When the battery meter gets close to 0% and your Solar Pi shuts down, you need to charge it. To do this, fold out the solar panels, and make sure that the Solar Pi is facing the sun. You will then need to wait for a few hours until it is charged up.
# Once your Solar Pi is charged, the battery meter should show 100%."""
#         #app.addLabel("info5", text)
#         #app.setLabelAlign("info5", "center")
#         #app.getLabelWidget("info5").config(font=("Piboto", "13"))
#
#         app.addMessage("charge_info", charge_info)
#         app.setMessageBg("charge_info", msgBg)
#         app.setMessageFg("charge_info", msgFg)
#         app.setMessageSticky("charge_info", "nesw")
#
#         app.addLabel("read", "Read more:", 1, 1)
#         app.setLabelAnchor("read", "e")
#         app.addButton("Starter Guide", Docs, 1, 2)
#         app.setButtonSticky("Starter Guide", "")
#
#         if solar_theme == True:
#             app.setButtonStyle("Starter Guide", "H.TButton")

    """

    # Applications Tab
    with app.note("Applications"):

        with app.labelFrame("Applications"):
            app.setSticky("ew")
            app.setPadding(10, 10)
            app.addLabel("applications_info", "Hover over the icons to see more information about each app.", colspan=2)

            # Start Programming
            with app.labelFrame("Start Programming", 1, 0):
                app.setPadding(10, 15)
                app.addImage("programming_icon", "../Resources/Images/Programming icon cropped.gif", 0, 0)
                app.zoomImage("programming_icon", -13)
                app.setImageTooltip("programming_icon", "This allows you to see and try the different options for programming.")
                app.addButton("Start Programming", Programming, 0, 1)

            # Performance to Battery Life
            with app.labelFrame("Solar Pi Settings", 1, 1):
                app.setPadding(10, 10)
                app.addImage("settings", "../Resources/Images/settings icon.gif", 0, 0)
                app.zoomImage("settings", -5)
                app.setImageTooltip("settings", "This allows you to change the settings for your Solar Pi.")
                app.addButton("Solar Pi Settings", Settings, 0, 1)

            # IDEs
            with app.labelFrame("IDEs", 2, 0, colspan=2):
                app.setPadding(10, 10)
                app.setSticky("nesw")

                with app.labelFrame("Scratch", 1, 0):
                    app.setPadding(10, 10)
                    app.addImage("scratch_logo2", "../Resources/Images/scratch logo.gif", 0, 0)
                    app.zoomImage("scratch_logo2", -50)
                    app.setImageTooltip("scratch_logo2", "The Scratch 2 IDE. Create Scratch programs and games with this.")
                    app.addButton("Scratch", ButtonHandler, 0, 1)

                with app.labelFrame("Python", 1, 1):
                    app.setPadding(10, 10)
                    app.addImage("python_logo2", "../Resources/Images/Python icon.gif", 0, 0)
                    app.zoomImage("python_logo2", -4)
                    app.setImageTooltip("python_logo2", "The Python IDE. Write and run Python applications.")
                    app.addButton("Python", ButtonHandler, 0, 1)

                with app.labelFrame("Java", 1, 2):
                    app.setPadding(10, 10)
                    app.addImage("java_logo", "../Resources/Images/java logo.gif", 0, 0)
                    app.zoomImage("java_logo", -5)
                    app.setImageTooltip("java_logo", "The BlueJ Java IDE. Create Java applications.")
                    app.addButton("Java", ButtonHandler, 0, 1)

        if solar_theme == True:
            app.setButtonStyle("Start Programming", "H.TButton")

    """

    with app.note("Applications"):

        with app.labelFrame("Applications"):
            app.setSticky("ew")
            app.setPadding(10, 10)
            app.addLabel("applications_info", "Hover over the icons to see more information about each app.", colspan=2)

            with app.labelFrame("Solar Pi Apps"):
                # Start Programming
                app.setPadding(10, 10)
                with app.frame("Start Programming", 1, 0):
                    app.setPadding(10, 10)
                    app.addImage("programming_icon", "../Resources/Images/Programming icon cropped.gif", 0, 0)
                    app.zoomImage("programming_icon", -13)
                    app.setImageTooltip("programming_icon", "This allows you to see and try the different options for coding.")
                    app.addButton("Start Coding", Programming, 0, 1)
                app.setFrameSticky("Start Programming", "nesw")

                # Performance to Battery Life
                with app.frame("Solar Pi Settings", 1, 1):
                    app.setPadding(10, 10)
                    app.addImage("settings", "../Resources/Images/settings icon.gif", 0, 0)
                    app.zoomImage("settings", -5)
                    app.setImageTooltip("settings", "This allows you to change the settings for your Solar Pi.")
                    app.addButton("Solar Pi Settings", Settings, 0, 1)

                with app.frame("libreoffice", 1, 2):
                    app.setPadding(10, 10)
                    app.addImage("libreoffice", "../Resources/Images/writer.gif", 0, 0)
                    app.setImageTooltip("libreoffice", "A free office suite - create documents, presentations and spreadsheets.")
                    app.addButton("Libreoffice", Libreoffice, 0, 1)

            # IDEs
            with app.labelFrame("IDEs", 2, 0, colspan=2):
                app.setPadding(10, 10)
                app.setSticky("nesw")

                with app.frame("Scratch", 1, 0):
                    app.setPadding(10, 10)
                    app.addImage("scratch_logo2", "../Resources/Images/scratch logo.gif", 0, 0)
                    app.zoomImage("scratch_logo2", -50)
                    app.setImageTooltip("scratch_logo2", "The Scratch 2 IDE. Create Scratch programs and games with this.")
                    app.addButton("Scratch", ButtonHandler, 0, 1)

                with app.frame("Python", 1, 1):
                    app.setPadding(10, 10)
                    app.addImage("python_logo2", "../Resources/Images/Python icon.gif", 0, 0)
                    app.zoomImage("python_logo2", -4)
                    app.setImageTooltip("python_logo2", "The Python IDE. Write and run Python applications.")
                    app.addNamedButton("Python", "thonny", ButtonHandler, 0, 1)

                with app.frame("Java", 1, 2):
                    app.setPadding(10, 10)
                    app.addImage("java_logo", "../Resources/Images/java logo.gif", 0, 0)
                    app.zoomImage("java_logo", -5)
                    app.setImageTooltip("java_logo", "The BlueJ Java IDE. Create Java applications.")
                    app.addNamedButton("Java", "bluej", ButtonHandler, 0, 1)


        if solar_theme == True:
            app.setButtonStyle("Start Coding", "H.TButton")

    """

    with app.note("Applications b"):
        app.setSticky("nesw")
        app.setPadding(0, 0)

        with app.scrollPane("scroll"):
            app.setPadding(0, 0)
            app.setSticky("nesw")
            app.addLabel("applications_title", "Solar Pi Applications")
            app.setLabelStyle("applications_title", "H.TLabel")
            app.getLabelWidget("applications_title").config(font=("ubuntu", 15, "normal"))

            app.addHorizontalSeparator()

            app.addLabel("coding_title", "Start Coding", colspan=3)
            #app.setLabelAlign("coding_title", "center")
            app.setLabelStyle("coding_title", "Info.TLabel")
            app.getLabelWidget("coding_title").config(font=title_font)
            with app.frame("frame8"):
                app.setPadding(10, 10)
                app.addImage("coding_icon", "../Resources/Images/Programming icon cropped.gif", 0, 0)
                app.zoomImage("coding_icon", -13)
                app.addLabel("coding_info", "This allows you to see and try the different options for coding.", 0, 1)
                #app.addLabel("coding_info", "Cela vous permet de voir et d'essayer les différentes options de programmation.", 0, 1)
                app.addNamedButton("Try it out!", "tryit1", Programming, 0, 2)

            app.addHorizontalSeparator()

            app.addLabel("settings_title", "Solar Pi Settings")
            app.setLabelStyle("settings_title", "Info.TLabel")
            app.getLabelWidget("settings_title").config(font=title_font)
            with app.frame("frame9"):
                app.setPadding(10, 10)
                app.addImage("settings_icon", "../Resources/Images/settings icon.gif", 0, 0)
                app.zoomImage("settings_icon", -6)
                app.addLabel("settings_info", "This allows you to change the settings for your Solar Pi.", 0, 1)
                app.addButton("Settings", Settings, 0, 2)

            #app.addHorizontalSeparator()
            app.addLabel("filler", "")

            app.addLabel("ides", "IDEs (Places where you can code)")
            app.setLabelStyle("ides", "H.TLabel")
            app.getLabelWidget("ides").config(font=title_font)
            app.addHorizontalSeparator()

            app.addLabel("scratch_title", "Scratch")
            app.setLabelStyle("scratch_title", "Info.TLabel")
            app.getLabelWidget("scratch_title").config(font=title_font)
            with app.frame("frame10"):
                app.setPadding(10, 10)
                app.addImage("scratch_icon", "../Resources/Images/scratch logo.gif", 0, 0)
                app.zoomImage("scratch_icon", -50)
                app.addLabel("scratch_info", "The Scratch 2 IDE. Create Scratch programs and games with this.", 0, 1)
                app.addNamedButton("Scratch", "scratch", ButtonHandler, 0, 2)

            app.addHorizontalSeparator()

            app.addLabel("python_title", "Python")
            app.setLabelStyle("python_title", "Info.TLabel")
            app.getLabelWidget("python_title").config(font=title_font)
            with app.frame("frame11"):
                app.setPadding(10, 10)
                app.addImage("python_icon", "../Resources/Images/Python icon.gif", 0, 0)
                app.zoomImage("python_icon", -4)
                app.addLabel("python_icon", "The Python IDE. Write and run Python applications.", 0, 1)
                app.addNamedButton("Python", "python", ButtonHandler, 0, 2)

            app.addHorizontalSeparator()

            app.addLabel("java_title", "Java")
            app.setLabelStyle("java_title", "Info.TLabel")
            app.getLabelWidget("java_title").config(font=title_font)
            with app.frame("frame12"):
                app.setPadding(10, 10)
                app.addImage("java_icon", "../Resources/Images/java logo.gif", 0, 0)
                app.zoomImage("java_icon", -5)
                app.addLabel("java_info", "The BlueJ Java IDE. Create Java applications.", 0, 1)
                app.addNamedButton("Java", "java", ButtonHandler, 0, 2)

            #app.addHorizontalSeparator()
            app.addLabel("filler2", "")

            
            # TODO: Add launchers + calls for ButtonHandler for Libreoffice
            app.addLabel("libreoffice_title", "LibreOffice: A free office suite")
            app.setLabelStyle("libreoffice_title", "H.TLabel")
            app.getLabelWidget("libreoffice_title").config(font=title_font)
            app.addHorizontalSeparator()

            app.addLabel("writer_title", "Writer")
            app.setLabelStyle("writer_title", "Info.TLabel")
            app.getLabelWidget("writer_title").config(font=title_font)
            with app.frame("frame13"):
                app.setPadding(10, 10)
                app.addImage("writer_icon", "../Resources/Images/writer.gif", 0, 0)
                #app.zoomImage("writer_icon", -2)
                app.addLabel("writer_info", "A simple, easy to use word processor.", 0, 1)
                app.addButton("Writer", ButtonHandler, 0, 2)

            app.addHorizontalSeparator()

            app.addLabel("calc_title", "Calc")
            app.setLabelStyle("calc_title", "Info.TLabel")
            app.getLabelWidget("calc_title").config(font=title_font)
            with app.frame("frame14"):
                app.setPadding(10, 10)
                app.addImage("calc_icon", "../Resources/Images/calc.gif", 0, 0)
                # app.zoomImage("writer_icon", -2)
                app.addLabel("calc_info", "Quickly make speadsheets and crunch numbers.", 0, 1)
                app.addButton("Calc", ButtonHandler, 0, 2)

            app.addHorizontalSeparator()

            app.addLabel("impress_title", "Impress")
            app.setLabelStyle("impress_title", "Info.TLabel")
            app.getLabelWidget("impress_title").config(font=title_font)
            with app.frame("frame15"):
                app.setPadding(10, 10)
                app.addImage("impress_icon", "../Resources/Images/impress.gif", 0, 0)
                # app.zoomImage("writer_icon", -2)
                app.addLabel("impress_info", "Create presentations!", 0, 1)
                app.addButton("Impress", ButtonHandler, 0, 2)

            app.addHorizontalSeparator()

            app.addLabel("draw_title", "Draw")
            app.setLabelStyle("draw_title", "Info.TLabel")
            app.getLabelWidget("draw_title").config(font=title_font)
            with app.frame("frame16"):
                app.setPadding(10, 10)
                app.addImage("draw_icon", "../Resources/Images/draw.gif", 0, 0)
                # app.zoomImage("writer_icon", -2)
                app.addLabel("draw_info", "Show off your art skills!", 0, 1)
                app.addButton("Draw", ButtonHandler, 0, 2)

            app.addHorizontalSeparator()

            app.addLabel("apps_more_info", "Want to look at more apps?\nGo to the Main Menu to see all of the apps installed on your Solar Pi.")
            app.setLabelStyle("apps_more_info", "H.TLabel")

        if solar_theme == True:
            app.setButtonStyle("tryit1", "H.TButton")
            #app.setButtonStyle("Settings", "H.TButton")
            #app.setButtonStyle("scratch", "H.TButton")
            #app.setButtonStyle("python", "H.TButton")
            #app.setButtonStyle("java", "H.TButton")
        
        """


    #     app.setSticky("nesw")
    #    # app.setBg("white")
    #     with app.scrollPane("scroll1"):
    #         app.setSticky("nesw")
    #         with app.frame("frame9"):
    #             #app.setBg("white")
    #             app.setSticky("nesw")
    #             app.addButton("Button", None)
    #             app.addMessage("m1", "jlkf;afd jfdkalf jkla;f jlk;afjkl;ajfkdlasf jkal; fjkadsl;f jkla;jklajkl;a kls akfl\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n;fjoiwejioruiowreu wqopuiqwopruiowqru oq[wruwioq[ruioq[ wru oq[wruoqwuro[iqruo[q uoq[urqow[ruoq")
    #     #app.setScrollPaneBg("scroll1", "white")

    ##################################
    #  Tab for Guides and Tutorials  #
    ##################################

    with app.note("Guides & Tutorials"):

        with app.labelFrame("Guides & Tutorials"):
            app.setSticky("nesw")
            app.setPadding(10, 10)
            app.addLabel("guides_info", "Hover over the icons to see more information about each resource.", 0, 0,
                         colspan=2)

            # RPi Foundation Python Tutorial
            with app.labelFrame("Python", colspan=2):
                app.setPadding(10, 10)
                app.setSticky("nesw")
                with app.frame("python intro", 0, 0):
                    app.setPadding(10, 10)
                    app.addImage("python2", "../Resources/Images/Python icon.gif", 0, 0)
                    app.zoomImage("python2", -4)
                    app.setImageTooltip("python2", "An introduction to Python, written by the Raspberry Pi Foundation")
                    app.addButton("Introduction to Python", PythonIntro, 0, 1)
                with app.frame("byte of python", 0, 1):
                    app.setPadding(10, 10)
                    app.addImage("python3", "../Resources/Images/Python icon.gif", 0, 0)
                    app.zoomImage("python3", -4)
                    app.setImageTooltip("python3", "A popular Ebook that teaches you Python")
                    app.addButton("A Byte of Python", ByteofPython, 0, 1)

            # Programming Glossary
            with app.labelFrame("Programming Glossary", 2, 0):
                app.setPadding(10, 10)
                app.addImage("programming_icon2", "../Resources/Images/Programming icon cropped.gif", 0, 0)
                app.zoomImage("programming_icon2", -10)
                app.setImageTooltip("programming_icon2",
                                    "Gives you definitions of words that you might not have heard before")
                app.addButton("Glossary", Glossary, 0, 1)

            # Google Python Tutorial
            with app.labelFrame("Java Guide", 2, 1):
                app.setPadding(10, 10)
                app.addImage("java_logo2", "../Resources/Images/java logo.gif", 0, 0)
                app.zoomImage("java_logo2", -5)
                app.setImageTooltip("java_logo2", "A guide on Java to help you get to know the basics of Java 8")
                app.addButton("Java Guide", Java, 0, 1)

        if solar_theme == True:
            app.setButtonStyle("Introduction to Python", "H.TButton")

    """

    with app.note("Guides & Tutorials"):

        with app.labelFrame("Guides & Tutorials"):
            app.setSticky("nesw")
            app.setPadding(10, 10)
            app.addLabel("guides_info", "Hover over the icons to see more information about each resource.", 0, 0, colspan=2)
            #    app.addImage("python", "../Resources/Images/Python icon.gif", 0, 1)
             #   app.zoomImage("python", -2)

            # RPi Foundation Python Tutorial
            with app.labelFrame("Introduction to Python", 1, 0):
                app.setPadding(10, 10)
                app.addImage("python2", "../Resources/Images/Python icon.gif", 0, 0)
                app.zoomImage("python2", -4)
                app.setImageTooltip("python2", "An introduction to Python, written by the Raspberry Pi Foundation")
                app.addButton("Python Intro", PythonIntro, 0, 1)

            # Programming Glossary
            with app.labelFrame("Programming Glossary", 1, 1):
                app.setPadding(10, 10)
                app.addImage("programming_icon2", "../Resources/Images/Programming icon cropped.gif", 0, 0)
                app.zoomImage("programming_icon2", -10)
                app.setImageTooltip("programming_icon2", "Gives you definitions of words that you might not have heard before")
                app.addButton("Glossary", Glossary, 0, 1)

            # A Byte of Python
            with app.labelFrame("A Byte of Python", 2, 0):
                app.setPadding(10, 10)
                app.addImage("python3", "../Resources/Images/Python icon.gif", 0, 0)
                app.zoomImage("python3", -4)
                app.setImageTooltip("python3", "A popular Ebook that teaches you Python")
                app.addButton("A Byte of Python", ByteofPython, 0, 1)

            # Google Python Tutorial
            with app.labelFrame("Java Guide", 2, 1):
                app.setPadding(10, 10)
                app.addImage("java_logo2", "../Resources/Images/java logo.gif", 0, 0)
                app.zoomImage("java_logo2", -5)
                app.setImageTooltip("java_logo2", "A guide on Java to help you get to know the basics of Java 8")
                app.addButton("Java Guide", Java, 0, 1)


        if solar_theme == True:
            app.setButtonStyle("Python Intro", "H.TButton")
        
        """

    #########################
    #  Tab for System Info  #
    #########################

    with app.note("System Info"):
        try:
            call("uname -r > \"../Solar Pi Welcome/sysinfo\"")
            call("df -h --output=size,used,avail,pcent >> \"../Solar Pi Welcome/sysinfo\"")
            call("cat /etc/*release* > \"../Solar Pi Welcome/osinfo\"")
        except FileNotFoundError:
            print("Running under Windows! ...or another machine that isn't a Solar Pi")

        with open("osinfo", "r") as file:
            data = file.readlines()
        for line in data:
            if line.startswith("DISTRIB_DESCRIPTION="):
                os_v = line.split("=")[1]
                os_v = os_v.lstrip("\"")
                os_v = os_v.rstrip("\"\n")
                break
        with open("sysinfo", "r") as file:
            data = file.readlines()
        kernel_v = data[0].rstrip("\n")
        disk_data = data[2].split()
        total_disk = disk_data[0] + "B"
        used_disk = disk_data[1] + "B"
        avail_disk = disk_data[2] + "B"
        pcent_disk_used = int(disk_data[3].rstrip("%"))
        pcent_disk_avail = 100 - pcent_disk_used

        bold_font = ("ubuntu", 12, "bold")

        with app.labelFrame("Raspberry Pi Info"):
            app.setPadding(10, 5)
            app.addLabel("rpi_model", "Raspberry Pi Model:", 0, 0)
            app.getLabelWidget("rpi_model").config(font=bold_font)
            app.addLabel("rpi_model_value", "Raspberry Pi 3 Model B", 0, 1)

            app.addLabel("soc", "SoC:", 0, 2)
            app.getLabelWidget("soc").config(font=bold_font)
            app.addLabel("soc_value", "Broadcom BCM2837", 0, 3)

            app.addLabel("cpu", "CPU:", 1, 0)
            app.getLabelWidget("cpu").config(font=bold_font)
            app.addLabel("cpu_value", "4 x ARM Cortex A53, 1.2GHz", 1, 1)

            app.addLabel("ram", "RAM:", 1, 2)
            app.getLabelWidget("ram").config(font=bold_font)
            app.addLabel("ram_value", "LPDDR2 1.0GB", 1, 3)

        with app.labelFrame("OS Info"):
            app.setPadding(10, 5)
            app.addLabel("os_version", "Operating System:", 0, 0)
            app.getLabelWidget("os_version").config(font=bold_font)
            app.addLabel("os_version_value", os_v, 0, 1)

            app.addLabel("kernel_version", "Kernel Version:", 0, 2)
            app.getLabelWidget("kernel_version").config(font=bold_font)
            app.addLabel("kernel_version_value", kernel_v, 0, 3)

        with app.labelFrame("Disk Info"):
            app.setPadding(10, 5)
            app.addLabel("total_disk", "Total Disk Space:", 0, 0)
            app.getLabelWidget("total_disk").config(font=bold_font)
            app.addLabel("total_disk_value", total_disk, 0, 1)

            app.addLabel("used_disk", "Used Disk Space:", 0, 2)
            app.getLabelWidget("used_disk").config(font=bold_font)
            app.addLabel("used_disk_value", used_disk, 0, 3)

            app.addLabel("avail_disk", "Free Disk Space:", 0, 4)
            app.getLabelWidget("avail_disk").config(font=bold_font)
            app.addLabel("avail_disk_value", avail_disk, 0, 5)

            with app.frame("frame22", 1, 0, colspan=2):
                app.setPadding(5, 1)
                app.addMeter("disk_usage", 0, 0)
                app.setMeter("disk_usage", pcent_disk_used)
                if pcent_disk_used < 85:
                    app.setMeterFill("disk_usage", "#687396")
                else:
                    app.setMeterFill("disk_usage", "red")
                app.setMeterSticky("disk_usage", "ew")
                app.setMeterTooltip("disk_usage", "Used: " + used_disk + "\nFree: " + avail_disk)
                app.addLabel("disk_label", avail_disk + " free of " + total_disk, 1, 0)
            app.setFrameSticky("frame22", "ew")
            #app.addPieChart("disk_chart", {"Available": pcent_disk_avail, "Used": pcent_disk_used}, 0, 1, rowspan=3)


def Startup(param):
    value = app.getCheckBox("Launch at startup")
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

app.setPadding(5, 5)
app.addCheckBox("Launch at startup", 1, 0)
app.setCheckBox("Launch at startup", ticked=LaunchWelcome())
app.setCheckBoxChangeFunction("Launch at startup", Startup)


# num = 0
# def updateMeter():
#     global num
#     app.setMeter("battery", num)
#     #app.setLabel("level", str(num)+"%")
#     num += 1
# with app.frame("battery", 1, 1):
#     app.addLabel("battery", "Battery Remaining: ", 0, 0)  # Update translation
#     #app.setLabelAlign("battery", "right")
#     app.setLabelAnchor("battery", "e")
#     app.addMeter("battery", 0, 2)
#     app.setMeterFill("battery", "#13d323")
#     app.addLabel("blank", "", 0, 3)
#     #app.setMeterPadding("battery", 5, 5)
#     app.registerEvent(updateMeter)
#     app.setPollTime(10000)


with open("language.txt", "r") as file:
    lang = file.readline()
    lang.rstrip("\n")

#print(lang)
#app.setLabelFrameStyle("-", "TFrame")
#app.setLabelFrameStyle("", "TFrame")
#app.ttkStyle.configure(".", background="white", foreground="black")

if solar_theme == False:
    ##app.ttkStyle.configure("TLabelframe", background="white")

    app.setLabelFrameStyle("Applications", "TFrame")
    app.setLabelFrameStyle("Start Programming", "TFrame")
    app.setLabelFrameStyle("Solar Pi Settings", "TFrame")
    app.setLabelFrameStyle("IDEs", "TFrame")
    app.setLabelFrameStyle("Scratch", "TFrame")
    app.setLabelFrameStyle("Python", "TFrame")
    app.setLabelFrameStyle("Java", "TFrame")
    app.setLabelFrameStyle("Guides & Tutorials", "TFrame")
    app.setLabelFrameStyle("Introduction to Python", "TFrame")
    app.setLabelFrameStyle("Programming Glossary", "TFrame")
    app.setLabelFrameStyle("A Byte of Python", "TFrame")
    app.setLabelFrameStyle("Java Guide", "TFrame")
    app.setLabelFrameStyle("About", "TFrame")
    app.setLabelFrameStyle("Raspberry Pi Info", "TFrame")
    app.setLabelFrameStyle("OS Info", "TFrame")
    app.setLabelFrameStyle("Disk Info", "TFrame")

if theme1 != "black":
    app.setBg("white")

#print(app.ttkStyle.lookup("TFrame", "bordercolor"))

app.go(language=lang)
