import subprocess


def pip_quick():
	commands = {'requests', 'qrcode', 'urllib3', 'bs4', 'youtube_dl', 'wget', 'wikipedia'}

	for call in commands:
		subprocess.call(["pip install "+call], shell=True)
	
	py = {"python3-pyqt5", "python3-pyqt5.qtwebengine"}

	for sudo in py:
		subprocess.call(["sudo apt install "+sudo], shell=True)
