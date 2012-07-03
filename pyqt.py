import sys
from PyQt4 import QtGui

app = QtGui.QApplication(sys.argv)

widget = QtGui.QWidget()
widget.setWindowTitle('simple')
widget.show()

sys.exit(app.exec_())