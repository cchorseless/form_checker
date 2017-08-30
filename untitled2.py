# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled2.ui'
#
# Created by: PyQt5 UI code generator 5.8
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 480)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(200, 110, 181, 81))
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(180, 240, 256, 192))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton.clicked.connect(self.msg)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "PushButton"))

    def msg(self):
        filepath,filetype = QtWidgets.QFileDialog.getOpenFileName(caption='fafffff',
                                                         directory='c:',
                                                         filter='All Files (*);;EXCEL文件 (*.xlsx)')
        self.textBrowser.setHtml(filepath)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)  # 注册UI界面
    aaa = QtWidgets.QWidget()  # 实例化UI界面
    ui = Ui_Form()  # 实例化对象
    ui.setupUi(aaa)  # 对象处理UI界面
    aaa.show()
    sys.exit(app.exec_())  # 保持界面不退出，接受指令退出
