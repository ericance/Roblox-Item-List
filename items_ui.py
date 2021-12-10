'''
	Name : items_ui.py
	Author: Eric Stalcup
	Created : 11/17/2021
	Course: CIS 152 - Data Structure
	Version: 1.0
	OS: Windows 10
	IDE: Visual Studio Code 1.61.2
	Copyright : This is my own original work 
	based on specifications issued by our instructor
	
	Description : This is where the user interface is created, which is the
	main portion to the application (since the goal is displaying data visually).
	It uses the list that is created from the ItemData class to fill the UI with
	useful information.
	
	Academic Honesty: I attest that this is my original work.
	I have not used unauthorized source code, either modified or
	unmodified. I have not given other fellow student(s) access
	to my program.
'''


from PyQt5 import QtCore, QtGui, QtWidgets
import webbrowser

class ItemWindow(object):
	def __init__(self):
		self.buttons = []
		self.urls = [] # Used to store the the url value for each button

	# Creates all of the UI objects
	def setupUi(self, MainWindow, data_list):
		
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(800, 1020)

		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setStyleSheet(
			"#__template {\n"
			"	background-color: #FFFFFF;\n"
			"}\n"
			"\n"
			"#itemMenu {\n"
			"	background-color: #49a0bf;\n"
			"}\n"
		)

		self.centralwidget.setObjectName("centralwidget")
		self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
		self.horizontalLayout.setObjectName("horizontalLayout")

		self.itemMenu = QtWidgets.QWidget(self.centralwidget)
		self.itemMenu.setObjectName("itemMenu")

		iteration = 1
		

		for data in data_list:
			self.__template = QtWidgets.QWidget(self.itemMenu)
			if iteration == 1:
				self.__template.setGeometry(QtCore.QRect(10, 90, 762, 80))
			else:
				self.__template.setGeometry(QtCore.QRect(10, (90 * iteration), 762, 80))

			self.__template.setObjectName("__template")
			self.itemName = QtWidgets.QLabel(self.__template)
			self.itemName.setGeometry(QtCore.QRect(10, 15, 620, 51))

			font = QtGui.QFont()
			font.setFamily("Futura PT Bold")
			font.setPointSize(26)
			font.setBold(True)
			font.setWeight(75)

			self.itemName.setFont(font)
			self.itemName.setAlignment(QtCore.Qt.AlignLeft)
			self.itemName.setObjectName("itemName")


			# If there is a way to cache the image from the link then this would be where you can set it.

			# self.itemImage = QtWidgets.QLabel(self.__template)
			# self.itemImage.setGeometry(QtCore.QRect(0, 0, 91, 81))
			# self.itemImage.setText("")
			# self.itemImage.setScaledContents(True)
			# self.itemImage.setObjectName("itemImage")
			# self.itemImage.setPixmap(QtGui.QPixmap("defaultHat.png"))

			self.button = QtWidgets.QPushButton(self.__template)
			self.button.setGeometry(QtCore.QRect(660, 20, 81, 41))
			font = QtGui.QFont()
			font.setFamily("Futura PT")
			font.setPointSize(10)
			font.setBold(True)
			font.setWeight(75)
			self.button.setFont(font)
			self.button.setObjectName(data['message'])
			
			self.urls.append(data["url"])
			self.buttons.append(self.button)

			self.horizontalLayout.addWidget(self.itemMenu)
			MainWindow.setCentralWidget(self.centralwidget)
			QtCore.QMetaObject.connectSlotsByName(MainWindow)

			_translate = QtCore.QCoreApplication.translate
			MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
			
			self.itemName.setText(_translate("MainWindow", data['message']))
			
			self.button.setText(_translate("MainWindow", "Open"))

			iteration += 1

	def setupButton(self, data_list):
		# I know how bad this is but I've spent over an hour trying to get it to work with for loops,
		# and it was still getting the same URL each time
		self.buttons[0].clicked.connect(lambda: webbrowser.open(self.urls[0]))
		self.buttons[1].clicked.connect(lambda: webbrowser.open(self.urls[1]))
		self.buttons[2].clicked.connect(lambda: webbrowser.open(self.urls[2]))
		self.buttons[3].clicked.connect(lambda: webbrowser.open(self.urls[3]))
		self.buttons[4].clicked.connect(lambda: webbrowser.open(self.urls[4]))
		self.buttons[5].clicked.connect(lambda: webbrowser.open(self.urls[5]))
		self.buttons[6].clicked.connect(lambda: webbrowser.open(self.urls[6]))
		self.buttons[7].clicked.connect(lambda: webbrowser.open(self.urls[7]))
		self.buttons[8].clicked.connect(lambda: webbrowser.open(self.urls[8]))
		self.buttons[9].clicked.connect(lambda: webbrowser.open(self.urls[9]))



		

