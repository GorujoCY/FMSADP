from modules.prerequisites.adb_computer import AdbCheckComputer
from modules.prerequisites.client import AdbCheckClient
from modules.install_apps import AdbInstallApps
from modules.change_keyboard_and_launcher import AdbChangeKeyboardLauncher
from modules.uninstall_system_equivalents import AdbUninstallSystemEquivalents

#yup prerquisites is as simple as that now
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

#Finally lets uninstall for currently supported manufacturers
#finally make an obtainium config
