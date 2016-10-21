import sys
import numpy as np

from PyQt5.QtWidgets import (QApplication, QDialog, QLineEdit, QVBoxLayout,
                             QMainWindow, QAction, QFileDialog)

from mplcanvas import MatplotlibCanvas

class MainWindow(QMainWindow) :
    
    def __init__(self, parent=None) :
        super(MainWindow, self).__init__(parent)
    
        # Create the file menu
        self.menuFile = self.menuBar().addMenu("&File")
        self.actionSaveAs = QAction("&Save As", self)
        self.actionSaveAs.triggered.connect(self.saveas)
        self.actionQuit = QAction("&Quit", self)
        self.actionQuit.triggered.connect(self.close)
        self.menuFile.addActions([self.actionSaveAs, self.actionQuit])
        
        # Set the central widget
        widget = Form()
        self.setCentralWidget(widget)
    
    def saveas(self) :
        """ Save the computed data as a text file. """
        fname = unicode(QFileDialog.getSaveFileName(self, "Save as..."))
        if fname :
            pass        
                
class Form(QDialog) :

    def __init__(self, parent=None) :
        super(Form, self).__init__(parent)

        # Define three text boxes.
        self.function_edit = QLineEdit("f(x) = ...")
        self.function_edit.selectAll() 
        self.value_edit = QLineEdit("x = ...")
        self.value_edit.selectAll()
        self.output_edit = QLineEdit(" ")
        self.output_edit.selectAll()

        # Define the plot widget
        self.plot = MatplotlibCanvas() 
        
        # Define the layout
        layout = QVBoxLayout()
        layout.addWidget(self.plot)
        layout.addWidget(self.function_edit)
        layout.addWidget(self.value_edit)
        layout.addWidget(self.output_edit)
        self.setLayout(layout)

        # Connect our output box to the update function
        self.output_edit.returnPressed.connect(self.updateUI) 

    def updateUI(self) :
        """ Method for updating the user interface"""
        p = self.function_edit.text()
        s = self.value_edit.text()
        x = float(s) 
        y = eval(p)
        self.output_edit.setText(str(y))

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    app.exec_()
