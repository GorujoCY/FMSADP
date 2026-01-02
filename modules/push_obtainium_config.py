import os

class AdbPushObtainiumConfig:

    def push_config(is_adb_established, c_os, config, adb_device=None):
        if isinstance(is_adb_established, list):
            if is_adb_established[0]:
                os.chdir(is_adb_established[1])
                if c_os == "Windows":
                    os.system(f'adb push {config} /sdcard/import_me_at_obtainium/config_for_updates.json')
                elif c_os.endswith("Linux") or c_os == 'Linux':
                    os.system(f'./adb push {config} /sdcard/import_me_at_obtainium/config_for_updates.json')
                else:
                    os.system(f'{is_adb_established[1]} push {config} /sdcard/import_me_at_obtainium/config_for_updates.json')
        elif isinstance(is_adb_established, bool):
            if is_adb_established:
                os.system(f'adb push {config} /sdcard/import_me_at_obtainium/config_for_updates.json')
        elif is_adb_established == 'built-in':
            adb_device.sync.push(config, '/sdcard/import_me_at_obtainium/config_for_updates.json')
