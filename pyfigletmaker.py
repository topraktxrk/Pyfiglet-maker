import time
import sys
import pyfiglet
import os
import platform
def homescreen():
    title = pyfiglet.figlet_format("Pyfiglet maker", font="slant")
    print(title)
def searchfonts():
    test = pyfiglet.FigletFont.getFonts()
    print(test)


def windowsorlinuxmac():
    asd = platform.system()
    asd.lower()
    if asd.lower() == "windows":
        os.system("cls")
    elif asd.lower() != "windows":
        os.system("clear")


while True:
    test = pyfiglet.FigletFont.getFonts()
    homescreen()
    print("[1]Create text")
    usrtrueinput = input()
    if usrtrueinput.isdigit() and int(usrtrueinput) == 1:
        print("do you want to search fonts?")
        print("yes or no?")
        doyouwanttosearch = input()
        doyouwanttosearch.lower()
        if doyouwanttosearch == "yes":
            searchfonts()
            print("Type the font you want to use:")
            fontinput = input()
            print("type the text you want to convert:")
            textinput = input()
            if fontinput in test:
                createdfontext = pyfiglet.figlet_format(textinput,font=fontinput)
                print(createdfontext)
                time.sleep(0.5)
                print("[1]exit\n[2]create text again\n[3]wait(228853 secs)")
                fontinputsector = int(input())
                if fontinputsector == 1:
                    windowsorlinuxmac()
                    break
                elif fontinputsector == 2:
                    time.sleep(0.00001)
                elif fontinputsector == 3:
                    time.sleep(228853)
        elif doyouwanttosearch == "no":
            print("type your font name in:")
            fontusrtype = input()
            print("type your text to convert:")
            textusrinput = input()
            if fontusrtype in test:
                outputfonttext = pyfiglet.figlet_format(textusrinput, font=fontusrtype)
                print(outputfonttext)
                time.sleep(0.5)
                print("[1]exit\n[2]create text again\n[3]wait(228853 secs)")
                outputfonttext = int(input())
                if outputfonttext == 1:
                    break
                    windowsorlinuxmac()
                elif outputfonttext == 2:
                    time.sleep(0.00001)
                elif outputfonttext == 3:
                    time.sleep(228853)
        else:
            print("invalid input")
            time.sleep(1)
            print("restarting script")
            time.sleep(2)
            windowsorlinuxmac()

            continue
    else:
        print("invalid option")
        time.sleep(1)
        print("restarting script")
        time.sleep(2)
        windowsorlinuxmac()

        continue
