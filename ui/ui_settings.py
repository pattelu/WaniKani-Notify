# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Settings(object):
    def setupUi(self, Settings):
        if not Settings.objectName():
            Settings.setObjectName(u"Settings")
        Settings.resize(475, 123)
        Settings.setMaximumSize(QSize(500, 150))
        icon = QIcon()
        icon.addFile(u"../img/icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Settings.setWindowIcon(icon)
        self.verticalLayout_2 = QVBoxLayout(Settings)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_api = QLabel(Settings)
        self.label_api.setObjectName(u"label_api")

        self.horizontalLayout.addWidget(self.label_api)

        self.text_api = QLineEdit(Settings)
        self.text_api.setObjectName(u"text_api")

        self.horizontalLayout.addWidget(self.text_api)

        self.btn_test = QPushButton(Settings)
        self.btn_test.setObjectName(u"btn_test")

        self.horizontalLayout.addWidget(self.btn_test)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.label_info = QLabel(Settings)
        self.label_info.setObjectName(u"label_info")
        self.label_info.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_info)

        self.line = QFrame(Settings)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_quit = QPushButton(Settings)
        self.btn_quit.setObjectName(u"btn_quit")

        self.horizontalLayout_2.addWidget(self.btn_quit)

        self.btn_save = QPushButton(Settings)
        self.btn_save.setObjectName(u"btn_save")

        self.horizontalLayout_2.addWidget(self.btn_save)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Settings)

        QMetaObject.connectSlotsByName(Settings)
    # setupUi

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(QCoreApplication.translate("Settings", u"Settings - WaniKani Notify ", None))
        self.label_api.setText(QCoreApplication.translate("Settings", u"WaniKani API key", None))
        self.btn_test.setText(QCoreApplication.translate("Settings", u"Test API Key", None))
        self.label_info.setText("")
        self.btn_quit.setText(QCoreApplication.translate("Settings", u"Quit", None))
        self.btn_save.setText(QCoreApplication.translate("Settings", u"Save configuration", None))
    # retranslateUi

