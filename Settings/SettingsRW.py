import fileinput
import sys

def getSetting(setting):
    with open("Settings.ini", "r") as file:
        for line in file.readlines():
            if line.split("=")[0] == setting.upper():
                value = line.split("=")[1].rstrip("\n")
                if value == "True" or value == "False": value = value == "True"
                return value

def setSetting(setting, value):
    for line in fileinput.input(["Settings.ini"], inplace=True):
        if line.strip().startswith(setting.upper() + "="):  # Searches for setting
            line = setting.upper() + "=" + str(value) + "\n"  # Replaces line with value
        sys.stdout.write(line)  # Writes back to file

if __name__ == "__main__":
    print("This is a module!")
    exit()
