import subprocess
import os
#uncomment below to run the testing
#from adb_computer import AdbCheckComputer
#also uncomment the if statement below
from adbutils import adb
from adbutils.errors import AdbError

class AdbCheckClient:

    def authorize_device_adb(adb_is_true, s_os):
        if isinstance(adb_is_true, list):
            if adb_is_true[0]:
                os.chdir(adb_is_true[1])
                if s_os == "Windows":
                    adb_c_slash_d_check_cmd = subprocess.run(['adb', 'devices'], capture_output=True).stdout
                    while adb_c_slash_d_check_cmd == b'List of devices attached\n\n':
                        print("Please connect a device and/or check a guide on how to turn on developer options on your device and go to it. Press enter when you're done!")
                        input()
                        print("Now enable USB Debugging and Authorize your computer (DONT FORGET to also tick Always allow from this computer for a more convenient experience)! \nWARNING: Xiaomi prevents install via usb and usb debugging (security settings) by default unless you make a xiaomi account or do workarounds (required for app installations and keyboard change to work), search for that same guide on how to bypass it or make a temporary account! It is a frustrating limitation that Xiaomi implements that is out of our control. Press enter when done")
                        input()
                        print("Trying again...")
                        adb_c_slash_d_check_cmd = subprocess.run(['adb', 'devices'], capture_output=True).stdout
                        if adb_c_slash_d_check_cmd == b'List of devices attached\n\n':
                            print("Device not connected or have not enabled USB Debugging")
                            continue
                        else:
                            break
                    while b'unauthorized' in adb_c_slash_d_check_cmd:
                        print("Please allow your pc to use usb debugging on your device to continue, press enter when done!")
                        input()
                        adb_c_slash_d_check_cmd = subprocess.run(['adb', 'devices'], capture_output=True).stdout
                        if b'unauthorized' in adb_c_slash_d_check_cmd:
                            print("Device still unauthorized")
                            continue
                        else:
                            return True
                            break


                elif s_os.endswith("Linux") or s_os == "Linux":
                    adb_c_slash_d_check_cmd = subprocess.run(['./adb', 'devices'], capture_output=True).stdout
                    while adb_c_slash_d_check_cmd == b'List of devices attached\n\n':
                        print("Please connect a device and/or check a guide on how to turn on developer options on your device and go to it. Press enter when you're done!")
                        input()
                        print("Now enable USB Debugging and Authorize your computer (DONT FORGET to also tick Always allow from this computer for a more convenient experience)! \nWARNING: Xiaomi prevents install via usb and usb debugging (security settings) by default unless you make a xiaomi account or do workarounds (required for app installations and keyboard change to work), search for that same guide on how to bypass it or make a temporary account! It is a frustrating limitation that Xiaomi implements that is out of our control. Press enter when done")
                        input()
                        print("Trying again...")
                        adb_c_slash_d_check_cmd = subprocess.run(['./adb', 'devices'], capture_output=True).stdout
                        if adb_c_slash_d_check_cmd == b'List of devices attached\n\n':
                            print("Device not connected or have not enabled USB Debugging")
                            continue
                        else:
                            break
                    while b'unauthorized' in adb_c_slash_d_check_cmd:
                        print("Please allow your pc to use usb debugging on your device to continue, press enter when done!")
                        input()
                        adb_c_slash_d_check_cmd = subprocess.run(['./adb', 'devices'], capture_output=True).stdout
                        if b'unauthorized' in adb_c_slash_d_check_cmd:
                            print("Device still unauthorized")
                            continue
                        else:
                            return True
                            break
                else:
                    adb_c_slash_d_check_cmd = subprocess.run([f'{adb_is_true[2]}', 'devices'], capture_output=True).stdout
                    while adb_c_slash_d_check_cmd == b'List of devices attached\n\n':
                        print("Please connect a device and/or check a guide on how to turn on developer options on your device and go to it. Press enter when you're done!")
                        input()
                        print("Now enable USB Debugging and Authorize your computer (DONT FORGET to also tick Always allow from this computer for a more convenient experience)! \nWARNING: Xiaomi prevents install via usb and usb debugging (security settings) by default unless you make a xiaomi account or do workarounds (required for app installations and keyboard change to work), search for that same guide on how to bypass it or make a temporary account! It is a frustrating limitation that Xiaomi implements that is out of our control. Press enter when done")
                        input()
                        print("Trying again...")
                        adb_c_slash_d_check_cmd = subprocess.run(['./adb', 'devices'], capture_output=True).stdout
                        if adb_c_slash_d_check_cmd == b'List of devices attached\n\n':
                            print("Device not connected or have not enabled USB Debugging")
                            continue
                        else:
                            break
                    while b'unauthorized' in adb_c_slash_d_check_cmd:
                        print("Please allow your pc to use usb debugging on your device to continue, press enter when done!")
                        input()
                        adb_c_slash_d_check_cmd = subprocess.run(['./adb', 'devices'], capture_output=True).stdout
                        if b'unauthorized' in adb_c_slash_d_check_cmd:
                            print("Device still unauthorized")
                            continue
                        else:
                            return True
                            break

        elif isinstance(adb_is_true, bool):
            if adb_is_true:
                adb_c_slash_d_check_cmd = subprocess.run(['adb', 'devices'], capture_output=True).stdout
                while adb_c_slash_d_check_cmd == b'List of devices attached\n\n':
                    print("Please connect a device and/or check a guide on how to turn on developer options on your device and go to it. Press enter when you're done!")
                    input()
                    print("Now enable USB Debugging and Authorize your computer (DONT FORGET to also tick Always allow from this computer for a more convenient experience)! \nWARNING: Xiaomi prevents install via usb and usb debugging (security settings) by default unless you make a xiaomi account or do workarounds (required for app installations and keyboard change to work), search for that same guide on how to bypass it or make a temporary account! It is a frustrating limitation that Xiaomi implements that is out of our control. Press enter when done")
                    input()
                    print("Trying again...")
                    adb_c_slash_d_check_cmd = subprocess.run(['adb', 'devices'], capture_output=True).stdout
                    if adb_c_slash_d_check_cmd == b'List of devices attached\n\n':
                        print("Device not connected or have not enabled USB Debugging")
                        continue
                    else:
                        break
                while b'unauthorized' in adb_c_slash_d_check_cmd:
                    print("Please allow your pc to use usb debugging on your device to continue, press enter when done!")
                    input()
                    adb_c_slash_d_check_cmd = subprocess.run(['adb', 'devices'], capture_output=True).stdout
                    if b'unauthorized' in adb_c_slash_d_check_cmd:
                        print("Device still unauthorized")
                        continue
                    else:
                        return True
                        break
        else:
            if adb_is_true == "built-in":
                d_found = False
                while not d_found:
                    try:
                        adb_c_slash_d = adb.device()
                        return adb_c_slash_d
                        d_found = True
                    except AdbError:
                        print("Please connect the device and check a guide on how to turn on developer options on your device and go to it. Press enter when you're done! (you will get the same prompts if you didnt authorize the device)")
                        input()
                        print("Now enable USB Debugging and Authorize your computer (DONT FORGET to also tick Always allow from this computer for a more convenient experience)! \nWARNING: Xiaomi prevents install via usb and usb debugging (security settings) by default unless you make a xiaomi account or do workarounds (required for app installations and keyboard change to work), search for that same guide on how to bypass it or make a temporary account! It is a frustrating limitation that Xiaomi implements that is out of our control. Press enter when done")
                        input()
                        print("Trying again")
                        continue


    def check_phone_manufacturer(adb_is_true, s_os, adbc=None):
        if isinstance(adb_is_true, list):
            if adb_is_true[0]:
                os.chdir(adb_is_true[1])
                if s_os == "Windows":
                    c_manufacturer = subprocess.run(['adb', 'shell', 'getprop', 'ro.product.manufacturer'], capture_output=True).stdout
                elif s_os.endswith("Linux") or s_os == "Linux":
                    c_manufacturer = subprocess.run(['./adb', 'shell', 'getprop', 'ro.product.manufacturer'], capture_output=True).stdout
                else:
                    c_manufacturer = subprocess.run([f'{adb_is_true[2]}', 'shell', 'getprop', 'ro.product.manufacturer'], capture_output=True).stdout
        elif isinstance(adb_is_true, bool):
            if adb_is_true:
                c_manufacturer = subprocess.run(['adb', 'shell', 'getprop', 'ro.product.manufacturer'], capture_output=True).stdout
        else:
            if adb_is_true == 'built-in':
                c_manufacturer = adbc.prop.get("ro.product.manufacturer")

        return c_manufacturer

if __name__ == "__main__":
    #run prerequisites
    c_slash_s_os = AdbCheckComputer.check_os()
    establish_adb = AdbCheckComputer.check_adb(c_slash_s_os)
    #this module
    authorized_device = AdbCheckClient.authorize_device_adb(establish_adb, c_slash_s_os)

'''if establish_adb == 'built-in':
    print(AdbCheckClient.check_phone_manufacturer(establish_adb, c_slash_s_os, authorized_device))
else:
    print(AdbCheckClient.check_phone_manufacturer(establish_adb, c_slash_s_os).decode())''' #remove quotations of these lines to initiate testing
