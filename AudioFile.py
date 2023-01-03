import os
import sys
import urllib.request
from bs4 import BeautifulSoup
import wikipedia
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtNetwork import QNetworkProxy


class AudioFile(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        proxy = QNetworkProxy()
        proxy.setType(1)
        proxy.setHostName("127.0.0.1")
        proxy.setPort(9050)
        proxy.setApplicationProxy(proxy)
        toolb = QToolBar("URL")
        self.lineEdit = QLineEdit(self)
        self.lineEdit2 = QLineEdit(self)
        combobox2 = QComboBox(self)
        self.textEdit = QTextEdit(self)

        def track_search():
            try:
                soup = BeautifulSoup(
                    urllib.request.urlopen(
                        wikipedia.page(
                            f"{self.lineEdit.text()} {self.lineEdit2.text()}"
                        ).url
                    ).read()
                )
            except:
                soup = BeautifulSoup(
                    urllib.request.urlopen(
                        wikipedia.page(
                            f"{self.lineEdit.text()} {self.lineEdit2.text()} album"
                        ).url
                    ).read()
                )
            for link in soup.find_all("td"):
                w = link.get_text().strip()
                if w[:1] == '"':
                    self.textEdit.append(w.replace('"', ""))
                else:
                    pass
            self.lineEdit2.clear()

        def save():
            bandName = self.lineEdit.text()
            script = self.textEdit.toPlainText()
            with open(
                f"{os.getcwd()}/.Pyrate/Set_List/{bandName}.txt", "w", encoding="utf-8"
            ) as file:
                file.write(script)
                file.close()
            self.textEdit.clear()
            self.lineEdit.clear()

        def text_changed():
            nav = combobox2.currentText()
            if nav == "Save":
                save()
            if nav == "Album Search":
                track_search()
            combobox2.setCurrentText("")

        toolb.setOrientation(0x2)
        self.addToolBar(toolb)
        self.lineEdit.setObjectName("Artist Name")
        self.lineEdit.setPlaceholderText("Artist Name")
        toolb.addWidget(self.lineEdit)
        self.lineEdit2.setObjectName("Album Name")
        self.lineEdit2.setPlaceholderText("Album Name")
        toolb.addWidget(self.lineEdit2)
        combobox2.addItems(["", "Album Search", "Save"])
        combobox2.currentTextChanged.connect(lambda: text_changed())
        toolb.addWidget(combobox2)
        self.textEdit.setObjectName("Track List")
        self.textEdit.setPlaceholderText("Track List")
        self.textEdit.setAcceptRichText(False)
        self.setCentralWidget(self.textEdit)
        self.setWindowIcon(QIcon(f"{os.getcwd()}/.Pyrate/.images/pp.png"))
        self.setWindowTitle("Shanties")
        self.setStyleSheet(
            "color: #fe2023;"
            "background-color: #000000;"
            "selection-color: #ffffff;"
            "selection-background-color: #e01b24;"
        )
        self.lineEdit.setStyleSheet(
            "background-color: #ffffff;" "selection-color: #000000;"
        )
        self.lineEdit2.setStyleSheet(
            "background-color: #ffffff;" "selection-color: #000000;"
        )
        self.textEdit.setStyleSheet(
            "background-color: #ffffff;" "selection-color: #000000;"
        )


if __name__ == "__main__":
    app = QApplication([])
    AudioFile().show()
    sys.exit(app.exec_())
