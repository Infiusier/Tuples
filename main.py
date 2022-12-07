import sys,argparse
from os import environ
from PySide2 import QtWidgets
import MainWindow
import linsimpy
tse = linsimpy.TupleSpaceEnvironment()
def main():
     
    app=QtWidgets.QApplication(sys.argv)
    ui=MainWindow.MainWindow()
    ui.show()
    sys.exit(app.exec_())   

if __name__ == "__main__":
    main()