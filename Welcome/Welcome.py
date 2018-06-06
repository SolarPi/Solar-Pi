#!/usr/bin/env python3
# Solar Pi Welcome

from appJar import gui
from subprocess import Popen, call
from sys import exit
import webbrowser
from AutorunConfig import Autorun
from SettingsRW import *
from PIL import Image, ImageTk
from time import sleep
from threading import Thread

theme1 = getSetting("theme")
startup1 = getSetting("welcome")

try:
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler

    class Watcher:
        DIRECTORY_TO_WATCH = "/usr/local/bin/Solar Pi/Settings"  # Looks at settings

        def __init__(self):
            self.observer = Observer()

        def run(self):
            event_handler = Handler()
            self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
            self.observer.start()
            try:
                while True:
                    sleep(5)
            except:
                self.observer.stop()
                print("Error")

            self.observer.join()


    class Handler(FileSystemEventHandler):

        @staticmethod
        def on_any_event(event):
            if event.is_directory:
                return None

            elif event.event_type == 'created':
                # Take any action here when a file is first created.
                print("Received created event")  # Triggered when a file is created

            elif event.event_type == 'modified':
                # Taken any action here when a file is modified.
                print("Received modified event")
                settings()  # Calls meter() when file is modified

except:
    pass

def settings(first=False):
    global theme1, startup1, msgBg, msgFg, title_font, bold_font
    theme2 = getSetting("theme")
    startup2 = getSetting("welcome")

    if theme1 != theme2 or first == True:
        if theme2 == "Solar Pi":
            msgFg = "black"
            msgBg = "white"

            app.setTtkTheme("plastik")
            app.setTtkTheme("clam")
            # app.ttkStyle.configure(".", font="10")

            # Custom Notebook
            app.ttkStyle.configure("TNotebook", background="white", bordercolor="#687396")
            app.ttkStyle.map("TNotebook.Tab", background=[("selected", "#76a928")],  # Selected tab
                             foreground=[("selected", "white")], padding=[("selected", "0.125cm")])
            app.ttkStyle.configure("TNotebook.Tab", background="#dbdce2", foreground="black", bordercolor="#687396",
                                   padding="0.095cm")  # Unselected tab
            # "#dbdce2"
            # Custom buttons

            # Highlighted button
            app.ttkStyle.configure("H.TButton", background="#324581", foreground="white", bordercolor="#687396")
            app.ttkStyle.map("H.TButton", background=[("pressed", "#172141"), ("active", "#4059a9")])

            app.ttkStyle.configure("Back.TButtton", background="#687396", bordercolor="#687396")
            app.ttkStyle.map("Back.TButton",
                             background=[("pressed", "#687396"), ("active", "#687396"), ("!pressed", "#687396"),
                                         ("!active", "#687396")])

            app.ttkStyle.map("TCheckbutton", background=[("active", "white")])

            # Regular button
            app.ttkStyle.configure("TButton", background="#dbdce2", bordercolor="#687396")

            app.ttkStyle.map("TLabelFrame", border=[("active", "black")])

            app.ttkStyle.configure("TLabelframe", bordercolor="#687396")


            # Buttons
            app.setButtonStyle("coding2", "H.TButton")
            app.setButtonStyle("Close", "H.TButton")
            app.setButtonStyle("Get Started", "H.TButton")
            app.setButtonStyle("Read More", "H.TButton")
            
        else:
            app.setTtkTheme(theme2)
            msgFg = "white"
            msgBg = "#424242"
            if theme2 != "black":
                app.ttkStyle.configure(".", foreground="black", background="white")
                app.ttkStyle.map("TCheckbutton", background=[("active", "white")])
                app.ttkStyle.map("TRadiobutton", background=[("active", "white")])
                app.setBg("white")
                msgFg = "black"
                msgBg = "white"

            app.setLabelFrameStyle("Applications", "TFrame")
            app.setLabelFrameStyle("Guides & Tutorials", "TFrame")
            app.setLabelFrameStyle("About", "TFrame")
            app.setLabelFrameStyle("Solar Pi Info", "TFrame")
            app.setLabelFrameStyle("OS Info", "TFrame")
            app.setLabelFrameStyle("Disk Info", "TFrame")

        if theme2 == "Solar Pi" or theme2 == "black":
            app.showButton("Get Started")
            app.hideButton("get started")
        else:
            app.showButton("get started")
            app.hideButton("Get Started")

        if theme2 != "black":
            app.setBg("white")

        app.setFont(family="piboto")
        app.ttkStyle.configure(".", font=("piboto"))

        title_font = ("piboto", 14, "normal")
        bold_font = ("piboto", 12, "bold")

        app.setFont(family="piboto")
        app.ttkStyle.configure(".", font=("piboto"))

        app.ttkStyle.configure("H.TLabel", background="#687396", foreground="white",
                               padding=[10, 10])  # #dbdce2, #687396
        app.ttkStyle.configure("Padding.TLabel", padding=[10, 7])

        app.ttkStyle.configure("back.TLabel", background="#687396", padding=[7, 6], borderwidth=1)
        # app.ttkStyle.map("back.TLabel", relief=[("!active", "raised")]) #bordercolor=[("active", "white")],

        app.ttkStyle.configure("Info.TLabel", padding=[10, 10])

    if startup1 != startup2:
        app.setCheckBox("Launch at startup", ticked=startup2, callFunction=False)

    theme1 = theme2
    startup1 = startup2


app = gui("Solar Pi Welcome", useTtk=True)
app.setResizable(False)

msgFg = "black"
msgBg = "white"

title_font = ("piboto", 14, "normal")
bold_font = ("piboto", 12, "bold")

# Event Handler for buttons
def ButtonHandler(press):
    press = press.lower()

    if press == "Exit" or press == "Exit3" or press == "Exit2" or press == "Exit4":  # Exits program
        exit()  # Quits program
    elif press == " about": app.showSubWindow("About Solar Pi")  # Opens the About subwindow
    elif press == "close": app.hideSubWindow("About Solar Pi")  # Closes the About subwindow
    elif press == "libreoffice_close": app.hideSubWindow("Libreoffice")

    elif press == "change advanced settings": Popen("/usr/bin/rc_gui")  # Launches RPi settings window
    elif press == "  languages": Popen("../Resources/Launchers/language_launcher.sh")  # Launches settings for display language
    elif press == "file manager": Popen("../Resources/Launchers/pcmanfm Launcher.sh")

    elif press == "get started": app.getNotebookWidget("MainTabs").select([1])  # Sets selected note/tab to Get Started
    elif press == "charging": app.getNotebookWidget("MainTabs").select([2])  # Set selected note/tab to Charging
    else:
        Popen("../Resources/Launchers/" + press + " launcher.sh")


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
    Popen("../Resources/Launchers/Start Coding.sh")
def PythonGuides(press):
    Popen("../Resources/Launchers/Python Guide Launcher.sh")

def Settings(press):
    Popen("../Resources/Launchers/Settings Launcher.sh")

def Libreoffice(press):
    if press == "Libreoffice":
        app.showSubWindow("Libreoffice")
    else:
        Popen("../Resources/Launchers/" + press + " launcher.sh")

def Terminal(press): # Terminal
    Popen("../Resources/Launchers/terminal.sh")

def Docs(press):
    webbrowser.get("chromium-browser").open("http://localhost/")  # Launch guides here

def PythonIntro(press):  # RPi Python Introduction
    webbrowser.get("chromium-browser").open("http://localhost/Advanced-Things/python/index.html")
def Glossary(press):  # Programming Glossary
    webbrowser.get("chromium-browser").open("http://localhost/Advanced-Things/programming-glossary/index.html")
def ByteofPython(press):  # Byte of Python
    webbrowser.get("chromium-browser").open("http://localhost:81/")
def Java(press):  # Google's Python Tutorial
    webbrowser.get("chromium-browser").open("http://localhost:82/java/index.htm")

#app.setFont(11, font="Dejavu Sans")

# About Popup
with app.subWindow("About Solar Pi", modal=True):
    app.setResizable(canResize=False)
    with app.frame("frame7"):  # Rename to frame6 to remove right hand button column on Welcome tab
        app.setPadding(10, 10)
        app.addImage("solar_pi_logo", "../Resources/Images/Solar Pi logo.gif")
        app.zoomImage("solar_pi_logo", -3)
        with app.labelFrame("About"):
            app.setPadding(10, 10)
            app.addLabel("about", "Solar Pi is a charity project, aimed at getting\nRaspberry Pi based, solar powered computers\nto those who need it most.\n\nEnjoy!")
        app.addButton("Close", ButtonHandler)
        app.setButtonSticky("Close", "")

# Main Window
app.setPadding(3, 3)

tools = ["Off", "Settings", "Files", "About", "Help"]
app.addToolbar(tools, ToolbarHandler, findIcon=True)


with app.notebook("MainTabs", colspan=2):
    with app.note("Welcome!"):
        app.setPadding(10, 10)
        with app.frame("frame4", 0, 0, colspan=3):
            app.addLabel("text4", "Welcome to your  ", 0, 0)
            app.setLabelAlign("text4", "right")
            app.getLabelWidget("text4").config(font=("piboto", "20"))
            app.addImage("logo text1", "../Resources/Images/Solar Pi text small.gif", 0, 1)
            app.setImageSticky("logo text1", "nsw")

        with app.frame("frame5", 1, 0):
            app.setPadding(10, 10)

            app.addNamedButton("Get Started", "Get Started", ButtonHandler, 1, 0)
            app.setButtonImage("Get Started", "../Resources/Images/md-play.gif", align="left")
            app.setButtonSticky("Get Started", "nesw")

            app.addNamedButton("Get Started", "get started", ButtonHandler, 1, 0)
            app.setButtonImage("get started", "../Resources/Images/md-play black.gif", align="left")
            app.setButtonSticky("get started", "nesw")

            if theme1 == "Solar Pi" or theme1 == "black":
                app.hideButton("get started")
            else:
                app.hideButton("Get Started")

            app.addImageButton(" Docs", Docs, "../Resources/Images/docs icon.gif", align="left", row=2, column=0)
            app.setButtonSticky(" Docs", "nesw")
            app.addIconButton(" About", ButtonHandler, "about", align="left", row=3, column=0)
            app.setButtonSticky(" About", "nesw")


        ###########################
        #     Animation Stuff     #
        ###########################

        canvas = app.addCanvas("c", 1, 1, rowspan=3)  # Create canvas

        if theme1 == "black":  # Configure options for black theme
            app.setCanvasBg("c", "#424242")
            img = Image.open("../Resources/Images/blackLogo.png")
            canvas.config(bd=0, highlightthickness=0, width=130, height=130)
            pos = 103  # 90
        elif getSetting("theme") == "Solar Pi":  # Configure options for Solar Pi theme
            app.setCanvasBg("c", "white")
            img = Image.open("../Resources/Images/whiteLogo2.png")
            canvas.config(bd=0, highlightthickness=0, width=150, height=150)
            pos = 110  # 100

        else:
            app.setCanvasBg("c", "white")  # Configure options for all other themes
            img = Image.open("../Resources/Images/whiteLogo.png")
            canvas.config(bd=0, highlightthickness=0, width=130, height=130)
            pos = 103  # 90

        images = []  # Create image cache
        img.putalpha(0)  # Make first image transparent
        images.append(app.addCanvasImage("c", pos, pos, ImageTk.PhotoImage(img)))  # Add to cache

        def fade():
            global images, img, canvas, stop
            image_cache = []
            failed = True
            while failed == True:  # Sometimes, Python will decide throw errors (eg. in IDLE on Pi)... so this fixes it :)
                try:
                    for i in range(0, 256, 8):  # Generate all 32 frames
                        img.putalpha(i)  # Adjust alpha of each frame
                        image_cache.append(ImageTk.PhotoImage(img))  # Add each frame to list
                    sleep(0.75)  # Pause so animation starts just after application launch
                    failed = False
                except Exception:
                    print("Animation failed :(")
            
            while True:
                images.append(app.addCanvasImage("c", pos, pos, image_cache[0]))  # Put each frame on canvas, then append to cache

                for image in image_cache:  # Iterate over canvas images
                    images.append(app.addCanvasImage("c", pos, pos, image))  # Display image, then add to temporary list
                    canvas.delete(images.pop(0))  # Delete image behind (1st image in list)
                    sleep(0.03333)  # Pause 0.45

                sleep(15)  # Show logo in full

                for image in reversed(image_cache):  # Iterate over canvas images again but in reverse to fade out
                    images.append(app.addCanvasImage("c", pos, pos, image))
                    canvas.delete(images.pop(0))
                    sleep(0.03333)  # 0.45

                images = []  # Clean temporary list

                sleep(0.25)  # Pause before fading back in

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


    with app.note("Get Started"):
        
        def guide(btn):
            if btn.lower() == "back":
                app.getFrameWidget("options").lift()
            else:
                app.getFrameWidget(btn).lift()

        with app.frame("options", 0, 0, sticky="new"):

            with app.frame("starter", 0, 0):
                app.setSticky("nwe")
                with app.frame("starter2"):
                    app.setPadding(5, 2)
                    app.addLabel("starter_options_title", "Solar Pi Starter Guide")
                    app.getLabelWidget("starter_options_title").config(font=title_font)
                    app.setLabelStyle("starter_options_title", "Padding.TLabel")
                    app.addHorizontalSeparator()

                with app.frame("starter3"):
                    app.setPadding(2, 10)
                    app.addImage("starter_icon", "../Resources/Images/Solar Pi logo icon.gif")

                with app.frame("starter4"):
                    app.setPadding(5, 10)
                    app.addButton("Starter Guide", guide)
                    app.setButtonSticky("Starter Guide", "")
                    app.setButtonStyle("Starter Guide", "H.TButton")
                    app.addMessage("starter_sum", "Click or tap to read a quick overview on how to use your Solar Pi.")
                    app.setMessageWidth("starter_sum", 225)
                    app.setMessageSticky("starter_sum", "ew")
                    app.setMessageFg("starter_sum", msgFg)
                    app.setMessageBg("starter_sum", msgBg)

            with app.frame("charging", 0, 1):
                app.setSticky("nwe")
                with app.frame("charging2"):
                    app.setPadding(5, 2)
                    app.addLabel("charging_title2", "Charging")
                    app.getLabelWidget("charging_title2").config(font=title_font)
                    app.setLabelStyle("charging_title2", "Padding.TLabel")
                    app.addHorizontalSeparator()

                with app.frame("charging3"):
                    app.setPadding(2, 23)
                    app.addImage("charge_icon", "../Resources/Images/battery-charging.gif")

                with app.frame("charging4"):
                    app.setPadding(5, 10)
                    app.addButton("Charging", guide)
                    app.setButtonSticky("Charging", "")
                    app.addMessage("charging_sum", "Click or tap to read how to charge your Solar Pi.")
                    app.setMessageWidth("charging_sum", 225)
                    app.setMessageSticky("charging_sum", "ew")
                    app.setMessageFg("charging_sum", msgFg)
                    app.setMessageBg("charging_sum", msgBg)

            with app.frame("coding", 0, 2):
                app.setSticky("nwe")
                with app.frame("coding2"):
                    app.setPadding(5, 2)
                    app.addLabel("coding_title2", "Coding")
                    app.getLabelWidget("coding_title2").config(font=title_font)
                    app.setLabelStyle("coding_title2", "Padding.TLabel")
                    app.addHorizontalSeparator()

                with app.frame("coding3"):
                    app.setPadding(2, 28)
                    app.addImage("coding_icon2", "../Resources/Images/coding icon small.gif")

                with app.frame("coding4"):
                    app.setPadding(5, 10)
                    app.addButton("Coding", guide)
                    app.setButtonSticky("Coding", "")
                    app.addMessage("coding_sum2", "Click or tap to learn more about coding on your Solar Pi.")
                    app.setMessageWidth("coding_sum2", 225)
                    app.setMessageSticky("coding_sum2", "ew")
                    app.setMessageFg("coding_sum2", msgFg)
                    app.setMessageBg("coding_sum2", msgBg)


        with app.frame("Starter Guide", 0, 0, sticky="new"):
            app.addLabel("basics_title", "          The Basics", 0, 0)  # 2 tabs + 2 spaces or 10 spaces
            app.getLabelWidget("basics_title").config(font=title_font)
            app.setLabelStyle("basics_title", "H.TLabel")

            ##687396

            app.addImage("back", "../Resources/Images/white back arrow.gif", 0, 0)
            app.setImageStyle("back", "back.TLabel")
            app.setImageSticky("back", "nw")
            app.setImageSubmitFunction("back", guide)

            with app.frame("frame19"):
                app.setPadding(10, 10)

                starter_info = """Your Solar Pi has a touchscreen. This means that you can use your finger to touch the screen and control the computer.

•  The image on the right is of the Solar Pi desktop.
•  There is a bar at the top, showing you what windows are open.
•  At the top left, there is a button to open a menu. From here, you can see and run all of the applications that are installed on your Solar Pi."""
                app.addMessage("basics_info", starter_info, 0, 0, rowspan=2)
                app.setMessageWidth("basics_info", 375)
                app.setMessageBg("basics_info", msgBg)
                app.setMessageFg("basics_info", msgFg)
                app.setMessageSticky("basics_info", "nesw")

                app.addImage("desktop", "../Resources/Images/Desktop small.gif", 0, 1)

                app.addButton("Read More", Docs, 1, 1)
                app.setButtonSticky("Read More", "n")


        with app.frame("Charging", 0, 0, sticky="new"):
            app.addLabel("charging_title", "          Charging Your Solar Pi", 0, 0)
            app.setLabelStyle("charging_title", "H.TLabel")
            app.getLabelWidget("charging_title").config(font=title_font)

            #app.addImageButton("Back", guide,"../Resources/Images/white back arrow.gif", 0, 0, align="none")
            #app.setButtonStyle("Back", "Back.TButton")
            #app.setButtonSticky("Back", "nw")

            app.addImage("Back", "../Resources/Images/white back arrow.gif", 0, 0)
            app.setImageStyle("Back", "back.TLabel")
            app.setImageSticky("Back", "nw")
            app.setImageSubmitFunction("Back", guide)

            with app.frame("frame20"):
                app.setPadding(10, 10)
                app.setStretch("columns")

                charge_info = """There is a battery meter at the bottom left corner of the display. This tells you how much power is left in the batteries.

•  When the battery gets low, you need to charge your Solar Pi. To do this, fold out the solar panels and face them to the sun.
•  You will know if the batteries are charging, as the meter will show the charging animation.
•  The batteries are fully charged when the bar is completely green."""

                app.addMessage("charge_info", charge_info)
                app.setMessageWidth("charge_info", 375)
                app.setMessageBg("charge_info", msgBg)
                app.setMessageFg("charge_info", msgFg)
                app.setMessageSticky("charge_info", "nsw")

                with app.frame("images", 0, 1):
                    app.addImage("low charge", "../Resources/Images/low battery small.gif", 0, 0)
                    app.addLabel("low charge", "Low Charge", 0, 1)

                    app.addImage("charging", "../Resources/Images/charging small.gif", 1, 0)
                    app.addLabel("charging", "Charging - you will\nsee this with an animation", 1, 1)

                    app.addImage("full charge", "../Resources/Images/full battery small.gif", 2, 0)
                    app.addLabel("full charge", "Full Charge", 2, 1)

        with app.frame("Coding", 0, 0, sticky="new"):
            app.addLabel("coding_title3", "          Coding With Your Solar Pi", 0, 0)  # 2 tabs + 2 spaces or 10 spaces
            app.getLabelWidget("coding_title3").config(font=title_font)
            app.setLabelStyle("coding_title3", "H.TLabel")

            app.addImage("BACK", "../Resources/Images/white back arrow.gif", 0, 0)
            app.setImageStyle("BACK", "back.TLabel")
            app.setImageSticky("BACK", "nw")
            app.setImageSubmitFunction("BACK", guide)

            with app.frame("coding5"):
                app.setPadding(10, 10)

                coding_info = """Your Solar Pi can let you code to create fun programs and games. You'll need to think logically to break down a problem into smaller steps, then tell the computer what it needs to do to solve the problem.

There are 3 different programming languages you can use on the Solar Pi - Scratch, Python and Java.
Learning these languages will give you valuable skills that could help you in the future, and it's also great fun!

Happy coding!"""
                app.addMessage("coding_info", coding_info, 0, 0)
                app.setMessageWidth("coding_info", 375)
                app.setMessageBg("coding_info", msgBg)
                app.setMessageFg("coding_info", msgFg)
                app.setMessageSticky("coding_info", "nsw")

                with app.frame("coding_img_btn", 0, 1):
                    app.setPadding(2, 3)
                    app.addImage("code", "../Resources/Images/code.gif", 0, 1)
                    app.setImageSticky("code", "w")
                    app.addNamedButton("Start Coding", "coding2", Programming, 1, 1)
                    app.setButtonSticky("coding2", "n")

        app.getFrameWidget("options").lift()

    ##########################
    #  Tab for Applications  #
    ##########################

    with app.note("Applications"):

        pages = [" Start Coding", " File Manager", " Solar Pi Settings", " LibreOffice", " Terminal"]  # Sets settings pages

        def change(listName):
            app.getFrameWidget(app.listBox("list")[0]).lift()

        with app.labelFrame("Applications", sticky="nws", stretch="none", padding=[10, 10]):  # Create LabelFrame
            lb = app.listBox("list", pages, change=change,
                             activestyle="none", selectbackground="#687396", selectforeground="white",
                             selectmode=app.SINGLE,
                             relief=app.FLAT)  # Create ListBox # selectborderwidth=5, relief=app.FLAT, selectrelief=app.FLAT
            app.configure(sticky="news", stretch="both")
            app.getListBoxWidget("list").config(font=title_font)

            with app.frame(pages[0], 0, 1, sticky="new"):  # Create frame for each page

                with app.frame("coding_title", colspan=2):
                    app.addLabel("coding_title", "Start Coding")
                    app.getLabelWidget("coding_title").config(font=title_font)
                    app.addImage("coding_icon", "../Resources/Images/coding icon small.gif", 0, 1)
                    app.zoomImage("coding_icon", -2)
                    app.addHorizontalSeparator(colspan=2)

                app.addImage("coding_image", "../Resources/Images/startcoding.gif", 1, 0, rowspan=2)

                with app.frame("coding_content", 1, 1):
                    app.setPadding(7, 7)
                    app.addMessage("coding_sum", "This allows you to see and try the different options for coding.")
                    app.setMessageWidth("coding_sum", 175)
                    app.setMessageFg("coding_sum", msgFg)
                    app.setMessageBg("coding_sum", msgBg)
                    app.addLabel("spacer1", "")
                    app.addButton("Start Coding", Programming)

            with app.frame(pages[1], 0, 1, sticky="new"):  # Create frame for each page

                with app.frame("file_title", colspan=2):
                    app.addLabel("file_title", "File Manager")
                    app.getLabelWidget("file_title").config(font=title_font)
                    app.addImage("file_title", "../Resources/Images/file manager.gif", 0, 1)
                    app.addHorizontalSeparator(colspan=2)

                app.addImage("file_image", "../Resources/Images/pcmanfm.gif", 1, 0, rowspan=2)

                with app.frame("file_content", 1, 1):
                    app.setPadding(7, 7)
                    app.addMessage("file_sum", "Also known as PCmanFM, this allows you to view and manage your files.")
                    app.setMessageWidth("file_sum", 175)
                    app.setMessageFg("file_sum", msgFg)
                    app.setMessageBg("file_sum", msgBg)
                    app.addLabel("spacer3", "")
                    app.addButton("File Manager", ButtonHandler)

            with app.frame(pages[2], 0, 1, sticky="new"):  # Create frame for each page

                with app.frame("settings_title", colspan=2):
                    app.addLabel("settings_title", "Solar Pi Settings")
                    app.getLabelWidget("settings_title").config(font=title_font)
                    app.addImage("settings_icon", "../Resources/Images/settings icon small 2.gif", 0, 1)
                    app.addHorizontalSeparator(colspan=2)

                app.addImage("settings_image", "../Resources/Images/perfpower.gif", 1, 0, rowspan=2)

                with app.frame("settings_content", 1, 1):
                    app.setPadding(7, 7)
                    app.addMessage("settings_sum", "This allows you to change the settings for your Solar Pi.")
                    app.setMessageWidth("settings_sum", 175)
                    app.setMessageFg("settings_sum", msgFg)
                    app.setMessageBg("settings_sum", msgBg)
                    app.addLabel("spacer2", "")
                    app.addButton("Settings", Settings)

            with app.frame(pages[3], 0, 1, sticky="new"):  # Create frame for each page

                with app.frame("libreoffice_title", colspan=2):
                    app.addLabel("libreoffice_title", "LibreOffice")
                    app.getLabelWidget("libreoffice_title").config(font=title_font)
                    app.addImage("libreoffice_icon", "../Resources/Images/libreoffice.gif", 0, 1)
                    app.addHorizontalSeparator(colspan=2)

                app.addMessage("libreoffice_sum", "Hover over the icons to see more information.")
                app.setMessageWidth("libreoffice_sum", 525)
                app.setMessageFg("libreoffice_sum", msgFg)
                app.setMessageBg("libreoffice_sum", msgBg)
                with app.frame("libreoffice"):
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

            with app.frame(pages[4], 0, 1, sticky="new"):  # Create frame for each page

                with app.frame("term_title", colspan=2):
                    app.addLabel("term_title", "Terminal")
                    app.getLabelWidget("term_title").config(font=title_font)
                    app.addImage("term_icon", "../Resources/Images/coding icon small.gif", 0, 1)
                    app.zoomImage("term_icon", -2)
                    app.addHorizontalSeparator(colspan=2)

                app.addImage("term_image", "../Resources/Images/terminal.gif", 1, 0, rowspan=2)

                with app.frame("term_content", 1, 1):
                    app.setPadding(7, 7)
                    app.addMessage("term_sum", "The Terminal is a powerful tool that can be used to do most things on your Solar Pi.")
                    app.setMessageWidth("term_sum", 175)
                    app.setMessageFg("term_sum", msgFg)
                    app.setMessageBg("term_sum", msgBg)
                    app.addLabel("Spacer3", "")
                    app.addButton("Terminal", Terminal)


    ##################################
    #  Tab for Guides and Tutorials  #
    ##################################

    with app.note("Guides & Tutorials"):
        pages2 = [" Python Introduction", " A Byte of Python", " Programming Glossary", " Java Guide"]  # Sets settings pages

        def change2(listName):
            app.getFrameWidget(app.listBox("list2")[0]).lift()

        with app.labelFrame("Guides & Tutorials", sticky="nws", stretch="none", padding=[10, 10]):  # Create LabelFrame
            lb2 = app.listBox("list2", pages2, change=change2,
                             activestyle="none", selectbackground="#687396", selectforeground="white",
                             selectmode=app.SINGLE,
                             relief=app.FLAT)  # Create ListBox # selectborderwidth=5, relief=app.FLAT, selectrelief=app.FLAT
            app.configure(sticky="news", stretch="both")
            app.getListBoxWidget("list2").config(font=title_font)

            with app.frame(pages2[0], 0, 1, sticky="new"):  # Create frame for each page
                with app.frame("intro_title", colspan=2):
                    app.addLabel("intro_title", "Python Introduction")
                    app.getLabelWidget("intro_title").config(font=title_font)
                    app.addImage("intro_icon", "../Resources/Images/Python icon small.gif", 0, 1)
                    app.addHorizontalSeparator(colspan=2)

                app.addImage("intro_image", "../Resources/Images/python hello world.gif", 1, 0)

                with app.frame("intro_content", 2, 0):
                    app.setPadding(5, 5)
                    app.addMessage("intro_sum", "An introduction to Python written by the Raspberry Pi Foundation.", 0, 0)
                    app.setMessageWidth("intro_sum", 500)
                    app.setMessageFg("intro_sum", msgFg)
                    app.setMessageBg("intro_sum", msgBg)
                    app.addLabel("spacer4", "")


                    app.addButton("Go!", PythonIntro, 1, 0)
                    app.setButtonSticky("Go!", "")

            with app.frame(pages2[1], 0, 1, sticky="new"):  # Create frame for each page
                with app.frame("byte_title", colspan=2):
                    app.addLabel("byte_title", "A Byte of Python")
                    app.getLabelWidget("byte_title").config(font=title_font)
                    app.addImage("byte_icon", "../Resources/Images/Python icon small.gif", 0, 1)
                    app.addHorizontalSeparator(colspan=2)

                app.addImage("byte_image", "../Resources/Images/Python icon.gif", 1, 0)

                with app.frame("byte_content", 2, 0):
                    app.setPadding(5, 5)
                    app.addMessage("byte_content", "A popular Ebook that will help you with coding in Python.", 0, 0)
                    app.setMessageWidth("byte_content", 500)
                    app.setMessageFg("byte_content", msgFg)
                    app.setMessageBg("byte_content", msgBg)
                    app.addLabel("spacer5", "")

                    app.addButton("More Python!", ByteofPython, 1, 0)
                    app.setButtonSticky("More Python!", "")

            with app.frame(pages2[2], 0, 1, sticky="new"):  # Create frame for each page

                with app.frame("glossary_title", colspan=2):
                    app.addLabel("glossary_title", "Programming Glossary")
                    app.getLabelWidget("glossary_title").config(font=title_font)
                    app.addImage("glossary_icon", "../Resources/Images/docs icon.gif", 0, 1)
                    app.addHorizontalSeparator(colspan=2)

                app.addImage("glossary_image", "../Resources/Images/glossary.gif", 1, 0, rowspan=2)

                with app.frame("glossary_content", 1, 1):
                    app.setPadding(7, 7)
                    app.addMessage("glossary_sum", "Gives you definitions of words that you might not have heard before.")
                    app.setMessageWidth("glossary_sum", 175)
                    app.setMessageFg("glossary_sum", msgFg)
                    app.setMessageBg("glossary_sum", msgBg)
                    app.addLabel("spacer6", "")
                    app.addButton("Glossary", Glossary)

            with app.frame(pages2[3], 0, 1, sticky="new"):  # Create frame for each page

                with app.frame("java_title", colspan=2):
                    app.addLabel("java_title", "Java Guide")
                    app.getLabelWidget("java_title").config(font=title_font)
                    app.addImage("java_icon", "../Resources/Images/java logo small.gif", 0, 1)
                    app.addHorizontalSeparator(colspan=2)

                app.addImage("java_image", "../Resources/Images/java guide.gif", 1, 0, rowspan=2)

                with app.frame("java_content", 1, 1):
                    app.setPadding(7, 7)
                    app.addMessage("java_sum", "A guide to help you get to know the basics of coding in Java.")
                    app.setMessageWidth("java_sum", 175)
                    app.setMessageFg("java_sum", msgFg)
                    app.setMessageBg("java_sum", msgBg)
                    app.addLabel("spacer7", "")
                    app.addButton("Java Guide", Java)


    #########################
    #  Tab for System Info  #
    #########################

    with app.note("System Info"):
        # Retrieve System information
        try:
            call("/usr/local/bin/Solar Pi/Welcome/info.sh")
        except OSError:
            print("Running under Windows! ...or something has gone horribly wrong :(")

        # Read osinfo file
        with open("osinfo", "r") as file:
            data = file.readlines()
        for line in data:
            if line.startswith("PRETTY_NAME="):  # Take line that matches PRETTY_NAME=
                os_v = line.split("=")[1].lstrip("\"").rstrip("\"\n")  # Remove unnecessary elements of line
                break

        # Read sysinfo file
        with open("sysinfo", "r") as file:
            data = file.readlines()
        kernel_v = data[0].rstrip("\n")  # Kernel info in first line
        disk_data = data[2].split()  # Disk info in third line
        total_disk = disk_data[0] + "B"  # Fetch total disk space
        used_disk = disk_data[1] + "B"  # Fetch used disk space
        avail_disk = disk_data[2] + "B"  # Fetch available disk space
        pcent_disk_used = int(disk_data[3].rstrip("%"))  # Fetch used percentage
        pcent_disk_avail = 100 - pcent_disk_used  # Fetch used percentage

        # Read solarinfo file
        with open("solarinfo", "r") as file:
            data = file.readlines()
        for line in data:  # Iterate through file
            if line.startswith("RPi="):
                rpi_model = line.split("=")[1].rstrip("\n")  # Fetch RPi model
            elif line.startswith("Software="):
                solar_software = line.split("=")[1].rstrip("\n")  # Fetch Solar Pi software version
            elif line.startswith("Display="):
                display = line.split("=")[1].rstrip("\n")  # Fetch display info
            elif line.startswith("Battery="):
                battery = line.split("=")[1].rstrip("\n")  # Fetch battery info

        with app.labelFrame("Solar Pi Info"):
            app.setPadding(10, 5)
            app.addLabel("rpi_model", "Raspberry Pi:", 0, 0)
            app.getLabelWidget("rpi_model").config(font=bold_font)
            app.addLabel("rpi_model_value", rpi_model, 0, 1)

            app.addLabel("solar_soft", "Solar Pi Software:", 0, 2)
            app.getLabelWidget("solar_soft").config(font=bold_font)
            app.addLabel("solar_soft_value", solar_software, 0, 3)

            app.addLabel("display", "Display:", 1, 0)
            app.getLabelWidget("display").config(font=bold_font)
            app.addLabel("display_value", display, 1, 1)

            app.addLabel("battery", "Battery:", 1, 2)
            app.getLabelWidget("battery").config(font=bold_font)
            app.addLabel("battery_value", battery, 1, 3)


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
                if pcent_disk_used > 90:
                    app.setMeterFill("disk_usage", "red")
                else:
                    app.setMeterFill("disk_usage", "#687396")
                app.setMeterSticky("disk_usage", "ew")
                app.setMeterTooltip("disk_usage", "Used: " + used_disk + "\nFree: " + avail_disk)
                app.addLabel("disk_label", avail_disk + " free of " + total_disk, 1, 0)
            app.setFrameSticky("frame22", "ew")


def Startup(param):
    value = app.getCheckBox("Launch at startup")
    setSetting("welcome", str(value))
    Autorun("welcome", value, "/home/pi/.config/autostart/Welcome Launcher.desktop")

app.setPadding(5, 5)
app.addCheckBox("Launch at startup")
app.setCheckBox("Launch at startup", ticked=getSetting("welcome"))
app.setCheckBoxChangeFunction("Launch at startup", Startup)

app.setListBoxGroup("list", True)
app.setListBoxGroup("list2", True)
app.selectListItemAtPos("list", 0, callFunction=True)
app.selectListItemAtPos("list2", 0, callFunction=True)

t = Thread(target=fade)
t.start()

try:
    w = Watcher()
    t2 = Thread(target=w.run)
    t2.start()
except:
    pass

settings(True)

app.go(language=getSetting("language"))
