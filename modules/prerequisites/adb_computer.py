import platform
import os
import sys

class AdbCheckComputer:

    def check_os():
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
                raise Warning("Unable to detect or missing linux distributions, currently the ones supported are: Fedora, Ubuntu/Debian, Arch & Gentoo. Assuming Generic distro.")
                return c_os
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
                print("3. use built-in ADB module")
                choices1 = int(input("1/2/3>"))
                if choices1 == 3:
                    return "built-in"
                if choices1 == 2:

                    #START of check dir
                    #------------------
                    curdir1 = os.getcwd()
                    found_adb = False
                    while not found_adb:
                        adbdir = input("Drag and Drop or Specify the directory ADB is located: ").strip(' ')
                        try:
                            os.chdir(adbdir)
                            is_adb_in_dir = os.system("./adb version")
                            if is_adb_in_dir == 0:
                                os.chdir(curdir1)
                                found_adb = True
                            else:
                                print('Did not find adb in this directory!')
                                continue
                        except FileNotFoundError:
                            print("No directory found like this!")
                            continue
                    #----------------
                    #END of check dir

                    return [True, adbdir] #for my testing when dragging the folder it adds a space so I make it automatically remove any spacing
                if choices1 == 1:
                    if c_os.startswith("Debian") or c_os.startswith("Ubuntu"):
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
                        print("3. use built-in ADB module")
                        choices2 = int(input("1/2/3>"))
                        if choices2 == 3:
                            return "built-in"
                        if choices2 == 2:

                            #START of check dir
                            #------------------
                            curdir1 = os.getcwd()
                            found_adb = False
                            while not found_adb:
                                adbdir = input("Drag and Drop or Specify the directory ADB is located: ").strip(' ')
                                try:
                                    os.chdir(adbdir)
                                    is_adb_in_dir = os.system("./adb version")
                                    if is_adb_in_dir == 0:
                                        os.chdir(curdir1)
                                        found_adb = True
                                    else:
                                        print('Did not find adb in this directory!')
                                        continue
                                except FileNotFoundError:
                                    print("No directory found like this!")
                                    continue
                            #----------------
                            #END of check dir

                            return [True, adbdir]
                        if choices2 == 1:
                            print ("Installing `android-tools`, you will be prompted with your user pasword")
                            os.system("sudo rpm-ostree install android-tools")
                            return True
                    else:
                        print("Without properly detecting the distro we can't exactly initiate your package manager's command to install android-tools/android-sdk, see how to install it by searching 'Install android platform tools [distro]' if needed or do on your own or restart to get the other choices")
                        input()
                        exit()

        elif c_os == "Windows":
            adbexists_W = os.system("where adb")
            if adbexists_W == 0:
                print("Found ADB installed on your PC!")
                return True
            else:
                print("Did not find adb, you can either let us install adb using Winget or specify the directory adb is located or use the built-in adb module")
                print("1. Install ADB")
                print("2. Manally specify ADB Directory")
                print("3. use built-in ADB module")
                choices3 = int(input("1/2/3>"))
                if choices3 == 3:
                    return "built-in"
                if choices3 == 2:

                     #START of check dir
                     #------------------
                     curdir1 = os.getcwd()
                     found_adb = False
                     while not found_adb:
                        adbdir = input("Drag and Drop or Specify the directory ADB is located: ").strip(' ')
                        try:
                            os.chdir(adbdir)
                            is_adb_in_dir = os.system("adb version")
                            if is_adb_in_dir == 0:
                                os.chdir(curdir1)
                                found_adb = True
                            else:
                                print('Did not find adb in this directory!')
                                continue
                        except FileNotFoundError:
                            print("No directory found like this!")
                            continue
                        #----------------
                        #END of check dir

                return [True, adbdir]
                if choices3 == 1:
                    os.system('winget install Google.PlatformTools')
                    print("Press enter to restart sotware for 'adb' command to work")
                    input()
                    os.execv(sys.executable)
        else:
            print("Do you: \n1. Have ADB Installed? \n2.Want to manually specify directory and let me know how you run ADB? \n3. Use the built-in ADB?")
            choices4 = int(input("1/2/3>"))
            if choices4 == 3:
                return "built-in"
            if choices4 == 2:
                abddir = input("Drag and Drop or Specify the directory ADB is located: ").strip(' ')
                adbcmd = print("How do you run ADB in that directory? \n1. ./adb \n2. adb ")
                acinput = int(input('1/2>'))
                if acinput == 1:

                     #START of check dir
                     #------------------
                    curdir1 = os.getcwd()
                    found_adb = False
                    while not found_adb:
                        adbdir = input("Drag and Drop or Specify the directory ADB is located: ").strip(' ')
                        try:
                            os.chdir(adbdir)
                            is_adb_in_dir = os.system("./adb version")
                            if is_adb_in_dir == 0:
                                os.chdir(curdir1)
                                found_adb = True
                            else:
                                print('Did not find adb in this directory!')
                                continue
                        except FileNotFoundError:
                            print("No directory found like this!")
                            continue
                    #----------------
                    #END of check

                    return [True, adbdir, './adb']
                elif acinput == 2:

                    #START of check dir
                    #------------------
                    curdir1 = os.getcwd()
                    found_adb = False
                    while not found_adb:
                        adbdir = input("Drag and Drop or Specify the directory ADB is located: ").strip(' ')
                        try:
                            os.chdir(adbdir)
                            is_adb_in_dir = os.system("adb version")
                            if is_adb_in_dir == 0:
                                os.chdir(curdir1)
                                found_adb = True
                            else:
                                print('Did not find adb in this directory!')
                                continue
                        except FileNotFoundError:
                            print("No directory found like this!")
                            continue
                    #----------------
                    #END of check dir

                    return [True, adbdir, 'adb']
            if choices4 == 1:
                return True


if __name__ == "__main__":
    c_os = AdbCheckComputer.check_os()
    print(c_os)
    check_adb_func = AdbCheckComputer.check_adb(c_os)
    if isinstance(check_adb_func, list):
        print(check_adb_func[0])
        print(check_adb_func[1])
    else:
        print(check_adb_func)
