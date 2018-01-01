# Solar Pi Apps

Your Solar Pi comes with a few custom apps that we have written to help you use your Solar Pi. Here, we'll explain what each one is for, and how to use them.

## Solar Pi Welcome
This is the main Solar Pi app that you see when you first log on to your Solar Pi. The toolbar at the top gives you options to shutdown, reboot of log out of your Pi. Also, you can change settings, open the file manager, see what the Solar Pi project is about and read these docs.

![welcome-toolbar]()

Also, at the bottom of the window, there is a bar showing how much battery is remaining in your Solar Pi. 100% means that your Solar Pi is fully charged, and 0% means that your Solar Pi has no power and you need to charge it.

![battery-meter]()

### Welcome!
![welcome]()

This tab introduces you to your Solar Pi. There are popups to show you what the Solar Pi project is about and also links you to the [languages](solar-pi-apps.md#languages) app, to allow you to change the display language of your Solar Pi.

### Get Started
![get-started]()

In this tab, it explains the touchscreen and the Main Menu. It also provides a link to this page in the docs.

### Applications
![applications]()

The applications tab shows you apps that you might find useful. On the top row, you can access the [Solar Pi Settings](solar-pi-apps.md#solar-pi-settings) app, and an app that will help explain the main programming languages supported on the Solar Pi, and the IDEs (**I**ntegrated **D**evelopment **E**nvironment) that go with them.

On the second row, you'll find launchers for IDEs for each main programming language. You can also hover over the icons to get a brief overview of what each application does.

### Guides & Tutorials
![guides-tutorials]()

Here, you'll find the guides and tutorials for programming. Click on the buttons to launch the applications, and hover over the icons to get a brief overview on what the guides and tutorials help you with.


## Start Programming
This app helps you decide where to start programming. It explains the 3 main programming languages supported on the Solar Pi: Scratch, [Python](/Advanced-Things/python.md) and Java.

![programming screenshot]()

To do this, select a language, and click "More Info". A popup box should then appear giving you a brief overview of the language. Once you have decided, click "Go", and the relevant IDE should launch.

## Python Guides
text goes here

## Solar Pi Docs
Not really an app, but still important. This is all the documentation for your Solar Pi. It opens in the Chromium web browser, to allow for easy navigation with a touchscreen. You can navigate different pages via clicking on the icon in the top left, and you can skip through different sections of a page through the menu on the right. You can search through the docs using the search bar in the top right. Links are highlighted in [green](solar-pi-apps.md#solar-pi-docs), and these will take you to different places in the docs.

## Solar Pi Settings
The Solar Pi Settings app allows you to change settings for your Solar Pi. These are settings that can't be changed from the default Raspbian installation, and are specific to the Solar Pi. When you have finished changing the settings, ensure that you click 'Apply' and reboot.

If you want to revert to default settings, click 'Restore Defaults' and reboot.

### Performance & Power
These settings are related to the performance and power of your Solar Pi. The slider at the top of this section allows you to change the clock speed of your Solar Pi's CPU (**C**entral **P**rocessing **U**nit - effectively the 'brain' of your Solar Pi.). The default is 1200MHz (Megahertz), which will give you maximum performance, but you can lower it to 600MHz if you would like to extend the battery life of your Solar Pi. There is also a text box where you can type the clock speed in, if this is easier for you.

The checkbox that's labelled `'Show standalone battery meter'` controls whether you see the battery meter that is on the bottom left of your screen. If this gets in the way, you can remove it.

### Updates
Currently, you need an internet connection to update your Solar Pi, but this is due to change in the near future.

### Other Settings
The checkbox that's labelled `'Launch the Solar Pi welcome application at startup'` controls if you see the Solar Pi Welcome app when you log in. This is on by default, but once you get used to using your Solar Pi, you can turn it off.

The next option is labelled `'Theme for Solar Pi apps:'`. This controls how Solar Pi apps look. The default is `'plastik'`, but you can always change it by clicking on the box, and selecting from the drop down menu.

Finally, at the bottom of the section, there are buttons which say `'Change Advanced Settings'` and `'Languages'`. The `'Change Advanced Settings'` takes you to the Raspberry Pi Configuration app, and will allow you to tweak things further. The `'Languages'` button takes you to the [Languages app](solar-pi-apps.md#languages), and will allow you to change the display language of your Solar Pi.

!!! warning
	Only go into the Advanced Settings if you know what you are doing!

## Languages
This allows you to change the display language of your Solar Pi. If the language that is currently used is not suitable, you can change it by clicking on the button for your language. After that, you'll need to reboot your Solar Pi.