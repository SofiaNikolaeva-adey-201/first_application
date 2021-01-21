from PyQt5 import uic
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QApplication

Form, Window = uic.loadUiType("tracker.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()

def on_click():
    print(form.plainTextEdit.toPlainText())
    print(form.dateEdit.dateTime().toString('dd-MM-yyyy'))
    print("Clicked!")
    print(form.calendarWidget.selectedDate().toString('dd-MM-yyyy'))
    date = QDate(2022, 9, 17)
    form.calendarWidget.setSelectedDate(date)


form.pushButton.clicked.connect(on_click)


app.exec_()
