import adb_shell
import os
import subprocess

class AdbCheckClient:

    def authorize_adb(adb_is_true):
        if isinstance(adb_is_true, list):
            if adb_is_true[0]:
                pass
        elif isinstance(adb_is_true, boolean)
            if adb_is_true:
                pass
        else:
              if adb_is_true == "built-in":
                  pass
        #todo: guide users towards turning on developer options, then authorize device

    def check_phone_manufacturer(adb_is_true, is_device_trusted, adbc=None, c_os=None):
        if isinstance(adb_is_true, list):
            if adb_is_true[0]:
                if is_device_trusted:
                    os.chdir(adb_is_true[1])
                    if c_os == "Windows":
                        c_manufacturer = subprocess.run(['adb', 'shell', 'getprop', 'ro.product.manufacturer'], capture_output=True)
                    elif c_os.endwith("Linux"):
                        c_manufacturer = subprocess.run('./adb', 'shell', 'getprop', 'ro.product.manufacturer'], capture_output=True)
        else:
            if isinstance(adb_is_true, boolean)
                if adb_is_true:
                    if is_device_trusted
                        c_manufacturer = subprocess.run(['adb', 'shell', 'getprop', 'ro.product.manufacturer'], capture_output=True)
            else:
                if adb_is_true == "built-in":
                    if is_device_trusted
                        adbc.shell("getprorp ro.product.manufacturer")
        return c_manufacturer
