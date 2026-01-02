import os
#from prerequisites.adb_computer import AdbCheckComputer
#from prerequisites.client import AdbCheckClient
#uncomment these and below for testing

class AdbChangeKeyboardLauncher:

    def change_some_apps(is_adb_established, c_os, adb_device=None):
        if isinstance(is_adb_established, list):
            if is_adb_established[0]:
                os.chdir(is_adb_established[1])
                if c_os == "Windows":
                    os.system('adb shell pm set-home-activity org.fossify.home/.MainActivity')
                    os.system('adb shell ime enable org.futo.inputmethod.latin/.LatinIME')
                    os.system('adb shell ime set org.futo.inputmethod.latin/.LatinIME')
                elif c_os.endswith("Linux") or c_os == 'Linux':
                    os.system('./adb shell pm set-home-activity org.fossify.home/.MainActivity')
                    os.system('./adb shell ime enable org.futo.inputmethod.latin/.LatinIME')
                    os.system('./adb shell ime set org.futo.inputmethod.latin/.LatinIME')
                else:
                    os.system(f'{is_adb_established[1]} shell pm set-home-activity org.fossify.home/.MainActivity')
                    os.system(f'{is_adb_established[1]} shell ime enable org.futo.inputmethod.latin/.LatinIME')
                    os.system(f'{is_adb_established[1]} shell ime set org.futo.inputmethod.latin/.LatinIME')
        elif isinstance(is_adb_established, bool):
            if is_adb_established:
                os.system('adb shell pm set-home-activity org.fossify.home/.MainActivity')
                os.system('adb shell ime enable org.futo.inputmethod.latin/.LatinIME')
                os.system('adb shell ime set org.futo.inputmethod.latin/.LatinIME')
        elif is_adb_established == 'built-in':
            adb_device.shell('pm set-home-activity org.fossify.home/.MainActivity')
            adb_device.shell('ime enable org.futo.inputmethod.latin/.LatinIME')
            adb_device.shell('ime set org.futo.inputmethod.latin/.LatinIME')

'''if __name__ == '__main__':
    adb_c_os = AdbCheckComputer.check_os()
    adb_c_check_adb = AdbCheckComputer.check_adb(adb_c_os)
    if adb_c_check_adb == 'built-in':
        adb_c_slash_d = AdbCheckClient.authorize_device_adb(adb_c_check_adb, adb_c_os)
        AdbChangeKeyboardLauncher.change_some_apps(adb_c_check_adb, adb_c_os)
    else:
        AdbChangeKeyboardLauncher.change_some_apps(adb_c_check_adb, adb_c_os)'''
