from time import sleep
import smbus
from appJar import gui

i2c = smbus.SMBus(1)
cache = 0

def pwr_mode():
    data = i2c.read_byte_data(0x69, 0x00)
    data = data & ~(1 << 7)
    if data == 1:
        return "C"
    elif data == 2:
        return "B"

def bat_level():
    data = i2c.read_word_data(0x69, 0x08)
    data = format(data, "02x")
    return float(data) / 100

def bat_percent():
    volts = bat_level()
    percent = ((volts - 3.4) / 0.8) * 100
    return percent

def close():
    app.stop()

ignore = False

while True:
    percentage = bat_percent()
    mode = pwr_mode()

    print(percentage, mode)
    
    if cache != percentage or ignore == True:
        if percentage > 101 and mode == "B":
            ignore = True
        else:
            with open("../ramdisk/power", "w") as file:
                file.write(str(percentage) + "," + mode)
            ignore = False

        cache = percentage

    if bat_percent() < 10:
        with gui("Notification", useTtk=True) as app:
            with open("../Solar Pi Settings/Settings.ini", "r") as file:
                data = file.readlines()
            data = data[0]
            theme = data[3]
            if theme == "Solar Pi":
                app.setTtkTheme("plastik")
                app.setTtkTheme("clam")
                app.ttkStyle.configure("TButton", background="#324581", foreground="white", bordercolor="#687396")
                app.ttkStyle.map("TButton", background=[("pressed", "#172141"), ("active", "#4059a9")])
            else:
                app.setTtkTheme(theme)
            
            app.setBg("white")
            #app.hideTitleBar()
            app.setPadding(10, 10)
            
            app.addImage("warning", "/usr/local/bin/Solar Pi/Resources/Images/warning icon.gif")
            app.zoomImage("warning", -4)
            app.addLabel("label", "The battery of your Solar Pi is running low.\nPlease save your work, as your Solar Pi will shut down soon.", 0, 1)
            app.addButton("Close", close, colspan=2)


    sleep(90)
