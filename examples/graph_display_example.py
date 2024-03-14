# -*- coding: utf-8 -*-
"""
Example QT GUI Showing use of ImageDisplayQT Widget to show a simple graph.

@author: Mike Hughes, Applied Optics Group, Physics & Astronomy, University of Kent


"""

import sys 
import os

import numpy as np
from PIL import Image
from pathlib import Path

from PyQt5 import QtGui, QtCore, QtWidgets  
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPalette, QColor, QImage, QPixmap, QPainter, QPen, QGuiApplication
from PyQt5.QtGui import QPainter, QBrush, QPen

sys.path.append(os.path.abspath("../src"))
from image_display import ImageDisplay


class ImageDisplayExample(QMainWindow):
    
    authorName = "MikeHughes"
    appName = "GraphDisplayExample"
             
    # Gui display defaults
    imageDisplaySize = 300
    controlPanelSize = 220
    
    # Timer interval defualts (ms)
    GUIupdateInterval = 1
        
    currentImage = None
    imageBuffer = None
    currentImageNum = 0 
    GUITimer = None
    currentGraph = None
    
    phase = 0
    
    
    def __init__(self,parent=None):    
        
        super(ImageDisplayExample, self).__init__(parent)
        self.create_layout() 
        self.update_display_settings()

        # Load in a stack of test images to simulated a live feed. Use a timer
        # to move through the stack, updating the image display
        self.GUITimer=QTimer()
        self.GUITimer.timeout.connect(self.handle_graph)
        self.GUITimer.start(self.GUIupdateInterval)
   
    
    def closeEvent(self, event):
        """ Called when main window closed
        """ 
        if self.GUITimer is not None:
            self.GUITimer.stop()
                
        
    def create_layout(self):
        """ Asemble the GUI from Qt Widgets
        """
        
        self.setWindowTitle('ImageDisplayQT: Example')       

        self.layout = QHBoxLayout()
        self.layout.setSpacing(20) 
        self.mainDisplayLayout = QVBoxLayout()      
        
        # Create the ImageDisplay widget 
        self.mainDisplay = ImageDisplay(name = "mainDisplay")
        
        # Add the ImageDisplay to the layout
        self.mainDisplayLayout.addWidget(self.mainDisplay)        
        self.layout.addLayout(self.mainDisplayLayout)
        
        # Create the panel with controls
        self.controlsLayout = QVBoxLayout()         
        self.waveSpeedSpin = QDoubleSpinBox()
        self.wavelengthSpin = QDoubleSpinBox()
        self.wavelengthSpin.setMinimum(1)
        self.offsetSpin = QDoubleSpinBox()
        self.controlsLayout.addWidget(QLabel("Num. Waves"))
        self.controlsLayout.addWidget(self.wavelengthSpin)
        self.controlsLayout.addWidget(QLabel("Speed"))
        self.controlsLayout.addWidget(self.waveSpeedSpin)
        self.controlsLayout.addWidget(QLabel("Vertical Offset"))

        self.controlsLayout.addWidget(self.offsetSpin)

        self.controlsLayout.addStretch()        
        
        
        kentlogo = QLabel()
        pixmap = QPixmap('../res/kent_logo_2.png')
        kentlogo.setPixmap(pixmap)
        self.controlsLayout.addWidget(kentlogo)
       
        self.layout.addLayout(self.controlsLayout)           
        app = QWidget()
        app.setLayout(self.layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(app)
        
        
    
    
    def update_gui(self):
        """ Updates the image display by setting the current image of the ImageDisplay widget
        """
        self.mainDisplay.set_graph(self.currentGraph)
        

    def update_display_settings(self):
        """ Updates the ImageDisplay settings based in GUI options selected"""

        pass

    
    def handle_graph(self):
        """ Called regularly by a timer to update graph. """
        
        pts = np.linspace(0, 1, 1024)

        self.phase = self.phase + .002 * self.waveSpeedSpin.value()

        self.currentGraph = self.offsetSpin.value() + np.sin(2 * np.pi * (pts * self.wavelengthSpin.value() + self.phase))
                
        self.update_gui()
    

    

if __name__ == '__main__':
    
   app=QApplication(sys.argv)
   app.setStyle("Fusion")
   
   # Now use a palette to switch to dark colors:
   palette = QPalette()
   palette.setColor(QPalette.Window, QColor(53, 53, 53))
   palette.setColor(QPalette.Window, QColor(0, 0, 0))

   palette.setColor(QPalette.WindowText, Qt.white)
   palette.setColor(QPalette.Base, QColor(55, 45, 45))
   palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
   palette.setColor(QPalette.ToolTipBase, Qt.black)
   palette.setColor(QPalette.ToolTipText, Qt.white)
   palette.setColor(QPalette.Text, Qt.white)
   palette.setColor(QPalette.Button, QColor(53, 53, 53))
   palette.setColor(QPalette.Button, QColor(63, 63, 63))

   palette.setColor(QPalette.ButtonText, Qt.white)
   palette.setColor(QPalette.BrightText, Qt.red)
   palette.setColor(QPalette.Link, QColor(42, 130, 218))
   palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
   palette.setColor(QPalette.HighlightedText, Qt.black)
   app.setPalette(palette)
   
   window=ImageDisplayExample()
   window.show()
   sys.exit(app.exec_())

