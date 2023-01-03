def pip_quick():
    if exists("/etc/apt/sources.list"):
        subprocess.call(["sudo apt install pip"], shell=True)
    elif exists("/ect/pacman.d"):
        subprocess.call(["sudo pacman -S pip"], shell=True)
    else:
        print("OS not supported")

    commands = {'requests', 'qrcode', 'urllib3', 'bs4', 'youtube_dl', 'wget', 'wikipedia'}

    for call in commands:
        subprocess.call(["pip install "+call], shell=True)
        
    py = ["python3-pyqt5", "python3-pyqt5.qtwebengine"]

    for sudo in py:
        if exists("/etc/apt/sources.list"):
            subprocess.call(["sudo apt install "+sudo], shell=True)
        elif exists("/ect/pacman.d"):
            subprocess.call(["sudo pacman -S "+sudo], shell=True)
        else:
            print("OS not supported")
