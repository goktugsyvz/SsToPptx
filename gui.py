import sys
from PyQt5 import QtWidgets,QtGui
import pyautogui
from PIL.ImageQt import ImageQt
from PIL import Image

class Pencere(QtWidgets.QWidget):

	def __init_(self):
		QtWidgets.QWidget.__init__(self)
		self.setWindowTitle("asd")

	def home(self):
		self.setWindowTitle("Experimental Gui")
		self.h_box1 = QtWidgets.QHBoxLayout()
		self.v_box1 = QtWidgets.QVBoxLayout()
		self.v_box2 = QtWidgets.QVBoxLayout()

		self.btn = QtWidgets.QPushButton("this")	
		self.btn.clicked.connect(self.change)

		self.text = QtWidgets.QLabel("Latest screenshot")

		self.labelImage = QtWidgets.QLabel(self)	
		self.image = pyautogui.screenshot()
		self.image = resizeImage(self.image)
		self.qimage = ImageQt(self.image)
		self.pixmap = QtGui.QPixmap().fromImage(self.qimage)
		self.labelImage.setPixmap(self.pixmap)


		self.v_box1.addWidget(self.btn)
		self.v_box2.addWidget(self.text)
		self.v_box2.addWidget(self.labelImage)		
		self.h_box1.addLayout(self.v_box1)		
		self.h_box1.addLayout(self.v_box2)
		self.setLayout(self.h_box1)		
		
	def change(self,image):
		self.image = resizeImage(image)
		self.qimage = ImageQt(self.image)
		self.pixmap = QtGui.QPixmap().fromImage(self.qimage)
		self.labelImage.setPixmap(self.pixmap)
	

def main():
	print("start")
	app = QtWidgets.QApplication(sys.argv)
	pencerem = Pencere()
	pencerem.home()	
	pencerem.show()
	sys.exit(app.exec_())
	
def resizeImage(image,size=(1920,1080),scale=1/3):
	im = image.resize((int(size[0]*scale),int(size[1]*scale)),Image.ANTIALIAS)
	return im
main()

