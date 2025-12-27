import os
#from prerequisites.adb_computer import AdbCheckComputer
#from prerequisites.client import AdbCheckClient
#uncomment these and below for testing

class AdbUninstallSystemEquivalents:
    #manufacturer checks will be put into the main software with apps list being a list on text files,
    #also note that some apps refuse to uninstall and therefore fallback to disabling!
    def uninstall_apps(is_adb_established, c_os, apps: list, adb_device=None):
        print('Please note that some system apps will refuse to uninstall and therefore those marked will fallback to disabling')
        if isinstance(is_adb_established, list):
            if is_adb_established[0]:
                os.chdir(is_adb_established[1])
                if c_os == "Windows":
                    if 'DISABLE' in a:
                        os.system(f'adb shell pm disable-user --user 0 {a.replace('DISABLE ', '')}')
                    else:
                        os.system(f'adb shell pm uninstall --user 0 {a}')
                elif c_os.endswith("Linux") or c_os == 'Linux':
                    for a in apps:
                        if 'DISABLE' in a:
                            os.system(f'./adb shell pm disable-user --user 0 {a.replace('DISABLE ', '')}')
                        else:
                            os.system(f'./adb shell pm uninstall --user 0 {a}')
                else:
                     for a in apps:
                        if 'DISABLE' in a:
                            os.system(f'{is_adb_established[1]} shell pm disable-user --user 0 {a.replace('DISABLE ', '')}')
                        else:
                            os.system(f'{is_adb_established[1]} shell pm uninstall --user 0 {a}')
        elif isinstance(is_adb_established, bool):
            if is_adb_established:
                for a in apps:
                    if 'DISABLE' in a:
                        os.system(f'adb shell pm disable-user --user 0 {a.replace('DISABLE ', '')}')
                    else:
                        os.system(f'adb shell pm uninstall --user 0 {a}')
        elif is_adb_established == 'built-in':
             for a in apps:
                    if 'DISABLE' in a:
                        adb_device.shell(f'pm disable-user --user 0 {a.replace('DISABLE ', '')}')
                    else:
                        adb_device.shell(f'adb shell pm uninstall --user 0 {a}')


'''
if __name__ == '__main__':
    adb_c_os = AdbCheckComputer.check_os()
    adb_c_check_adb = AdbCheckComputer.check_adb(adb_c_os)
    print('Press enter to begin xiaomi uninstallation test')
    input()
    if adb_c_check_adb == 'built-in':
        adb_c_slash_d = AdbCheckClient.authorize_device_adb()
        xiaomiapps = open('') #xiaomi test
        AdbUninstallSystemEquivalents.uninstall_apps(adb_c_check_adb, adb_c_os, xiaomiapps.readlines(), adb_c_slash_d)
        xiaomiapps.close()
    else:
        xiaomiapps = open('') #google apps to go along
        AdbUninstallSystemEquivalents.uninstall_apps(adb_c_check_adb, adb_c_os, xiaomiapps.readlines())
        xiaomiapps.close()
'''
