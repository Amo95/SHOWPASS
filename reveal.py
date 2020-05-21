import subprocess
import platform
import os
import sys
import time

# color effect on output
colors = dict(
    red='\033[91m', yellow='\33[93m',
    green='\033[1;32m', end='\033[0m')


# pass list (commands) of non-key arguments to split output and return the result
def process(*args):
    a = subprocess.check_output(args, shell=True).decode("utf-8")
    a = a.split("\n")
    return a

# linux platform
def linux():
    if os.getuid() == 0:
        a = process("cat /etc/NetworkManager/system-connections/*.nmconnection")
        # check SSIDs
        b = [m for m in a if "ssid=" in m]
        # check Keys
        a = [i for i in a if "psk=" in i]

        print(colors.get("red") + "\n[!]Available Wi-Fi Passwords" + colors.get("end"))
        print(colors.get("red") + "{}".format("="*29) + colors.get("end"))
        a[1], b[1] = b[1], a[1]
        print(a, b)

        # work here later

    else:
        print("{} Run program as root!! {}".format(colors.get("red"), colors.get("end")))

# windows platform
def windows(*args):
    a = process("netsh", "wlan", "show", "profiles")
    # passiing some list comprehension on var NB: line of code is from pythonhub
    a = [i.split(":"[1][1:-1] for i in results 
    if "All User Profile" in i)] # simple huh
    for i in a:
        results = process("netsh", "wlan", "profile", "key=clear")
        results = [b.split(":")[1][1:-1] for b in results 
        if "Key Content" in b]
        try:
            print("{:<30} {:<}".format(i, results))
        except IndexError:
            print("{:<30} {:<}".format(i, ""))

def macOs():
    pass

def main():
    if os.name == "posix":
        subprocess.call("clear", shell=True)
    else:
        subprocess.call("cls", shell=True)

    print("Select platform:")
    platforms = ["Linux", "Windows", "MacOs"]
    for p, i in enumerate(platforms, start=1):
        print(f"{[p]} {i}")

    inputs = int(input(">>> "))
    try:
        if inputs == 1:
            linux()
        elif inputs == 2:
            windows()
        elif inputs == 3:
            macOs()
        else:
            pass

    except FileNotFoundError:
        print("Select the correct OS of your device!!")
        print("Please wait", end=" ")

        time.sleep(5)

        if platform.system() == "Linux" or "Linux2":
            os.system("clear")
        else:
            subprocess.check_call("cls", shell=True)

        main(colors)

if __name__ == "__main__":
    main()
    