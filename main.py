import sys
# First import it
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *


# Then create a class
class MainWindow(QMainWindow):
    # First create a constructor
    def __init__(self):
        # Now create connection with parent class
        super(MainWindow, self).__init__()
        # Now we will create a browser which value would be other qtpackedge
        self.browser = QWebEngineView()
        # now set the url
        self.browser.setUrl(QUrl('http://www.google.com'))
        self.setCentralWidget(self.browser)
        # It will show the browser in fullscreen
        self.showMaximized()

        # Now we will create navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        # Now I will add back button
        back_btn = QAction('<-', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        # Now I will add forward button
        forward_btn = QAction('->', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        # Now I will add reload button
        reload_btn = QAction('⟳', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        # Now I will create home button
        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        # Now I will add a search bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl('http://google.com'))

    def navigate_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())


# Now we will see how it looks
app = QApplication(sys.argv)
QApplication.setApplicationName("A browser by Nafis Al-Ad-Din")

# Now create a window which will be just the window class u created
window = MainWindow()
app.exec_()
