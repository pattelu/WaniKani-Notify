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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Settings(object):
    def setupUi(self, Settings):
        if not Settings.objectName():
            Settings.setObjectName(u"Settings")
        Settings.resize(629, 549)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Settings.sizePolicy().hasHeightForWidth())
        Settings.setSizePolicy(sizePolicy)
        Settings.setMaximumSize(QSize(700, 550))
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
        self.verticalLayout_4.setContentsMargins(15, -1, -1, -1)
        self.label_lessons = QLabel(Settings)
        self.label_lessons.setObjectName(u"label_lessons")

        self.verticalLayout_4.addWidget(self.label_lessons)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(10, -1, -1, -1)
        self.check_user_level_lesson = QCheckBox(Settings)
        self.check_user_level_lesson.setObjectName(u"check_user_level_lesson")

        self.verticalLayout_5.addWidget(self.check_user_level_lesson)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.check_l_radicals = QCheckBox(Settings)
        self.check_l_radicals.setObjectName(u"check_l_radicals")

        self.horizontalLayout_6.addWidget(self.check_l_radicals)

        self.check_l_kanji = QCheckBox(Settings)
        self.check_l_kanji.setObjectName(u"check_l_kanji")

        self.horizontalLayout_6.addWidget(self.check_l_kanji)

        self.check_l_vocabulary = QCheckBox(Settings)
        self.check_l_vocabulary.setObjectName(u"check_l_vocabulary")

        self.horizontalLayout_6.addWidget(self.check_l_vocabulary)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)


        self.verticalLayout_5.addLayout(self.horizontalLayout_6)


        self.verticalLayout_4.addLayout(self.verticalLayout_5)

        self.label_reviews = QLabel(Settings)
        self.label_reviews.setObjectName(u"label_reviews")

        self.verticalLayout_4.addWidget(self.label_reviews)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(10, -1, -1, -1)
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.check_r_radicals = QCheckBox(Settings)
        self.check_r_radicals.setObjectName(u"check_r_radicals")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(30)
        sizePolicy3.setHeightForWidth(self.check_r_radicals.sizePolicy().hasHeightForWidth())
        self.check_r_radicals.setSizePolicy(sizePolicy3)
        self.check_r_radicals.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_4.addWidget(self.check_r_radicals, 0, Qt.AlignmentFlag.AlignLeft)

        self.widget_radicals_srs = QWidget(Settings)
        self.widget_radicals_srs.setObjectName(u"widget_radicals_srs")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.widget_radicals_srs.sizePolicy().hasHeightForWidth())
        self.widget_radicals_srs.setSizePolicy(sizePolicy4)
        self.horizontalLayout_3 = QHBoxLayout(self.widget_radicals_srs)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.line_3 = QFrame(self.widget_radicals_srs)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_3.addWidget(self.line_3)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.check_user_level_review_radicals = QCheckBox(self.widget_radicals_srs)
        self.check_user_level_review_radicals.setObjectName(u"check_user_level_review_radicals")

        self.verticalLayout_7.addWidget(self.check_user_level_review_radicals)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setContentsMargins(-1, 0, -1, 6)
        self.check_srs_radicals_1 = QCheckBox(self.widget_radicals_srs)
        self.check_srs_radicals_1.setObjectName(u"check_srs_radicals_1")

        self.gridLayout.addWidget(self.check_srs_radicals_1, 0, 1, 1, 1)

        self.check_srs_radicals_2 = QCheckBox(self.widget_radicals_srs)
        self.check_srs_radicals_2.setObjectName(u"check_srs_radicals_2")

        self.gridLayout.addWidget(self.check_srs_radicals_2, 0, 2, 1, 1)

        self.check_srs_radicals_5 = QCheckBox(self.widget_radicals_srs)
        self.check_srs_radicals_5.setObjectName(u"check_srs_radicals_5")

        self.gridLayout.addWidget(self.check_srs_radicals_5, 1, 1, 1, 1)

        self.check_srs_radicals_6 = QCheckBox(self.widget_radicals_srs)
        self.check_srs_radicals_6.setObjectName(u"check_srs_radicals_6")

        self.gridLayout.addWidget(self.check_srs_radicals_6, 1, 2, 1, 1)

        self.check_srs_radicals_8 = QCheckBox(self.widget_radicals_srs)
        self.check_srs_radicals_8.setObjectName(u"check_srs_radicals_8")

        self.gridLayout.addWidget(self.check_srs_radicals_8, 1, 4, 1, 1)

        self.check_srs_radicals_7 = QCheckBox(self.widget_radicals_srs)
        self.check_srs_radicals_7.setObjectName(u"check_srs_radicals_7")

        self.gridLayout.addWidget(self.check_srs_radicals_7, 1, 3, 1, 1)

        self.check_srs_radicals_3 = QCheckBox(self.widget_radicals_srs)
        self.check_srs_radicals_3.setObjectName(u"check_srs_radicals_3")

        self.gridLayout.addWidget(self.check_srs_radicals_3, 0, 3, 1, 1)

        self.check_srs_radicals_4 = QCheckBox(self.widget_radicals_srs)
        self.check_srs_radicals_4.setObjectName(u"check_srs_radicals_4")

        self.gridLayout.addWidget(self.check_srs_radicals_4, 0, 4, 1, 1)


        self.verticalLayout_7.addLayout(self.gridLayout)


        self.horizontalLayout_3.addLayout(self.verticalLayout_7)


        self.horizontalLayout_4.addWidget(self.widget_radicals_srs)


        self.verticalLayout_9.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.check_r_kanji = QCheckBox(Settings)
        self.check_r_kanji.setObjectName(u"check_r_kanji")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.check_r_kanji.sizePolicy().hasHeightForWidth())
        self.check_r_kanji.setSizePolicy(sizePolicy5)
        self.check_r_kanji.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_5.addWidget(self.check_r_kanji, 0, Qt.AlignmentFlag.AlignLeft)

        self.widget_kanji_srs = QWidget(Settings)
        self.widget_kanji_srs.setObjectName(u"widget_kanji_srs")
        sizePolicy4.setHeightForWidth(self.widget_kanji_srs.sizePolicy().hasHeightForWidth())
        self.widget_kanji_srs.setSizePolicy(sizePolicy4)
        self.horizontalLayout_7 = QHBoxLayout(self.widget_kanji_srs)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.line_4 = QFrame(self.widget_kanji_srs)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_7.addWidget(self.line_4)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.check_user_level_review_kanji = QCheckBox(self.widget_kanji_srs)
        self.check_user_level_review_kanji.setObjectName(u"check_user_level_review_kanji")

        self.verticalLayout_8.addWidget(self.check_user_level_review_kanji)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.check_srs_kanji_3 = QCheckBox(self.widget_kanji_srs)
        self.check_srs_kanji_3.setObjectName(u"check_srs_kanji_3")

        self.gridLayout_2.addWidget(self.check_srs_kanji_3, 0, 2, 1, 1)

        self.check_srs_kanji_6 = QCheckBox(self.widget_kanji_srs)
        self.check_srs_kanji_6.setObjectName(u"check_srs_kanji_6")

        self.gridLayout_2.addWidget(self.check_srs_kanji_6, 1, 1, 1, 1)

        self.check_srs_kanji_4 = QCheckBox(self.widget_kanji_srs)
        self.check_srs_kanji_4.setObjectName(u"check_srs_kanji_4")

        self.gridLayout_2.addWidget(self.check_srs_kanji_4, 0, 3, 1, 1)

        self.check_srs_kanji_8 = QCheckBox(self.widget_kanji_srs)
        self.check_srs_kanji_8.setObjectName(u"check_srs_kanji_8")

        self.gridLayout_2.addWidget(self.check_srs_kanji_8, 1, 3, 1, 1)

        self.check_srs_kanji_1 = QCheckBox(self.widget_kanji_srs)
        self.check_srs_kanji_1.setObjectName(u"check_srs_kanji_1")

        self.gridLayout_2.addWidget(self.check_srs_kanji_1, 0, 0, 1, 1)

        self.check_srs_kanji_5 = QCheckBox(self.widget_kanji_srs)
        self.check_srs_kanji_5.setObjectName(u"check_srs_kanji_5")

        self.gridLayout_2.addWidget(self.check_srs_kanji_5, 1, 0, 1, 1)

        self.check_srs_kanji_7 = QCheckBox(self.widget_kanji_srs)
        self.check_srs_kanji_7.setObjectName(u"check_srs_kanji_7")

        self.gridLayout_2.addWidget(self.check_srs_kanji_7, 1, 2, 1, 1)

        self.check_srs_kanji_2 = QCheckBox(self.widget_kanji_srs)
        self.check_srs_kanji_2.setObjectName(u"check_srs_kanji_2")

        self.gridLayout_2.addWidget(self.check_srs_kanji_2, 0, 1, 1, 1)


        self.verticalLayout_8.addLayout(self.gridLayout_2)


        self.horizontalLayout_7.addLayout(self.verticalLayout_8)


        self.horizontalLayout_5.addWidget(self.widget_kanji_srs)


        self.verticalLayout_9.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.check_r_vocabulary = QCheckBox(Settings)
        self.check_r_vocabulary.setObjectName(u"check_r_vocabulary")
        sizePolicy5.setHeightForWidth(self.check_r_vocabulary.sizePolicy().hasHeightForWidth())
        self.check_r_vocabulary.setSizePolicy(sizePolicy5)
        self.check_r_vocabulary.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_8.addWidget(self.check_r_vocabulary, 0, Qt.AlignmentFlag.AlignLeft)

        self.widget_vocabulary_srs = QWidget(Settings)
        self.widget_vocabulary_srs.setObjectName(u"widget_vocabulary_srs")
        sizePolicy4.setHeightForWidth(self.widget_vocabulary_srs.sizePolicy().hasHeightForWidth())
        self.widget_vocabulary_srs.setSizePolicy(sizePolicy4)
        self.horizontalLayout_9 = QHBoxLayout(self.widget_vocabulary_srs)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.line_5 = QFrame(self.widget_vocabulary_srs)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.Shape.VLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_9.addWidget(self.line_5)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.check_user_level_review_vocabulary = QCheckBox(self.widget_vocabulary_srs)
        self.check_user_level_review_vocabulary.setObjectName(u"check_user_level_review_vocabulary")

        self.verticalLayout_10.addWidget(self.check_user_level_review_vocabulary)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.check_srs_vocabulary_2 = QCheckBox(self.widget_vocabulary_srs)
        self.check_srs_vocabulary_2.setObjectName(u"check_srs_vocabulary_2")

        self.gridLayout_3.addWidget(self.check_srs_vocabulary_2, 0, 1, 1, 1)

        self.check_srs_vocabulary_1 = QCheckBox(self.widget_vocabulary_srs)
        self.check_srs_vocabulary_1.setObjectName(u"check_srs_vocabulary_1")

        self.gridLayout_3.addWidget(self.check_srs_vocabulary_1, 0, 0, 1, 1)

        self.check_srs_vocabulary_3 = QCheckBox(self.widget_vocabulary_srs)
        self.check_srs_vocabulary_3.setObjectName(u"check_srs_vocabulary_3")

        self.gridLayout_3.addWidget(self.check_srs_vocabulary_3, 0, 2, 1, 1)

        self.check_srs_vocabulary_4 = QCheckBox(self.widget_vocabulary_srs)
        self.check_srs_vocabulary_4.setObjectName(u"check_srs_vocabulary_4")

        self.gridLayout_3.addWidget(self.check_srs_vocabulary_4, 0, 3, 1, 1)

        self.check_srs_vocabulary_5 = QCheckBox(self.widget_vocabulary_srs)
        self.check_srs_vocabulary_5.setObjectName(u"check_srs_vocabulary_5")

        self.gridLayout_3.addWidget(self.check_srs_vocabulary_5, 1, 0, 1, 1)

        self.check_srs_vocabulary_6 = QCheckBox(self.widget_vocabulary_srs)
        self.check_srs_vocabulary_6.setObjectName(u"check_srs_vocabulary_6")

        self.gridLayout_3.addWidget(self.check_srs_vocabulary_6, 1, 1, 1, 1)

        self.check_srs_vocabulary_7 = QCheckBox(self.widget_vocabulary_srs)
        self.check_srs_vocabulary_7.setObjectName(u"check_srs_vocabulary_7")

        self.gridLayout_3.addWidget(self.check_srs_vocabulary_7, 1, 2, 1, 1)

        self.check_srs_vocabulary_8 = QCheckBox(self.widget_vocabulary_srs)
        self.check_srs_vocabulary_8.setObjectName(u"check_srs_vocabulary_8")

        self.gridLayout_3.addWidget(self.check_srs_vocabulary_8, 1, 3, 1, 1)


        self.verticalLayout_10.addLayout(self.gridLayout_3)


        self.horizontalLayout_9.addLayout(self.verticalLayout_10)


        self.horizontalLayout_8.addWidget(self.widget_vocabulary_srs)


        self.verticalLayout_9.addLayout(self.horizontalLayout_8)


        self.horizontalLayout_10.addLayout(self.verticalLayout_9)


        self.verticalLayout_4.addLayout(self.horizontalLayout_10)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)


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
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_info.sizePolicy().hasHeightForWidth())
        self.label_info.setSizePolicy(sizePolicy6)
        self.label_info.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_info)

        self.btn_quit = QPushButton(Settings)
        self.btn_quit.setObjectName(u"btn_quit")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.btn_quit.sizePolicy().hasHeightForWidth())
        self.btn_quit.setSizePolicy(sizePolicy7)

        self.horizontalLayout_2.addWidget(self.btn_quit)

        self.btn_save = QPushButton(Settings)
        self.btn_save.setObjectName(u"btn_save")
        sizePolicy7.setHeightForWidth(self.btn_save.sizePolicy().hasHeightForWidth())
        self.btn_save.setSizePolicy(sizePolicy7)

        self.horizontalLayout_2.addWidget(self.btn_save)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Settings)

        QMetaObject.connectSlotsByName(Settings)
    # setupUi

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(QCoreApplication.translate("Settings", u"Settings - WaniKani Notify ", None))
        self.label_api.setText(QCoreApplication.translate("Settings", u"WaniKani API key", None))
        self.btn_test.setText(QCoreApplication.translate("Settings", u"Test API Key", None))
        self.label_test_api.setText("")
        self.label_notification.setText(QCoreApplication.translate("Settings", u"Notification settings", None))
        self.label_lessons.setText(QCoreApplication.translate("Settings", u"Lessons", None))
        self.check_user_level_lesson.setText(QCoreApplication.translate("Settings", u"Only current user level", None))
        self.check_l_radicals.setText(QCoreApplication.translate("Settings", u"Radicals", None))
        self.check_l_kanji.setText(QCoreApplication.translate("Settings", u"Kanji", None))
        self.check_l_vocabulary.setText(QCoreApplication.translate("Settings", u"Vocabulary", None))
        self.label_reviews.setText(QCoreApplication.translate("Settings", u"Reviews", None))
        self.check_r_radicals.setText(QCoreApplication.translate("Settings", u"Radicals", None))
        self.check_user_level_review_radicals.setText(QCoreApplication.translate("Settings", u"Only current user level", None))
        self.check_srs_radicals_1.setText(QCoreApplication.translate("Settings", u"Apprentice I", None))
        self.check_srs_radicals_2.setText(QCoreApplication.translate("Settings", u"Apprentice II", None))
        self.check_srs_radicals_5.setText(QCoreApplication.translate("Settings", u"Guru I", None))
        self.check_srs_radicals_6.setText(QCoreApplication.translate("Settings", u"Guru II", None))
        self.check_srs_radicals_8.setText(QCoreApplication.translate("Settings", u"Enlightened", None))
        self.check_srs_radicals_7.setText(QCoreApplication.translate("Settings", u"Master", None))
        self.check_srs_radicals_3.setText(QCoreApplication.translate("Settings", u"Apprentice III", None))
        self.check_srs_radicals_4.setText(QCoreApplication.translate("Settings", u"Apprentice IV", None))
        self.check_r_kanji.setText(QCoreApplication.translate("Settings", u"Kanji", None))
        self.check_user_level_review_kanji.setText(QCoreApplication.translate("Settings", u"Only current user level", None))
        self.check_srs_kanji_3.setText(QCoreApplication.translate("Settings", u"Apprentice III", None))
        self.check_srs_kanji_6.setText(QCoreApplication.translate("Settings", u"Guru II", None))
        self.check_srs_kanji_4.setText(QCoreApplication.translate("Settings", u"Apprentice IV", None))
        self.check_srs_kanji_8.setText(QCoreApplication.translate("Settings", u"Enlightened", None))
        self.check_srs_kanji_1.setText(QCoreApplication.translate("Settings", u"Apprentice I", None))
        self.check_srs_kanji_5.setText(QCoreApplication.translate("Settings", u"Guru I", None))
        self.check_srs_kanji_7.setText(QCoreApplication.translate("Settings", u"Master", None))
        self.check_srs_kanji_2.setText(QCoreApplication.translate("Settings", u"Apprentice II", None))
        self.check_r_vocabulary.setText(QCoreApplication.translate("Settings", u"Vocabulary", None))
        self.check_user_level_review_vocabulary.setText(QCoreApplication.translate("Settings", u"Only current user level", None))
        self.check_srs_vocabulary_2.setText(QCoreApplication.translate("Settings", u"Apprentice II", None))
        self.check_srs_vocabulary_1.setText(QCoreApplication.translate("Settings", u"Apprentice I", None))
        self.check_srs_vocabulary_3.setText(QCoreApplication.translate("Settings", u"Apprentice III", None))
        self.check_srs_vocabulary_4.setText(QCoreApplication.translate("Settings", u"Apprentice IV", None))
        self.check_srs_vocabulary_5.setText(QCoreApplication.translate("Settings", u"Guru I", None))
        self.check_srs_vocabulary_6.setText(QCoreApplication.translate("Settings", u"Guru II", None))
        self.check_srs_vocabulary_7.setText(QCoreApplication.translate("Settings", u"Master", None))
        self.check_srs_vocabulary_8.setText(QCoreApplication.translate("Settings", u"Enlightened", None))
        self.label_info.setText("")
        self.btn_quit.setText(QCoreApplication.translate("Settings", u"Quit", None))
        self.btn_save.setText(QCoreApplication.translate("Settings", u"Save configuration", None))
    # retranslateUi

