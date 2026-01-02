# FMSADP
FMSADP (Fossify(R) My Android Device Please) is a Python Software utilizing the Android(TM) Debug Bridge (ADB) for replacing system apps to a suite of apps. All rights to these respective apps and names belongs to them!

# In concerns of offline release
Codeberg limits file size to 100MB even on releases therefore those coming through codeberg you can either:
1. Install from the [Github Releases](https://github.com/GorujoCY/FMSADP/releases/latest)
2. Install through [Proton Drive](https://drive.proton.me/urls/333Y0RFB4W#SFEO3wys0Uiv) if you for some reason refuse to use github, either option is valid

# In regards to APKs
keep in mind that if you run from source, it requests (with your consent) github for the bundled apks zip. Unless I used tresorit send or pcloud transfer (the fact that both require email to even get me a link, forget it), this isn't possible and there aren't any good options to store at least a gigabyte or 1.1GB file permanently, means I resorted to github releases as the next best option. This is for the sake of making things simpler and to be functioning.

If you want you may go ahead and get it for yourself instead and extract it under the folder name `bundled_apks` for the program to work unless you wanna modify where it points at! You may also obtain a copy of them on [Proton Drive](https://drive.proton.me/urls/D1SEZVCCCR#E3d3QbZmnCVo)

The reason that they cannot be in the repo is size limit on each cloud based git platform (limited to either 25 or 100MB per file making it invalid to upload them directly)

# Running from executables

- For Linux simply double click the executable, if you dont see a terminal, try to right click and run within your respective terminal app (for Dolphin and KDE for example: `right click` on the executable and click `Run in Konsole`)

- For Windows double click the .exe (when that comes out, you can for now start with the run from source if you want)

- MacOS I will not be supproting because simply put I do not have a Mac, run from source instead

- BSD you can try with the linux compatibility or otherwise same with MacOS, run from source

# Running from source
0. Install python at https://www.python.org/ or your respective package manager (eg. for winget and windows, open windows terminal and run: `winget install Python.Python.3.14`). On windows **make sure you tick the `PATH` tickbox** for `python` command to work anywhere
1. Open your console/terminal (on Linux/Windows it can be done with right click with the exception of Windows 10) Run either `pip install adbutils[apk]` or `pip install -r requirements.txt` on the same directory as the program
2. run the program on the same terminal with `python main-offline-run_this_from_source.py`

# Report Issues
Feel free to report issues through the forums I shared or for better management open them in either Codeberg or Github and detail what issues you have and whenever related to the program or manufacturer

# TODO
- [ ] windows executable
- [ ] release online version
- [ ] complete readme
- [ ] Templates for issues either on the phone end or program end
### More readme stuff coming soon