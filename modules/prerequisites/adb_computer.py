import platform
import os
import sys

class AdbCheckComputer:

    def check_computer():
        c_os = platform.system()
        if c_os == "Windows":
            return c_os
        elif c_os == "Linux":
            #check which distro
            distro = platform.freedesktop_os_release()['ID']
            if distro == 'ubuntu' or distro == "linuxmint":
                return "Ubuntu Linux"
            elif distro == 'debian' or distro == 'raspbian':
                return "Debian Linux"
            elif distro == "arch":
                return "Arch Linux"
            elif distro == "gentoo":
                return "Gentoo Linux"
            elif distro == "fedora" or distro == 'centos':
                if os.path.exists('/run/ostree-booted'):
                    return "Fedora Atomic Linux"
                else:
                    return "Fedora Linux"
            else:
                raise Warning("Unable to detect or missing linux distributions, currently the ones supported are: Fedora, Ubuntu/Debian and Arch. Assuming Generic distro.")
                return "Linux"
        else:
            raise Warning("Unable to detect your OS (it is likely you're using BSD, Android or MacOS), but you may be able to continue assuming you already have ADB, the prerequisite process is currently for Linux and Windows")


    def check_adb(c_os):
        if c_os.endswith("Linux") or c_os == "Linux":
            adbexists_L = os.system("which adb")
            if adbexists_L == 0:
                print("Found ADB installed on your PC!")
                return True
            else:
                print("Did not find adb, you can either let us install adb using your package manager or specify the directory adb is located or use the built-in adb module")
                print("1. Install ADB")
                print("2. Manally specify ADB Directory")
                print("3. use built-in ADB module [NOT RECOMMENDED]")
                choices1 = input(int("1/2/3>"))
                if choices2 == 3:
                    return "built-in"
                if choices2 == 2:
                    adbdir = input("Drag and Drop or Specify the directory ADB is located: ")
                    return [True, adbdir]
                if choices1 == 1:
                    if c_os.startswith("Debian") or os.startswith("Ubuntu"):
                        print("Installing `android-sdk`, you will be prompted your sudo user password")
                        os.system("sudo apt install android-sdk")
                        return True
                    elif c_os.startswith("Arch"):
                        print("Installing `android-tools`, you will be prompted your sudo user password")
                        os.system("sudo pacman -S android-tools")
                        return True
                    elif c_os.startswith("Gentoo"):
                        print("Installing `android-tools`, you will be switched to root user and asked to install android-tools")
                        #mind you im not sure if this is the correct, report it to issues or make a PR if it isn't, this one is solely based on research while others are on experience and research
                        os.system("su -")
                        os.system("emerge --ask dev-util/android-tools")
                        return True
                    elif c_os == "Fedora Linux":
                        print ("Installing `android-tools`, you will be prompted with your user pasword")
                        os.system("sudo dnf install android-tools")
                        return True
                    elif c_os == "Fedora Atomic Linux":
                        print("For fedora atomic or distros based on it, they use `rpm-ostree` for the package manager meaning you would need to reboot the pc and in turn the program. I advise on reconsidering your choice.\n\n")
                        print("1. Confirm")
                        print("2. Manally specify ADB Directory")
                        print("3. use built-in ADB module [NOT RECOMMENDED]")
                        choices1 = input(int("1/2/3>"))
                        if choices2 == 3:
                            return "built-in"
                        if choices2 == 2:
                            input("Drag and Drop or Specify the directory ADB is located: ")
                            return [True, adbdir]
                        if choices1 == 1:
                            print ("Installing `android-tools`, you will be prompted with your user pasword")
                            os.system("sudo rpm-ostree install android-tools")
                            return True
                    else:
                        print("Without properly detecting the distro we can't exactly initiate your package manager's command to install android-tools, see how to install it by searching 'Install android platform tools [distro]' if needed or do on your own or restart to get the other choices")
                        input()
                        exit()

        elif c_os == "Windows":
            adbexists_W = os.system("where adb")
            if adbexists_L == 0:
                print("Found ADB installed on your PC!")
                return True
            else:
                print("Did not find adb, you can either let us install adb using Winget or specify the directory adb is located or use the built-in adb module")
                print("1. Install ADB")
                print("2. Manally specify ADB Directory")
                print("3. use built-in ADB module [NOT RECOMMENDED (And nor is/will it tested)]")
                choices2 = input(int("1/2/3>"))
                if choices2 == 3:
                    return "built-in"
                if choices2 == 2:
                    abdpath = input("Drag and Drop or Specify the directory ADB is located: ")
                    return [True, adbdir]
                if choices1 == 1:
                    os.system('winget install Google.PlatformTools')
                    print("Press enter to restart sotware for 'adb' command to work")
                    input()
                    os.execv(sys.executable)

if __name__ == "__main__":

    print("Press enter to initiate test")
    input()

    c_os = AdbCheckcomputer.check_computer()
    print(c_os)

    print("Press enter to initiate adb check test")
    input()
    AdbCheckcomputer.check_adb(c_os)
