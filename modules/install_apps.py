import os
#from prerequisites.adb_computer import AdbCheckComputer
#from prerequisites.client import AdbCheckClient
#uncomment these and below for testing
from adbutils import adb
import urllib

class AdbInstallApps:

    def install_apps(online_or_offline, is_adb_established, c_os, apks_path=None, urls_txt_file=None, adb_device=None):
        if isinstance(is_adb_established, list):
            if is_adb_established[0]:
                os.chdir(is_adb_established[1])
                if c_os == "Windows":
                    if online_or_offline == 'offline':
                        for apks in [f for f in os.listdir(apks_path) if os.path.isfile(os.path.join(apks_path, f))]:
                            os.system(f'adb install {apks_path}/{apks}')
                    elif online_or_offline == 'online':
                        with open(urls_txt_file) as txturlsf:
                            for ul in txturlsf.readlines():
                                print(f'Downloading and installing from {ul}')
                                urllib.request.urlretrieve(uf, 'temp.apk')
                                os.system('adb install temp.apk')
                                os.remove('temp.apk')
                elif c_os.endswith("Linux") or c_os == 'Linux':
                    if online_or_offline == 'offline':
                        for apks in [f for f in os.listdir(apks_path) if os.path.isfile(os.path.join(apks_path, f))]:
                            os.system(f'./adb install {apks_path}/{apks}')
                    elif online_or_offline == 'online':
                        with open(urls_txt_file) as txturlsf:
                                for ul in txturlsf.readlines():
                                    print(f'Downloading and installing from {ul}')
                                    if ul.startswith('https://api.github.com')
                                        urllib.request.Request

                                    else:
                                        urllib.request.urlretrieve(uf, 'temp.apk')
                                        os.system(f'./adb install temp.apk')
                                        os.remove('temp.apk')
                else:
                    if is_adb_established:
                        if online_or_offline == 'offline':
                            for apks in [f for f in os.listdir(apks_path) if os.path.isfile(os.path.join(apks_path, f))]:
                                os.system(f'{is_adb_established[2]} install {apks_path}/{apks}')
                        elif online_or_offline == 'online':
                            with open(urls_txt_file) as txturlsf:
                                for ul in txturlsf.readlines():
                                    print(f'Downloading and installing from {ul}')
                                    urllib.request.urlretrieve(uf, 'temp.apk')
                                    os.system(f'{is_adb_established[2]} install temp.apk')
                                    os.remove('temp.apk')
        elif isinstance(is_adb_established, bool):
            if is_adb_established:
                if online_or_offline == 'offline':
                    for apks in [f for f in os.listdir(apks_path) if os.path.isfile(os.path.join(apks_path, f))]:
                        os.system(f'adb install {apks_path}/{apks}')
                elif online_or_offline == 'online':
                    with open(urls_txt_file) as txturlsf:
                        for ul in txturlsf.readlines():
                            print(f'Downloading and installing from {ul}')
                            urllib.request.urlretrieve(uf, 'temp.apk')
                            os.system('adb install temp.apk')
                            os.remove('temp.apk')
        elif is_adb_established == 'built-in':
            if online_or_offline == 'offline':
                for apks in [f for f in os.listdir(apks_path) if os.path.isfile(os.path.join(apks_path, f))]:
                    adb_device.install(f'{apks_path}/{apks}')
            elif online_or_offline == 'online':
                pass # make a file that has all the download urls and distinctly also install them

''' if __name__ == '__main__':
    adb_c_os = AdbCheckComputer.check_os()
    adb_c_check_adb = AdbCheckComputer.check_adb(adb_c_os)
    on_or_off_line = input('online or offline?: ')
    if on_or_off_line == 'offline':
        path_for_apks = input('Enter paths of all necessary apks:').strip(' ')
        if adb_c_check_adb == 'built-in':
            d_adb = AdbCheckClient.authorize_device_adb(adb_c_check_adb, adb_c_os)
            print('Press enter to confirm mass install the apks in directory')
            input()
            AdbInstallApps.install_apps(on_or_off_line, adb_c_check_adb, adb_c_os, path_for_apks, d_adb)
        else:
            print('Press enter to confirm mass install the apks in directory')
            input()
            AdbInstallApps.install_apps(on_or_off_line, adb_c_check_adb, adb_c_os, path_for_apks)
    elif on_or_off_line == 'online':
        print('This is coming soon!')
        exit()
'''

