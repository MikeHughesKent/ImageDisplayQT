# -*- coding: utf-8 -*-
"""
Example QT GUI Showing use of ImageDisplay Widget.

@author: Mike Hughes
Applied Optics Group
University of Kent

"""

import sys 
import os

import numpy as np
from PIL import Image

from PyQt5 import QtGui, QtCore, QtWidgets  
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPalette, QColor, QImage, QPixmap, QPainter, QPen, QGuiApplication
from PyQt5.QtGui import QPainter, QBrush, QPen

sys.path.append(os.path.abspath("..\\src"))
from image_display import ImageDisplay


class ImageDisplayExample(QMainWindow):
    
    authorName = "AOG"
    appName = "ImageDisplayExample"
    
    # Images to display
    imageSource = "example_mono8.tif"
    
    # Will loop through this number of images
    numImages = 10        
         
    # Gui display defaults
    imageDisplaySize = 300
    controlPanelSize = 220
    
    # Timer interval defualts (ms)
    GUIupdateInterval = 50
    imagesUpdateInterval = 1
        
    currentImage = None
    imageBuffer = None
    currentImageNum = 0 
    GUITimer = None
    
    
    def __init__(self,parent=None):    
        
        super(ImageDisplayExample, self).__init__(parent)

        self.create_layout() 
        self.update_display_settings()

        # Load in a stack of test images to simulated a live feed. Use a timer
        # to move through the stack, updating the image display
        self.imageBuffer = self.load_images(self.imageSource, self.numImages)
        self.GUITimer=QTimer()
        self.GUITimer.timeout.connect(self.handle_images)
        self.GUITimer.start(self.GUIupdateInterval)
   
    
    def closeEvent(self, event):
        """ Called when main window closed
        """ 
        if self.GUITimer is not None:
            self.GUITimer.stop()
                
        
    def create_layout(self):
        """ Asemble the GUI from Qt Widgets
        """
        
        self.setWindowTitle('Image Display Example')       

        self.layout = QHBoxLayout()
        self.mainDisplayLayout = QVBoxLayout()      
        
        # Create the ImageDisplay widget 
        self.mainDisplay = ImageDisplay(name = "mainDisplay")
        
        # Add the ImageDisplay to the layout
        self.mainDisplayLayout.addWidget(self.mainDisplay)        
        self.layout.addLayout(self.mainDisplayLayout)
        
        # Create the panel with controls
        self.controlsLayout = QVBoxLayout()        
        self.showRectangleCheck = QCheckBox('Show rectangular overlay')
        self.controlsLayout.addWidget(self.showRectangleCheck)
        self.showRectangleCheck.stateChanged.connect(self.update_display_settings)        
        self.showEllipseCheck = QCheckBox('Show Ellipse overlay')
        self.controlsLayout.addWidget(self.showEllipseCheck)
        self.showEllipseCheck.stateChanged.connect(self.update_display_settings)        
        self.showLineCheck = QCheckBox('Show line overlay')
        self.controlsLayout.addWidget(self.showLineCheck)
        self.showLineCheck.stateChanged.connect(self.update_display_settings)        
        self.showPointsCheck = QCheckBox('Show point overlays')
        self.controlsLayout.addWidget(self.showPointsCheck)
        self.showPointsCheck.stateChanged.connect(self.update_display_settings)        
        self.showTextCheck = QCheckBox('Show text overlay')
        self.controlsLayout.addWidget(self.showTextCheck)
        self.showTextCheck.stateChanged.connect(self.update_display_settings)        
        self.showStatusCheck = QCheckBox('Show status bar')
        self.controlsLayout.addWidget(self.showStatusCheck)
        self.showStatusCheck.stateChanged.connect(self.update_display_settings)        
        self.allowZoomCheck = QCheckBox('Allow zoom')
        self.controlsLayout.addWidget(self.allowZoomCheck)
        self.allowZoomCheck.stateChanged.connect(self.update_display_settings)        
        self.allowROICheck = QCheckBox('Allow ROI')
        self.controlsLayout.addWidget(self.allowROICheck)
        self.allowROICheck.stateChanged.connect(self.update_display_settings)
        self.autoscaleCheck = QCheckBox('Autoscale')
        self.controlsLayout.addWidget(self.autoscaleCheck)
        self.autoscaleCheck.stateChanged.connect(self.update_display_settings)
       
        self.controlsLayout.addStretch()
        
        self.layout.addLayout(self.controlsLayout)   
        
        app = QWidget()
        app.setLayout(self.layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(app)
        
        
    def load_images(self, filename, numToLoad ):
        """ Loads a stack of images into memmory from tif.
        """            
        dataset = Image.open(filename)
        h = np.shape(dataset)[0]
        w = np.shape(dataset)[1]    
        imageBuffer = np.zeros((h,w,dataset.n_frames))
        
        for i in range(min(dataset.n_frames, numToLoad)):
            dataset.seek(i)
            imageBuffer[:,:,i] = np.array(dataset).astype('double')
        dataset.close() 

        return imageBuffer

    
    def update_gui(self):
        """ Updates the image display by setting the current image of the ImageDisplay widget
        """
        self.mainDisplay.set_mono_image(self.currentImage)
        

    def update_display_settings(self):
        """ Updates the ImageDisplay settings based in GUI options selected"""

        self.mainDisplay.set_status_bar(self.showStatusCheck.isChecked())
        self.mainDisplay.set_zoom_enabled(self.allowZoomCheck.isChecked())
        self.mainDisplay.set_roi_enabled(self.allowROICheck.isChecked())
        self.mainDisplay.set_auto_scale(self.autoscaleCheck.isChecked())

        
        # Overlays
        self.mainDisplay.clear_overlays()
        if self.showLineCheck.isChecked():
            lineOverlay = self.mainDisplay.add_overlay(ImageDisplay.LINE, 140, 70, 230, 420, QPen(Qt.red, 2, Qt.SolidLine))
        if self.showRectangleCheck.isChecked():
            rectOverlay = self.mainDisplay.add_overlay(ImageDisplay.RECTANGLE, 90, 100, 30, 40, QPen(Qt.blue, 2, Qt.SolidLine), None)
        if self.showEllipseCheck.isChecked():
            ellipseOverlay = self.mainDisplay.add_overlay(ImageDisplay.ELLIPSE, 180, 70, 90, 90, QPen(Qt.green, 2, Qt.SolidLine), None)
        if self.showPointsCheck.isChecked():
            pointOverlay1 = self.mainDisplay.add_overlay(ImageDisplay.POINT, 180, 50, QPen(Qt.yellow, 2, Qt.SolidLine), None)
            pointOverlay2 = self.mainDisplay.add_overlay(ImageDisplay.POINT, 200, 200, QPen(Qt.yellow, 2, Qt.SolidLine), None)
        if self.showTextCheck.isChecked():
            textOverlay = self.mainDisplay.add_overlay(ImageDisplay.TEXT, 180, 50, QPen(Qt.yellow, 2, Qt.SolidLine), "Example Label")


    
    def handle_images(self):
        """ Called regularly by a timer to deal with input images. If a processor
        is defined by the sub-class, this will handle processing. Overload for
        a custom processing pipeline"""
        
        # Grab the next image from the buffer
        self.currentImageNum = self.currentImageNum + 1
        self.currentImageNum = np.remainder(self.currentImageNum, self.numImages)
        self.currentImage = self.imageBuffer[:,:,self.currentImageNum]
                
        self.update_gui()
    

    

if __name__ == '__main__':
    
   app=QApplication(sys.argv)
   app.setStyle("Fusion")

   #Now use a palette to switch to dark colors:
   palette = QPalette()
   palette.setColor(QPalette.Window, QColor(53, 53, 53))
   palette.setColor(QPalette.WindowText, Qt.white)
   palette.setColor(QPalette.Base, QColor(25, 25, 25))
   palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
   palette.setColor(QPalette.ToolTipBase, Qt.black)
   palette.setColor(QPalette.ToolTipText, Qt.white)
   palette.setColor(QPalette.Text, Qt.white)
   palette.setColor(QPalette.Button, QColor(53, 53, 53))
   palette.setColor(QPalette.ButtonText, Qt.white)
   palette.setColor(QPalette.BrightText, Qt.red)
   palette.setColor(QPalette.Link, QColor(42, 130, 218))
   palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
   palette.setColor(QPalette.HighlightedText, Qt.black)
   palette.setColor(QPalette.Disabled, QPalette.Light, Qt.black)
   palette.setColor(QPalette.Disabled, QPalette.Shadow, QColor(12, 15, 16))
   
   app.setPalette(palette)  
   
   window=ImageDisplayExample()
   window.show()
   sys.exit(app.exec_())

