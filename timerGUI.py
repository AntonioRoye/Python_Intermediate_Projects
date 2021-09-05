from PyQt6 import QtCore, QtGui, QtWidgets
import timer
import threading
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        self.newTimer = timer.Timer()
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(401, 249)
        Dialog.setMinimumSize(QtCore.QSize(401, 249))
        Dialog.setMaximumSize(QtCore.QSize(401, 249))
        Dialog.setMouseTracking(False)
        Dialog.setAutoFillBackground(False)
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 20, 381, 87))
        self.widget.setObjectName("widget")
        self.timeLabelGroup = QtWidgets.QHBoxLayout(self.widget)
        self.timeLabelGroup.setContentsMargins(0, 0, 0, 0)
        self.timeLabelGroup.setObjectName("timeLabelGroup")
        self.dayLabel = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(48)
        self.dayLabel.setFont(font)
        self.dayLabel.setScaledContents(False)
        self.dayLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.dayLabel.setObjectName("dayLabel")
        self.timeLabelGroup.addWidget(self.dayLabel)
        self.colon1 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(48)
        self.colon1.setFont(font)
        self.colon1.setScaledContents(False)
        self.colon1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.colon1.setObjectName("colon1")
        self.timeLabelGroup.addWidget(self.colon1)
        self.hourLabel = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(48)
        self.hourLabel.setFont(font)
        self.hourLabel.setScaledContents(False)
        self.hourLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.hourLabel.setObjectName("hourLabel")
        self.timeLabelGroup.addWidget(self.hourLabel)
        self.colon2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(48)
        self.colon2.setFont(font)
        self.colon2.setScaledContents(False)
        self.colon2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.colon2.setObjectName("colon2")
        self.timeLabelGroup.addWidget(self.colon2)
        self.minuteLabel = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(48)
        self.minuteLabel.setFont(font)
        self.minuteLabel.setScaledContents(False)
        self.minuteLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.minuteLabel.setObjectName("minuteLabel")
        self.timeLabelGroup.addWidget(self.minuteLabel)
        self.colon3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(48)
        self.colon3.setFont(font)
        self.colon3.setScaledContents(False)
        self.colon3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.colon3.setObjectName("colon3")
        self.timeLabelGroup.addWidget(self.colon3)
        self.secondLabel = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(48)
        self.secondLabel.setFont(font)
        self.secondLabel.setScaledContents(False)
        self.secondLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.secondLabel.setObjectName("secondLabel")
        self.timeLabelGroup.addWidget(self.secondLabel)
        self.widget1 = QtWidgets.QWidget(Dialog)
        self.widget1.setGeometry(QtCore.QRect(10, 139, 381, 26))
        self.widget1.setObjectName("widget1")
        self.spinBoxGroup = QtWidgets.QHBoxLayout(self.widget1)
        self.spinBoxGroup.setContentsMargins(0, 0, 0, 0)
        self.spinBoxGroup.setObjectName("spinBoxGroup")
        self.daySpinBox = QtWidgets.QSpinBox(self.widget1)
        self.daySpinBox.setObjectName("daySpinBox")
        self.spinBoxGroup.addWidget(self.daySpinBox)
        self.hourSpinBox = QtWidgets.QSpinBox(self.widget1)
        self.hourSpinBox.setMaximum(23)
        self.hourSpinBox.setObjectName("hourSpinBox")
        self.spinBoxGroup.addWidget(self.hourSpinBox)
        self.minuteSpinBox = QtWidgets.QSpinBox(self.widget1)
        self.minuteSpinBox.setMaximum(59)
        self.minuteSpinBox.setObjectName("minuteSpinBox")
        self.spinBoxGroup.addWidget(self.minuteSpinBox)
        self.secondSpinBox = QtWidgets.QSpinBox(self.widget1)
        self.secondSpinBox.setMaximum(59)
        self.secondSpinBox.setObjectName("secondSpinBox")
        self.spinBoxGroup.addWidget(self.secondSpinBox)
        self.widget2 = QtWidgets.QWidget(Dialog)
        self.widget2.setGeometry(QtCore.QRect(20, 173, 381, 24))
        self.widget2.setObjectName("widget2")
        self.spinBoxLabelsGroup = QtWidgets.QHBoxLayout(self.widget2)
        self.spinBoxLabelsGroup.setContentsMargins(0, 0, 0, 0)
        self.spinBoxLabelsGroup.setObjectName("spinBoxLabelsGroup")
        self.spinBoxDayLabel = QtWidgets.QLabel(self.widget2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.spinBoxDayLabel.setFont(font)
        self.spinBoxDayLabel.setObjectName("spinBoxDayLabel")
        self.spinBoxLabelsGroup.addWidget(self.spinBoxDayLabel)
        self.spinBoxHoursLabel = QtWidgets.QLabel(self.widget2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.spinBoxHoursLabel.setFont(font)
        self.spinBoxHoursLabel.setObjectName("spinBoxHoursLabel")
        self.spinBoxLabelsGroup.addWidget(self.spinBoxHoursLabel)
        self.spinBoxMinutesLabel = QtWidgets.QLabel(self.widget2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.spinBoxMinutesLabel.setFont(font)
        self.spinBoxMinutesLabel.setObjectName("spinBoxMinutesLabel")
        self.spinBoxLabelsGroup.addWidget(self.spinBoxMinutesLabel)
        self.spinBoxSecondsLabel = QtWidgets.QLabel(self.widget2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.spinBoxSecondsLabel.setFont(font)
        self.spinBoxSecondsLabel.setObjectName("spinBoxSecondsLabel")
        self.spinBoxLabelsGroup.addWidget(self.spinBoxSecondsLabel)
        self.widget3 = QtWidgets.QWidget(Dialog)
        self.widget3.setGeometry(QtCore.QRect(90, 210, 231, 32))
        self.widget3.setObjectName("widget3")
        self.pushButtonsGroup = QtWidgets.QHBoxLayout(self.widget3)
        self.pushButtonsGroup.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.pushButtonsGroup.setContentsMargins(0, 0, 0, 0)
        self.pushButtonsGroup.setObjectName("pushButtonsGroup")
        self.startPushButton = QtWidgets.QPushButton(self.widget3)
        self.startPushButton.setObjectName("startPushButton")
        self.pushButtonsGroup.addWidget(self.startPushButton)
        self.stopPushButton = QtWidgets.QPushButton(self.widget3)
        self.stopPushButton.setObjectName("stopPushButton")
        self.pushButtonsGroup.addWidget(self.stopPushButton)
        self.exitPushButton = QtWidgets.QPushButton(self.widget3)
        self.exitPushButton.setObjectName("exitPushButton")
        self.pushButtonsGroup.addWidget(self.exitPushButton)
        self.dayLabel.setBuddy(self.dayLabel)
        self.colon1.setBuddy(self.dayLabel)
        self.hourLabel.setBuddy(self.dayLabel)
        self.colon2.setBuddy(self.dayLabel)
        self.minuteLabel.setBuddy(self.dayLabel)
        self.colon3.setBuddy(self.dayLabel)
        self.secondLabel.setBuddy(self.dayLabel)

        self.retranslateUi(Dialog)
        self.daySpinBox.valueChanged.connect(lambda: self.spinBoxClicked(self.daySpinBox))
        self.hourSpinBox.valueChanged.connect(lambda: self.spinBoxClicked(self.hourSpinBox))
        self.minuteSpinBox.valueChanged.connect(lambda: self.spinBoxClicked(self.minuteSpinBox))
        self.secondSpinBox.valueChanged.connect(lambda: self.spinBoxClicked(self.secondSpinBox))
        self.exitPushButton.clicked.connect(self.exit)
        self.startPushButton.clicked.connect(lambda: threading.Thread(target=self.startTimer_mainLoop, daemon=True).start())
        self.stopPushButton.clicked.connect(lambda: self.stopTimer())
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.daySpinBox, self.hourSpinBox)
        Dialog.setTabOrder(self.hourSpinBox, self.minuteSpinBox)
        Dialog.setTabOrder(self.minuteSpinBox, self.secondSpinBox)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Timer"))
        self.dayLabel.setText(_translate("Dialog", " 0 "))
        self.colon1.setText(_translate("Dialog", ":"))
        self.hourLabel.setText(_translate("Dialog", " 0 "))
        self.colon2.setText(_translate("Dialog", ":"))
        self.minuteLabel.setText(_translate("Dialog", " 0 "))
        self.colon3.setText(_translate("Dialog", ":"))
        self.secondLabel.setText(_translate("Dialog", " 0 "))
        self.spinBoxDayLabel.setText(_translate("Dialog", "Days"))
        self.spinBoxHoursLabel.setText(_translate("Dialog", "Hours"))
        self.spinBoxMinutesLabel.setText(_translate("Dialog", "Minutes"))
        self.spinBoxSecondsLabel.setText(_translate("Dialog", "Seconds"))
        self.startPushButton.setText(_translate("Dialog", "Start"))
        self.stopPushButton.setText(_translate("Dialog", "Stop"))
        self.exitPushButton.setText(_translate("Dialog", "Exit"))
        
    def spinBoxClicked(self, spinBox):
        if spinBox.objectName() == "daySpinBox":
            self.dayLabel.setText(str(spinBox.value()))
        elif spinBox.objectName() == "hourSpinBox":
            self.hourLabel.setText(str(spinBox.value()))
        elif spinBox.objectName() == "minuteSpinBox":
            self.minuteLabel.setText(str(spinBox.value()))
        else:
            self.secondLabel.setText(str(spinBox.value()))
    
    def startTimer_mainLoop(self):
        self.newTimer.setDays(int(self.dayLabel.text()))
        self.newTimer.setHours(int(self.hourLabel.text()))
        self.newTimer.setMinutes(int(self.minuteLabel.text()))
        self.newTimer.setSeconds(int(self.secondLabel.text()))
        self.newTimer.isStopped = False
        self.newTimer.isDone = False
        while True:
            if self.newTimer.isDone == True:
                print("Finised")
                #NEED A MESSAGE TO PRINT HERE
                break
            if self.newTimer.isStopped == True:
                break
            self.newTimer.main()
            self.dayLabel.setText(str(self.newTimer.getDays()))
            self.hourLabel.setText(str(self.newTimer.getHours()))
            self.minuteLabel.setText(str(self.newTimer.getMinutes()))
            self.secondLabel.setText(str(self.newTimer.getSeconds()))
        
            
    def stopTimer(self):
        self.newTimer.isStopped = True 
        
    def exit(self):
        Dialog.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
