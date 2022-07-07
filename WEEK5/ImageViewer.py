from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QApplication
import matplotlib.pyplot as plt
import sys
import os

class Ui_imageViewer(object):
    def setupUi(self, imageViewer):
        imageViewer.setObjectName("imageViewer")
        imageViewer.resize(800, 580)
        imageViewer.setMinimumSize(QtCore.QSize(800, 580))
        imageViewer.setMaximumSize(QtCore.QSize(800, 580))
        self.centralwidget = QtWidgets.QWidget(imageViewer)
        self.centralwidget.setObjectName("centralwidget")


    def open_directory_callback(self):

        # Paths
        self._base_dir = os.getcwd()
        self._images_dir = os.path.join(self._base_dir, 'test_images')

        # Open a File Dialog and select the folder path
        dialog = QFileDialog()
        self._folder_path = dialog.getExistingDirectory(None, "Select Folder")

        # Get the list of images in the folder and read using matplotlib and print its shape
        self.list_of_images = os.listdir(self._folder_path)
        self.list_of_images = sorted(self.list_of_images)

        # Length of Images
        print('Number of Images in the selected folder: {}'.format(len(self.list_of_images)))
        input_img_raw_string = '{}\\{}'.format(self._images_dir, self.list_of_images[0])

        # Show the first Image in the same window. (self.label comes from the Ui_main_window class)
        self.label.setPixmap(QtGui.QPixmap(input_img_raw_string))
        self.label.show()

        self.i = 0

    def next_button_callback(self):

        # Total Images in List
        total_images = len(self.list_of_images)

        if self.list_of_images:
            try:
                self.i = (self.i + 1) % total_images
                img = self.list_of_images[self.i]
                self.label.setPixmap(QtGui.QPixmap('{}\\{}'.format(self._images_dir, img)))
                self.label.show()

            except ValueError as e:
                print('The selected folder does not contain any images')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    imageViewer = QtWidgets.QMainWindow()
    ui = Ui_imageViewer()
    ui.setupUi(imageViewer)
    imageViewer.show()
    sys.exit(app.exec_())

