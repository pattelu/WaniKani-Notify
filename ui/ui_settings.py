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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Settings(object):
    def setupUi(self, Settings):
        if not Settings.objectName():
            Settings.setObjectName(u"Settings")
        Settings.resize(500, 260)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Settings.sizePolicy().hasHeightForWidth())
        Settings.setSizePolicy(sizePolicy)
        Settings.setMaximumSize(QSize(500, 260))
        icon = QIcon()
        icon.addFile(u"../img/icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Settings.setWindowIcon(icon)
        self.verticalLayout_2 = QVBoxLayout(Settings)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
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


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.label_test_api = QLabel(Settings)
        self.label_test_api.setObjectName(u"label_test_api")
        self.label_test_api.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(30)
        sizePolicy1.setHeightForWidth(self.label_test_api.sizePolicy().hasHeightForWidth())
        self.label_test_api.setSizePolicy(sizePolicy1)
        self.label_test_api.setMaximumSize(QSize(16777215, 16777215))
        self.label_test_api.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_test_api)


        self.verticalLayout_2.addLayout(self.verticalLayout_3)

        self.line_2 = QFrame(Settings)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_notification = QLabel(Settings)
        self.label_notification.setObjectName(u"label_notification")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(20)
        sizePolicy2.setHeightForWidth(self.label_notification.sizePolicy().hasHeightForWidth())
        self.label_notification.setSizePolicy(sizePolicy2)
        self.label_notification.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout.addWidget(self.label_notification)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(20, -1, -1, -1)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.check_user_level = QCheckBox(Settings)
        self.check_user_level.setObjectName(u"check_user_level")

        self.horizontalLayout_9.addWidget(self.check_user_level)


        self.verticalLayout_4.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_lessons = QLabel(Settings)
        self.label_lessons.setObjectName(u"label_lessons")

        self.horizontalLayout_6.addWidget(self.label_lessons)

        self.check_l_radicals = QCheckBox(Settings)
        self.check_l_radicals.setObjectName(u"check_l_radicals")

        self.horizontalLayout_6.addWidget(self.check_l_radicals)

        self.check_l_kanji = QCheckBox(Settings)
        self.check_l_kanji.setObjectName(u"check_l_kanji")

        self.horizontalLayout_6.addWidget(self.check_l_kanji)

        self.check_l_vocabulary = QCheckBox(Settings)
        self.check_l_vocabulary.setObjectName(u"check_l_vocabulary")

        self.horizontalLayout_6.addWidget(self.check_l_vocabulary)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_reviews = QLabel(Settings)
        self.label_reviews.setObjectName(u"label_reviews")

        self.horizontalLayout_4.addWidget(self.label_reviews)

        self.check_r_radicals = QCheckBox(Settings)
        self.check_r_radicals.setObjectName(u"check_r_radicals")

        self.horizontalLayout_4.addWidget(self.check_r_radicals)

        self.check_r_kanji = QCheckBox(Settings)
        self.check_r_kanji.setObjectName(u"check_r_kanji")

        self.horizontalLayout_4.addWidget(self.check_r_kanji)

        self.check_r_vocabulary = QCheckBox(Settings)
        self.check_r_vocabulary.setObjectName(u"check_r_vocabulary")

        self.horizontalLayout_4.addWidget(self.check_r_vocabulary)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(15)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_srs = QLabel(Settings)
        self.label_srs.setObjectName(u"label_srs")

        self.horizontalLayout_7.addWidget(self.label_srs)

        self.combo_srs = QComboBox(Settings)
        self.combo_srs.addItem("")
        self.combo_srs.addItem("")
        self.combo_srs.addItem("")
        self.combo_srs.addItem("")
        self.combo_srs.addItem("")
        self.combo_srs.addItem("")
        self.combo_srs.addItem("")
        self.combo_srs.addItem("")
        self.combo_srs.setObjectName(u"combo_srs")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.combo_srs.sizePolicy().hasHeightForWidth())
        self.combo_srs.setSizePolicy(sizePolicy3)

        self.horizontalLayout_7.addWidget(self.combo_srs)


        self.verticalLayout_4.addLayout(self.horizontalLayout_7)


        self.verticalLayout.addLayout(self.verticalLayout_4)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.line = QFrame(Settings)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.label_info = QLabel(Settings)
        self.label_info.setObjectName(u"label_info")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_info.sizePolicy().hasHeightForWidth())
        self.label_info.setSizePolicy(sizePolicy4)
        self.label_info.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_info)

        self.btn_quit = QPushButton(Settings)
        self.btn_quit.setObjectName(u"btn_quit")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.btn_quit.sizePolicy().hasHeightForWidth())
        self.btn_quit.setSizePolicy(sizePolicy5)

        self.horizontalLayout_2.addWidget(self.btn_quit)

        self.btn_save = QPushButton(Settings)
        self.btn_save.setObjectName(u"btn_save")
        sizePolicy5.setHeightForWidth(self.btn_save.sizePolicy().hasHeightForWidth())
        self.btn_save.setSizePolicy(sizePolicy5)

        self.horizontalLayout_2.addWidget(self.btn_save)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Settings)

        self.combo_srs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Settings)
    # setupUi

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(QCoreApplication.translate("Settings", u"Settings - WaniKani Notify ", None))
        self.label_api.setText(QCoreApplication.translate("Settings", u"WaniKani API key", None))
        self.btn_test.setText(QCoreApplication.translate("Settings", u"Test API Key", None))
        self.label_test_api.setText("")
        self.label_notification.setText(QCoreApplication.translate("Settings", u"Notification settings", None))
        self.check_user_level.setText(QCoreApplication.translate("Settings", u"Only current user level", None))
        self.label_lessons.setText(QCoreApplication.translate("Settings", u"Lessons", None))
        self.check_l_radicals.setText(QCoreApplication.translate("Settings", u"Radicals", None))
        self.check_l_kanji.setText(QCoreApplication.translate("Settings", u"Kanji", None))
        self.check_l_vocabulary.setText(QCoreApplication.translate("Settings", u"Vocabulary", None))
        self.label_reviews.setText(QCoreApplication.translate("Settings", u"Reviews", None))
        self.check_r_radicals.setText(QCoreApplication.translate("Settings", u"Radicals", None))
        self.check_r_kanji.setText(QCoreApplication.translate("Settings", u"Kanji", None))
        self.check_r_vocabulary.setText(QCoreApplication.translate("Settings", u"Vocabulary", None))
        self.label_srs.setText(QCoreApplication.translate("Settings", u"Equal and below SRS level", None))
        self.combo_srs.setItemText(0, QCoreApplication.translate("Settings", u"Apprentice I", None))
        self.combo_srs.setItemText(1, QCoreApplication.translate("Settings", u"Apprentice II", None))
        self.combo_srs.setItemText(2, QCoreApplication.translate("Settings", u"Apprentice III", None))
        self.combo_srs.setItemText(3, QCoreApplication.translate("Settings", u"Apprentice IV", None))
        self.combo_srs.setItemText(4, QCoreApplication.translate("Settings", u"Guru I", None))
        self.combo_srs.setItemText(5, QCoreApplication.translate("Settings", u"Guru II", None))
        self.combo_srs.setItemText(6, QCoreApplication.translate("Settings", u"Master", None))
        self.combo_srs.setItemText(7, QCoreApplication.translate("Settings", u"Enlightened", None))

        self.label_info.setText("")
        self.btn_quit.setText(QCoreApplication.translate("Settings", u"Quit", None))
        self.btn_save.setText(QCoreApplication.translate("Settings", u"Save configuration", None))
    # retranslateUi

