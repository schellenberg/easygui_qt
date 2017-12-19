
try:
    from PyQt5 import QtGui, QtCore, QtWidgets
except ImportError:
    print("Error importing PyQt5. Have you installed it?")
    
class CalendarWidget(QtWidgets.QWidget):
    """Creates a calendar widget allowing the user to select a date."""
    def __init__(self, title="Calendar"):
        super(CalendarWidget, self).__init__()

        self.setWindowTitle(title)
        layout = QtWidgets.QGridLayout()
        layout.setColumnStretch(1, 1)

        self.cal = QtWidgets.QCalendarWidget(self)
        self.cal.setGridVisible(True)
        self.cal.clicked[QtCore.QDate].connect(self.show_date)
        layout.addWidget(self.cal, 0, 0, 1, 2)

        self.date_label = QtWidgets.QLabel()
        self.date = self.cal.selectedDate()
        self.date_label.setText(self.date.toString())
        layout.addWidget(self.date_label, 1, 0)

        button_box = QtWidgets.QDialogButtonBox()
        confirm_button = button_box.addButton(QtWidgets.QDialogButtonBox.Ok)
        confirm_button.clicked.connect(self.confirm)
        layout.addWidget(button_box, 1, 1)

        self.setLayout(layout)
        self.show()
        self.raise_()

    def show_date(self, date):
        self.date = self.cal.selectedDate()
        self.date_label.setText(self.date.toString())

    def confirm(self):
        self.date = self.cal.selectedDate()
        self.close()

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication([])
    cal = CalendarWidget(title="title")
    app.exec_()
    date = cal.date.toString()
    if sys.version_info < (3,):
        print(unicode(date))
    print(date)