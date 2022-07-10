import sys
from PySide6.QtWidgets import QApplication, QMainWindow

from MINI import Ui_MainWindow
import nltk
from nltk import word_tokenize
from nltk.tag import pos_tag

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.tokenize.clicked.connect(self.tokenizing)
        self.ui.parsing.clicked.connect(self.parse)

    def tokenizing(self):

        txt = self.ui.input.toPlainText()
        tokens=word_tokenize(txt)
        self.ui.tokenizeresponse.setText("Tokens are: "+str(tokens))

    def parse(self):
        txt=self.ui.input.toPlainText()
        pos=pos_tag(word_tokenize(txt))
        self.ui.parsingresponse.setText("Parts of Speech Tagging:"+str(pos))

if __name__=='__main__':
    app=QApplication(sys.argv)

    window=MainWindow()
    window.show()

    sys.exit(app.exec_())