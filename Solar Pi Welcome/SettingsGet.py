#!/usr/bin/env python


with open("/usr/local/bin/Solar Pi/Solar Pi Settings/Settings.ini") as file:
    data = file.readlines()[0]
    data = data.split(",")

def Clock():
        return int(data[0])

def BatteryMeter():
    if data[1] == "True":
        return True
    elif data[1] == "False":
        return False

def LaunchWelcome():
    if data[2] == "True":
        return True
    elif data[2] == "False":
        return False

def Theme():
    return data[3]


if __name__ == "__main__":
    print("This is a module!")
    exit()