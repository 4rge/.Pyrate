# This Python file uses the following encoding: utf-8

import sys; import os; import shutil; import atexit; import requests; import qrcode; import wget; import codecs; import urllib.request; import tempfile; from bs4 import BeautifulSoup; import subprocess; from collections import deque; import re; import youtube_dl; from shutil import make_archive; from zipfile import ZipFile
from AudioFile import AudioFile
from PyQt5.QtWidgets import *; from PyQt5.QtWebEngineCore import QWebEngineCookieStore; from PyQt5.QtWebEngineWidgets import QWebEngineProfile, QWebEnginePage, QWebEngineView; from PyQt5.QtGui import QIcon; from PyQt5.QtCore import QUrl; from PyQt5.QtNetwork import QNetworkProxy

class after_thought():
    def __init__(self):
        for artists in os.listdir(os.getcwd()+"/.Pyrate/Set_List/"):
            if artists.endswith(".txt"):
                try:
                    loc = os.getcwd()+"/.Pyrate/Set_List/"
                    for bandName in os.listdir(loc):
                        if bandName.endswith(".txt"):
                            with open(loc+bandName) as setlist:
                                tracks = setlist.readlines(); q = deque()
                                setlist.close(); os.remove(loc+bandName)
                                for trk_numbr in tracks:
                                    trk = q.append(trk_numbr)
                                    try:
                                        with youtube_dl.YoutubeDL({'format':'bestaudio/best', 'keepvideo':True, 'outtmpl':'Music/'+bandName.replace(".txt", "")+'/%(title)s.mp3'}) as ydl:
                                            ydl.download([(youtube_dl.YoutubeDL().extract_info(url = ("https://www.youtube.com/watch?v=" + (re.findall(r"watch\?v=(\S{11})", (urllib.request.urlopen("https://www.youtube.com/results?search_query=" + (bandName+q.popleft()).replace(" ", "+"))).read().decode()))[0]), download=False))['webpage_url']])
                                    except: continue
                except: continue

class PyrateBrowser(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        proxy = QNetworkProxy()
        proxy.setType(1); proxy.setHostName("127.0.0.1"); proxy.setPort(9050); proxy.setApplicationProxy(proxy)
        cwd = os.getcwd(); temp = tempfile.mktemp(); engine = QWebEngineView(); self.tabs = QTabWidget(); self.status = QStatusBar(); navtb = QToolBar("Navigation"); combobox2 = QComboBox(self); combobox3 = QComboBox(self); urlb = QToolBar("URL"); self.urlbar = QLineEdit(); combobox1 = QComboBox(self)

        def clean():
            try: os.unlink(temp)
            except:pass

        def clear():
            QWebEngineCookieStore.deleteAllCookies; QWebEngineProfile().clearHttpCache(); QWebEngineProfile().clearAllVisitedLinks()

        def AudioFile():
            subprocess.Popen("python3 "+cwd+"/.Pyrate/AudioFile.py", shell=True, stdout=subprocess.PIPE).stdout.read()

        def text_changed0(self):
            set_lang = combobox2.currentText()
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            if set_lang == ".chartCourse":
                fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()",cwd+"/.Pyrate/Bookmarks/" ,"*", options=options)
                if fileName: self.add_new_tab(QUrl(fileName).fromLocalFile(fileName))
            elif set_lang == ".makeNote":
                fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()",cwd+"/.Pyrate/Bookmarks/" ,"*", options=options); inj_site = cwd+"/.Pyrate/Injection"; soup = BeautifulSoup(requests.get(self.urlbar.text()).content)
                with open(inj_site+"/injection.html") as inj:
                    script = inj.read()
                    inj.close()
                with open(fileName+".html", "w", encoding = 'utf-8') as file:
                    file.write(script+str(soup.prettify()))
            combobox2.setCurrentText(".mapRoom")

        def text_changed1(self):
            set_lang = combobox3.currentText()
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            if set_lang == ".qrMatey": qrcode.make(self.urlbar.text()).save(temp); self.add_new_tab(QUrl(temp).fromLocalFile(temp))
            elif set_lang == ".downLoad":
                fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()",cwd+"/Downloads/" ,"*", options=options)
                if fileName: wget.download(self.urlbar.text()); os.rename("download.wget", fileName)
            elif set_lang == ".seaShanties": AudioFile()
            elif set_lang == ".djanGo()":
                fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()",cwd ,"*", options=options)
                if fileName:
                    Name = ((fileName).split("/"))[3]
                    subprocess.run(["django-admin", "startproject", Name], capture_output=True)
                    self.add_new_tab(QUrl("http://127.0.0.1:8000/"))
                msg = QMessageBox(self)
                msg.setWindowTitle("/Yarrr!"); msg.setText("Now launch a seperate terminal and run 'python3 manage.py runserver'"); ok_btn = QMessageBox.addButton(msg, 0x00000400); msg.exec_()
            elif set_lang == ".abandonShip":
                msg = QMessageBox(self)
                msg.setWindowTitle("/Yarrr!"); msg.setText("This will delete ALL .local files associated with this instance."); ok_btn = QMessageBox.addButton(msg, 0x00000400); msg.exec_()
                if msg.clickedButton(): shutil.rmtree(cwd+"/.local/share/QtWebEngine")
            combobox3.setCurrentText(".capsQuarters" )

        def text_changed2(self):
            nav = combobox1.currentText()
            if nav == "∩": self.tabs.currentWidget().reload()
            elif nav == "◄": self.tabs.currentWidget().back()
            elif nav == "►": self.tabs.currentWidget().forward()
            elif nav == "■": self.tabs.currentWidget().stop()
            combobox1.setCurrentText("_")

        engine.page().profile().setHttpCacheType(0); engine.page().profile().setPersistentCookiesPolicy(0); engine.page().profile().setHttpUserAgent("Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0"); self.tabs.setTabShape(1); self.tabs.setMovable(True); self.tabs.setDocumentMode(True); self.tabs.setTabsClosable(True); self.tabs.tabBarDoubleClicked.connect(self.tab_open_doubleclick); self.tabs.currentChanged.connect(self.current_tab_changed); self.tabs.tabCloseRequested.connect(self.close_current_tab); self.setCentralWidget(self.tabs); self.setStatusBar(self.status); self.addToolBar(navtb); combobox2.addItems([".mapRoom", ".chartCourse", ".makeNote"]); combobox2.currentTextChanged.connect(lambda: text_changed0(self)); navtb.addWidget(combobox2); combobox3.addItems([".capsQuarters", ".qrMatey", ".downLoad", ".seaShanties", ".djanGo()", ".abandonShip"]); combobox3.currentTextChanged.connect(lambda: text_changed1(self)); navtb.addWidget(combobox3); self.addToolBar(urlb); self.urlbar.returnPressed.connect(self.navigate_to_url); urlb.addWidget(self.urlbar); combobox1.addItems(["_", "◄", "►", "■", "∩"]); combobox1.currentTextChanged.connect(lambda: text_changed2(self)); urlb.addWidget(combobox1)

        self.setWindowIcon(QIcon(cwd+'/.Pyrate/.images/pp.png')); self.setWindowTitle(".Pyrate/.Browser"); self.setStyleSheet("color: #ffffff;" "background-color: #000000;" "selection-color: #fe2023;" "selection-background-color: #ffffff;"); self.status.setStyleSheet("background-color: #000000;"); self.tabs.setStyleSheet("background-image: url("+cwd+"/.Pyrate/.images/pp_sm.png);" "background-repeat: repeat-xy; background-color: #fe2023")

        ## un/comment to en/disable bowser_player as homepage
        self.add_new_tab(QUrl(cwd+'/.Pyrate/Bookmarks/.Pyrate_Player.html').fromLocalFile(cwd+'/.Pyrate/Bookmarks/.Pyrate_Player.html'))
        ## un/comment to en/disable ddg.onion homepage
#        self.add_new_tab(QUrl('https://duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion/'))

        self.show(); atexit.register(clear); atexit.register(clean)

    def add_new_tab(self, qurl=None, label="Blank"):
        cwd = os.getcwd()
        if qurl is None: qurl = QUrl("https://duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion/")
        browser = QWebEngineView(); browser.setUrl(qurl)
        try: title = self.tabs.currentWidget().page().title()
        except: title = label
        i = self.tabs.addTab(browser, QIcon(cwd+"/.Pyrate/.images/pp_sm.png"), title)
        self.tabs.setCurrentIndex(i)
        browser.urlChanged.connect(lambda qurl, browser=browser: self.update_urlbar(qurl, browser)); browser.loadFinished.connect(lambda _, i=i, browser=browser:self.tabs.setTabText(i, browser.page().title()))

    def tab_open_doubleclick(self, i):
        if i == -1: self.add_new_tab()

    def current_tab_changed(self, i): self.update_urlbar((self.tabs.currentWidget().url()), self.tabs.currentWidget())

    def close_current_tab(self, i):
        if self.tabs.count() < 2: self.destroy()
        self.tabs.removeTab(i)

    def navigate_to_url(self):
        q = QUrl(self.urlbar.text())
        if q.scheme() == ".onion": q.setScheme("onion")
        elif q.scheme() =="http": q.setScheme("http")
        elif q.scheme() == "": q = QUrl("https://duckduckgo.com/?q="+self.urlbar.text().replace(" ", "+")+"&t=h")
        self.add_new_tab(q)

    def update_urlbar(self, q, browser=None):
        if browser != self.tabs.currentWidget(): return
        self.urlbar.setText(q.toString()); self.urlbar.setCursorPosition(0)


if __name__ == "__main__":
    app = QApplication([])
    PyrateBrowser().show()
    atexit.register(after_thought)
    sys.exit(app.exec_())

