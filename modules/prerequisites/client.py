import subprocess
from adbutils import adb

class AdbCheckClient:

    def authorize_device_adb(adb_is_true, s_os):
        if isinstance(adb_is_true, list):
            if adb_is_true[0]:
                os.chdir(adb_is_true[1])
                if s_os == "Windows":
                    adb_c_slash_d_check_cmd = subprocess.run(['adb', 'devices'], capture_output=True).stdout
                    if 'unauthorized' in adb_c_slash_d_check_cmd:
                        pass #just like below basically
                elif s_os.endwith("Linux") or s_os == "Linux":
                    adb_c_slash_d_check_cmd = subprocess.run(['./adb', 'devices'], capture_output=True).stdout
                    if 'unauthorized' in adb_c_slash_d_check_cmd:
                        pass #just like below basically
        elif isinstance(adb_is_true, bool)
            if adb_is_true:
                adb_c_slash_d_check_cmd = subprocess.run(['adb', 'devices'], capture_output=True).stdout
                if 'unauthorized' in adb_c_slash_d_check_cmd:
                    pass #just like below basically
        else:
              if adb_is_true == "built-in":
                  adb_c_slash_d = None
                  while adb_c_slash_d == None:
                    try:
                        adb_c_slash_d = adb.device()
                        return adb_c_slash_d
                    except AdbError:
                        adb_c_slash_d = None
                        print("Please check a guide on how to turn on developer options on your device and go to it. Press enter when you're done! (you will get the same prompts if you didnt authorize the device)")
                        input()
                        print("Now enable USB Debugging and Authorize your computer (DONT FORGET to also tick Always allow from this computer for a more convenient experience)! \nWARNING: Xiaomi prevents install via usb by default unless you make a xiaomi account or do workarounds (required for app installations to work), search for that same guide on how to bypass it or make a temporary account! It is a frustrating limitation that Xiaomi implements that is out of our control.")
                        input()
                        print("Trying again")
                        continue


    def check_phone_manufacturer(adb_is_true, s_os, adbc):
        if isinstance(adb_is_true, list):
            if adb_is_true[0]:
                os.chdir(adb_is_true[1])
                if s_os == "Windows":
                    c_manufacturer = subprocess.run(['adb', 'shell', 'getprop', 'ro.product.manufacturer'], capture_output=True)
                elif s_os.endwith("Linux") or s_os == "Linux":
                    c_manufacturer = subprocess.run('./adb', 'shell', 'getprop', 'ro.product.manufacturer'], capture_output=True)}
        else:
            if isinstance(adb_is_true, bool)
                if adb_is_true:
                    c_manufacturer = subprocess.run(['adb', 'shell', 'getprop', 'ro.product.manufacturer'], capture_output=True)
            else:
                if adb_is_true == "built-in":
                    c_manufacturer = adbc.prop.get("ro.product.manufacturer")
        return c_manufacturer
