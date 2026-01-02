from modules.prerequisites.adb_computer import AdbCheckComputer
from modules.prerequisites.client import AdbCheckClient
from modules.install_apps import AdbInstallApps
from modules.change_keyboard_and_launcher import AdbChangeKeyboardLauncher
from modules.uninstall_system_equivalents import AdbUninstallSystemEquivalents

#yup prerequisites is as simple as that
computer_os = AdbCheckComputer.check_os()

checked_adb = AdbCheckComputer.check_adb(computer_os)

adb_device = AdbCheckClient.authorize_device_adb(checked_adb, computer_os)

#START Yes/No question 1
print('Replace Play Store with Aurora Store?')
playstore_to_aurora_yn = ''
while playstore_to_aurora_yn.upper() not in ('NO', 'N', 'YES', 'Y'):
    playstore_to_aurora_yn = input('(Y)es/(N)o>')
    if playstore_to_aurora_yn.upper() not in ('NO', 'N', 'YES', 'Y'):
        print('Please just say "Y/y" or "N/n", "YES/yes" or "NO/no"')
        continue
#END Yes/No question 1

#START Yes/No question 2
print('Replace Google Suite with Proton Suite?')
google_suite_to_proton_yn = ''
while google_suite_to_proton_yn.upper() not in ('NO', 'N', 'YES', 'Y'):
    playstore_to_aurora_yn = input('(Y)es/(N)o>')
    if google_suite_to_proton_yn.upper() not in ('NO', 'N', 'YES', 'Y'):
        print('Please just say "Y/y" or "N/n", "YES/yes" or "NO/no"')
        continue
#END Yes/No question 2

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

#now begins the main bits

#installing
if checked_adb == 'built-in':
    AdbInstallApps.install_apps('offline', checked_adb, computer_os, 'bundled_apks', adb_device)
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
if checked_adb == 'built_in':
    AdbChangeKeyboardLauncher.change_some_apps(checked_adb, computer_os, adb_device)
else:
    AdbChangeKeyboardLauncher.change_some_apps(checked_adb, computer_os)



#Finally lets uninstall for supported manufacturers

#But first the google apps

#fun fact: most if not all chinese manufacturers include some form of system google apps on their global versions (eg. my Xiaomi had google contacts, google phone and google messages [which fair enough on the last one we normally install it]), that's why the list includes those

if checked_adb == 'built_in':
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


#Finally time for manufacturer specific
apmanufacturer = AdbCheckClient.check_phone_manufacturer(checked_adb, computer_os)
if checked_adb == 'built_in':
    apmanufacturer = AdbCheckClient.check_phone_manufacturer(checked_adb, computer_os, adb_device)
    if apmanufacturer == 'Xiaomi':
        with open('list_of_targeted_system_apps/xiaomi.txt') as xiaomi_list:
            AdbUninstallSystemEquivalents.uninstall_apps(checked_adb, computer_os, xiaomi_list.readlines())
    else:
        pass #basically add a messagee basically saying sorry no list yet for your manufacturer

else:
    if apmanufacturer.decode().replace('\n', '') == 'Xiaomi':
        with open('list_of_targeted_system_apps/xiaomi.txt') as xiaomi_list:
            AdbUninstallSystemEquivalents.uninstall_apps(checked_adb, computer_os, xiaomi_list.readlines())
    #add any other supported brands, in this case so far samsung
    #eg. elif apmanufacturer.decode().replace('\n', '') == 'Manufacturer':
    else:
        pass #basically add a messagee basically saying sorry no list yet for your manufacturer

#finally make an obtainium config
