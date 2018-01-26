from time import sleep
import smbus
from appJar import gui

i2c = smbus.SMbus(1)
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


while True:
    if cache != bat_percent():
        with open("../ramdisk/power", "w") as file:
            file.write(str(bat_percent()) + "," + pwr_mode())

        cache = bat_percent()

    else:
        pass

    if bat_percent() < 10:
        with gui("Notification", useTtk=True) as app:
            app.setBg("white")
            app.hideTitleBar()
            app.ttkStyle.configure("TButton", background="#324581", foreground="white", bordercolor="#687396")
            app.ttkStyle.map("TButton", background=[("pressed", "#172141"), ("active", "#4059a9")])
            app.addLabel("label", "The battery of your Solar Pi is running low.\nPlease save your work, as your Solar Pi will shut down soon.")
            app.addButton("Close", close)

    sleep(90)
