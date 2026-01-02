from modules.prerequisites.adb_computer import AdbCheckComputer
from modules.prerequisites.client import AdbCheckClient
from modules.install_apps import AdbInstallApps
from modules.change_keyboard_and_launcher import AdbChangeKeyboardLauncher
from modules.uninstall_system_equivalents import AdbUninstallSystemEquivalents
from modules.push_obtainium_config import AdbPushObtainiumConfig
import os
import time
import urllib
import zipfile

#yup prerequisites is as simple as that
global computer_os
computer_os = AdbCheckComputer.check_os()

checked_adb = AdbCheckComputer.check_adb(computer_os)

adb_device = AdbCheckClient.authorize_device_adb(checked_adb, computer_os)


#since this is a run from source thing lets make it that it gets the zip and extracts
if os.path.exists('bundled_apks'):
    pass
else:
    print('Welcome! to continue with the offline installation you will need the bundled apks to be installed. \nBy pressing enter, the software will check for the zip if manually downloaded and extract it for you (make sure it is in the same folder as the program and it is called `bundled_apks.zip`). Otherwise it requests github releases of this project to get the zip and extract to the correct folder for you! If you agree press enter otherwise exit the software!')
    input()
    if os.path.isfile(os.path.join(os.getcwd(), 'bundled_apks.zip')):
        with zipfile.ZipFile('bundled_apks.zip') as tmp_b_a_zip:
            tmp_b_a_zip.extractall('bundled_apks')
        os.remove('bundled_apks.zip')
    else:
        urllib.request.urlretrieve('github release link to zip', 'temp_bundled_apks.zip')
        with zipfile.ZipFile('temp_bundled_apks.zip') as tmp_b_a_zip:
            tmp_b_a_zip.extractall('bundled_apks')
        os.remove('temp_bundled_apks.zip')

def clear_screen():
    if computer_os.endswith('Linux') or computer_os == 'Linux':
        os.system('clear')
    elif computer_os == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
        os.system('clear')

clear_screen()

#START Yes/No question 1
print('Replace Play Store with Aurora Store?')
playstore_to_aurora_yn = ''
while playstore_to_aurora_yn.upper() not in ('NO', 'N', 'YES', 'Y'):
    playstore_to_aurora_yn = input('(Y)es/(N)o>')
    if playstore_to_aurora_yn.upper() not in ('NO', 'N', 'YES', 'Y'):
        print('Please just say "Y/y" or "N/n", "YES/yes" or "NO/no"')
        continue
#END Yes/No question 1

clear_screen()

#START Yes/No question 2
print('Replace Google Suite with Proton Suite?')
google_suite_to_proton_yn = ''
while google_suite_to_proton_yn.upper() not in ('NO', 'N', 'YES', 'Y'):
    google_suite_to_proton_yn = input('(Y)es/(N)o>')
    if google_suite_to_proton_yn.upper() not in ('NO', 'N', 'YES', 'Y'):
        print('Please just say "Y/y" or "N/n", "YES/yes" or "NO/no"')
        continue
#END Yes/No question 2

clear_screen()

#START Browser question
print('Brave (Like Chrome but better) or Firefox (Ironfox)?')
print('1. Brave')
print('2. Firefox')
install_browser_choice = 3
while install_browser_choice not in (1, 2):
    install_browser_choice = int(input('1/2>'))
    if install_browser_choice not in (1, 2):
        print('Please select the choice by typing number 1 or 2')
        continue
#END Browser question
print('Thank you for answering...')
time.sleep(3)
clear_screen()

#now begins the main bits

#installing
if checked_adb == 'built-in':
    AdbInstallApps.install_apps('offline', checked_adb, computer_os, 'bundled_apks', adb_device)
    if install_browser_choice == 1:
        AdbInstallApps.install_apps('offline', checked_adb, computer_os, 'bundled_apks/browsers/brave', adb_device)
    elif install_browser_choice == 2:
        AdbInstallApps.install_apps('offline', checked_adb, computer_os, 'bundled_apks/browsers/ironfox', adb_device)
    #Google Suite to Proton suite
    if google_suite_to_proton_yn.upper() in ('Y', 'YES'):
        AdbInstallApps.install_apps('offline', checked_adb, computer_os, 'bundled_apks/when_consented_by_user/proton_suite', adb_device)
    if playstore_to_aurora_yn.upper() in ('Y', 'YES'):
        AdbInstallApps.install_apps('offline', checked_adb, computer_os, 'bundled_apks/when_consented_by_user/aurora_store', adb_device)
else:
    AdbInstallApps.install_apps('offline', checked_adb, computer_os, 'bundled_apks')
    #browser choice
    if install_browser_choice == 1:
        AdbInstallApps.install_apps('offline', checked_adb, computer_os, 'bundled_apks/browsers/brave')
    elif install_browser_choice == 2:
        AdbInstallApps.install_apps('offline', checked_adb, computer_os, 'bundled_apks/browsers/ironfox')
    #Google Suite to Proton suite
    if google_suite_to_proton_yn.upper() in ('Y', 'YES'):
        AdbInstallApps.install_apps('offline', checked_adb, computer_os, 'bundled_apks/when_consented_by_user/proton_suite')
    if playstore_to_aurora_yn.upper() in ('Y', 'YES'):
        AdbInstallApps.install_apps('offline', checked_adb, computer_os, 'bundled_apks/when_consented_by_user/aurora_store')

#finally change the launcher and Keyboard
if checked_adb == 'built-in':
    AdbChangeKeyboardLauncher.change_some_apps(checked_adb, computer_os, adb_device)
else:
    AdbChangeKeyboardLauncher.change_some_apps(checked_adb, computer_os)



#Finally lets uninstall for supported manufacturers

#But first the google apps

#fun fact: most if not all chinese manufacturers include some form of system google apps on their global versions (eg. my Xiaomi had google contacts, google phone and google messages [which fair enough on the last one we normally install it]), that's why the list includes those

if checked_adb == 'built-in':
    with open('list_of_targeted_system_apps/google_apps.txt') as gappsfilelist:
        AdbUninstallSystemEquivalents.uninstall_apps(checked_adb, computer_os, gappsfilelist.readlines(), adb_device)

    #Sort out the user's prayers
    if playstore_to_aurora_yn.upper() in ('Y', 'YES'):
        with open('list_of_targeted_system_apps/when_consented_by_user/just_for_aurora.txt') as aurora_disable:
            AdbUninstallSystemEquivalents.uninstall_apps(checked_adb, computer_os, aurora_disable.readlines(), adb_device)
    if google_suite_to_proton_yn.upper() in ('Y', 'YES'):
         with open('list_of_targeted_system_apps/when_consented_by_user/just_proton_suite.txt') as g_to_p_file_list:
            AdbUninstallSystemEquivalents.uninstall_apps(checked_adb, computer_os, g_to_p_file_list.readlines(), adb_device)
else:
    with open('list_of_targeted_system_apps/google_apps.txt') as gappsfilelist:
        AdbUninstallSystemEquivalents.uninstall_apps(checked_adb, computer_os, gappsfilelist.readlines())

    #Sort out the user's prayers
    if playstore_to_aurora_yn.upper() in ('Y', 'YES'):
        with open('list_of_targeted_system_apps/when_consented_by_user/just_for_aurora.txt') as aurora_disable:
            AdbUninstallSystemEquivalents.uninstall_apps(checked_adb, computer_os, aurora_disable.readlines())
    if google_suite_to_proton_yn.upper() in ('Y', 'YES'):
         with open('list_of_targeted_system_apps/when_consented_by_user/just_proton_suite.txt') as g_to_p_file_list:
            AdbUninstallSystemEquivalents.uninstall_apps(checked_adb, computer_os, g_to_p_file_list.readlines())


    #Put obtainium config to user's device to import for updates while respecting preference
    if playstore_to_aurora_yn.upper() in ('Y', 'YES') and google_suite_to_proton_yn.upper() in ('Y', 'YES'):
        AdbPushObtainiumConfig.push_config(checked_adb, computer_os, 'Obtainium_configs/With_Aurora_and_Proton/obtainium_config.json')
    elif playstore_to_aurora_yn.upper() in ('Y', 'YES'):
        AdbPushObtainiumConfig.push_config(checked_adb, computer_os, 'Obtainium_configs/With_aurora_store/obtainium_config.json')
    elif google_suite_to_proton_yn.upper() in ('Y', 'YES'):
        AdbPushObtainiumConfig.push_config(checked_adb, computer_os, 'Obtainium_configs/Just_Proton_Suite/obtainium_config.json')
    else:
        AdbPushObtainiumConfig.push_config(checked_adb, computer_os, 'Obtainium_configs/obtainium_config.json')


#Finally time for manufacturer specific
apmanufacturer = AdbCheckClient.check_phone_manufacturer(checked_adb, computer_os)
if checked_adb == 'built-in':
    apmanufacturer = AdbCheckClient.check_phone_manufacturer(checked_adb, computer_os, adb_device)
    if apmanufacturer == 'Xiaomi':
        with open('list_of_targeted_system_apps/xiaomi.txt') as xiaomi_list:
            AdbUninstallSystemEquivalents.uninstall_apps(checked_adb, computer_os, xiaomi_list.readlines(), adb_device)
            print('Done, check your phone now!')
            input()
            exit()
    elif apmanufacturer == 'Samsung':
        with open('list_of_targeted_system_apps/samsung.txt') as samsung_list:
            AdbUninstallSystemEquivalents.uninstall_apps(checked_adb, computer_os, samsung_list.readlines(), adb_device)
            print('Done, check your phone now!')
            input()
            exit()
    else:
         print('Sorry about that, the program currently does not support your manufacturer. Feel free to open an issue in codeberg with your phone manufacturer and willigness to (briefly) test your device to help and contribute to the project if you are willing to!')
         print('===============================================================================================================================================================')
         print("Support gets added manually and slowly but more often it will be untested and you will be warned if that's the case as to report issues")
         print('Apologies for the inconvenicence, But it is not over, check out these projects to do your own manual uninstallation (it is advised to stick with packages tagged recommended)!')
         print('Cantas (+ Shizuku): https://samolego.github.io/Canta/')
         print('Universal Android Debloater next generation: https://github.com/Universal-Debloater-Alliance/universal-android-debloater-next-generation')
         print('========================================================================================================================================')
         print("Thank for your understanding, Press enter to exit when you're done")
         input()
         exit()
else:
    if apmanufacturer.decode().replace('\n', '') == 'Xiaomi':
        with open('list_of_targeted_system_apps/xiaomi.txt') as xiaomi_list:
            AdbUninstallSystemEquivalents.uninstall_apps(checked_adb, computer_os, xiaomi_list.readlines())
            print('Done, check your phone now!')
            input()
            exit()
    elif apmanufacturer.decode().replace('\n', '') == 'Samsung':
        with open('list_of_targeted_system_apps/samsung.txt') as samsung_list:
            AdbUninstallSystemEquivalents.uninstall_apps(checked_adb, computer_os, samsung_list.readlines())
            print('Done, check your phone now!')
            input()
            exit()
    else:
         print('Sorry about that, the program currently does not support your manufacturer. Feel free to open an issue in codeberg with your phone manufacturer and willigness to (briefly) test your device to help and contribute to the project if you are willing to!')
         print('===============================================================================================================================================================')
         print("Support gets added manually and slowly but more often it will be untested and you will be warned if that's the case as to report issues")
         print('Apologies for the inconvenicence, But it is not over, check out these projects to do your own manual uninstallation (it is advised to stick with the recommended)!')
         print('Cantas (+ Shizuku): https://samolego.github.io/Canta/')
         print('Universal Android Debloater next generation: https://github.com/Universal-Debloater-Alliance/universal-android-debloater-next-generation')
         print('========================================================================================================================================')
         print("Thank for your understanding, Press enter to exit when you're done")
         input()
         exit()

#Notes for above function
#add any other supported brands, in this case so far samsung
#eg. elif apmanufacturer.decode().replace('\n', '') == 'Manufacturer':
#when needing to warn for untested add the following code
#print('WARNING: The manufacturer detected has been untested! \nYou may be able to continue however if you have spotted any issue please report it on our codeberg repo under 'Issues' and clearly describe what went wrong to resolve it for the hassle to be avoided. \nYou have been warned and and thank you for understanding, Press enter if you wanna continue or otherwise exit the program now!')
#input()
