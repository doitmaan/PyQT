import sys
from PyQt5.QtWidgets import QDialog, QApplication
from demoLineEdit import *
class MyForm(QDialog):

	def dispmessage(self):
		self.ui.LabelResponse.setText("Hello "
		+self.ui.lineEditName.text())


	def __init__(self):
		super().__init__()
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)
		self.ui.ButtonClickMe.clicked.connect(self.dispmessage)
		self.show()
	
if __name__=="__main__":

	app = QApplication(sys.argv)
	w = MyForm()
	w.show()
	sys.exit(app.exec_())