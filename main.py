'''
	Name : main.py
	Author: Eric Stalcup
	Created : 11/17/2021
	Course: CIS 152 - Data Structure
	Version: 1.0
	OS: Windows 10
	IDE: Visual Studio Code 1.61.2
	Copyright : This is my own original work 
	based on specifications issued by our instructor
	
	Description : This should be the only file that need to get called by the interpreter 
	to run the entire project. It is the entry point of the project. This file manages 
	all of the other classes, and gives the user interface the data it needs to work with.
	
	Academic Honesty: I attest that this is my original work.
	I have not used unauthorized source code, either modified or
	unmodified. I have not given other fellow student(s) access
	to my program.
'''

from PyQt5 import QtCore, QtGui, QtWidgets
from get_data import ItemData
from items_ui import ItemWindow

# Get the data from an object
item_data = ItemData()
data_list = item_data.get_item_data()

if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = ItemWindow()
	ui.setupUi(MainWindow, data_list)
	ui.setupButton(data_list)
	MainWindow.show()
	sys.exit(app.exec_())

# print(item_dict)
