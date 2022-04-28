################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QListWidget,
    QListWidgetItem, QMainWindow, QPlainTextEdit, QPushButton,
    QSizePolicy, QTabWidget, QToolButton, QVBoxLayout,
    QWidget)
import files_rc

class Ui_Main(object):
    def setupUi(self, Main):
        if not Main.objectName():
            Main.setObjectName(u"Main")
        Main.resize(1258, 761)
        Main.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.centralwidget = QWidget(Main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget\n"
"{\n"
"	background-color: #fff;\n"
"}")
        self.main_lt = QVBoxLayout(self.centralwidget)
        self.main_lt.setSpacing(15)
        self.main_lt.setObjectName(u"main_lt")
        self.main_lt.setContentsMargins(0, 0, 0, 0)
        self.name_prj = QLabel(self.centralwidget)
        self.name_prj.setObjectName(u"name_prj")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name_prj.sizePolicy().hasHeightForWidth())
        self.name_prj.setSizePolicy(sizePolicy)
        self.name_prj.setStyleSheet(u"QLabel\n"
"{\n"
"	font-family: 'Inter';\n"
"	font-weight: 700;\n"
"	font-size: 40px;\n"
"	color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(7, 119, 164, 206));\n"
"	padding-left: 5px;\n"
"}")

        self.main_lt.addWidget(self.name_prj)

        self.main_frame_lt = QFrame(self.centralwidget)
        self.main_frame_lt.setObjectName(u"main_frame_lt")
        self.main_frame_lt.setStyleSheet(u"QFrame\n"
"{\n"
"	background-color: #FAFAFA;\n"
"	border: 1px solid #C4C4C4;\n"
"	box-sizing: border-box;\n"
"	border-radius: 16px;\n"
"}")
        self.main_frame_lt.setFrameShape(QFrame.StyledPanel)
        self.main_frame_lt.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.main_frame_lt)
        self.horizontalLayout_3.setSpacing(20)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(20, 20, 20, 20)
        self.left_lt = QVBoxLayout()
        self.left_lt.setSpacing(20)
        self.left_lt.setObjectName(u"left_lt")
        self.files = QFrame(self.main_frame_lt)
        self.files.setObjectName(u"files")
        sizePolicy.setHeightForWidth(self.files.sizePolicy().hasHeightForWidth())
        self.files.setSizePolicy(sizePolicy)
        self.files.setStyleSheet(u"QFrame \n"
"{\n"
"	border: 0;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0));\n"
"}\n"
"\n"
"QLabel \n"
"{\n"
"	font-family: 'Inter';\n"
"	font-weight: 700;\n"
"	font-size: 32px;\n"
"	color: #000000;\n"
"	border: 0;\n"
"	text-align: left;\n"
"}\n"
"\n"
"QToolButton\n"
"{\n"
"	padding: 10 0 -5 0;\n"
"	font-family: 'Inter';\n"
"	font-weight: 400;\n"
"	font-size: 14px;\n"
"	position: top;\n"
"	background-color: #FFFFFF;\n"
"	border: 1px solid #C4C4C4;\n"
"	border-radius: 16px;\n"
"}\n"
"\n"
"QToolButton::hover\n"
"{\n"
"	background-color: rgba(196, 196, 196, 0.125);\n"
"	border: 1px solid #C4C4C4;\n"
"}\n"
"\n"
"QToolButton::pressed\n"
"{\n"
"	background-color: rgba(196, 196, 196, 0.25);\n"
"	border: 1px solid #C4C4C4;\n"
"}\n"
"")
        self.files.setFrameShape(QFrame.StyledPanel)
        self.files.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.files)
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.files_title = QLabel(self.files)
        self.files_title.setObjectName(u"files_title")
        sizePolicy.setHeightForWidth(self.files_title.sizePolicy().hasHeightForWidth())
        self.files_title.setSizePolicy(sizePolicy)
        self.files_title.setAutoFillBackground(False)
        self.files_title.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.files_title)

        self.files_lt = QHBoxLayout()
        self.files_lt.setSpacing(15)
        self.files_lt.setObjectName(u"files_lt")
        self.files_lt.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.btn_file_1 = QToolButton(self.files)
        self.btn_file_1.setObjectName(u"btn_file_1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_file_1.sizePolicy().hasHeightForWidth())
        self.btn_file_1.setSizePolicy(sizePolicy1)
        self.btn_file_1.setMinimumSize(QSize(120, 120))
        self.btn_file_1.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/icons/file_off.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_file_1.setIcon(icon)
        self.btn_file_1.setIconSize(QSize(60, 60))
        self.btn_file_1.setChecked(False)
        self.btn_file_1.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.files_lt.addWidget(self.btn_file_1)

        self.btn_file_2 = QToolButton(self.files)
        self.btn_file_2.setObjectName(u"btn_file_2")
        sizePolicy1.setHeightForWidth(self.btn_file_2.sizePolicy().hasHeightForWidth())
        self.btn_file_2.setSizePolicy(sizePolicy1)
        self.btn_file_2.setMinimumSize(QSize(120, 120))
        self.btn_file_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_file_2.setIcon(icon)
        self.btn_file_2.setIconSize(QSize(60, 60))
        self.btn_file_2.setChecked(False)
        self.btn_file_2.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.files_lt.addWidget(self.btn_file_2)

        self.btn_file_3 = QToolButton(self.files)
        self.btn_file_3.setObjectName(u"btn_file_3")
        self.btn_file_3.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.btn_file_3.sizePolicy().hasHeightForWidth())
        self.btn_file_3.setSizePolicy(sizePolicy1)
        self.btn_file_3.setMinimumSize(QSize(120, 120))
        self.btn_file_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_file_3.setIcon(icon)
        self.btn_file_3.setIconSize(QSize(60, 60))
        self.btn_file_3.setChecked(False)
        self.btn_file_3.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.files_lt.addWidget(self.btn_file_3)

        self.btn_file_4 = QToolButton(self.files)
        self.btn_file_4.setObjectName(u"btn_file_4")
        sizePolicy1.setHeightForWidth(self.btn_file_4.sizePolicy().hasHeightForWidth())
        self.btn_file_4.setSizePolicy(sizePolicy1)
        self.btn_file_4.setMinimumSize(QSize(120, 120))
        self.btn_file_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_file_4.setIcon(icon)
        self.btn_file_4.setIconSize(QSize(60, 60))
        self.btn_file_4.setChecked(False)
        self.btn_file_4.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.files_lt.addWidget(self.btn_file_4)

        self.btn_file_5 = QToolButton(self.files)
        self.btn_file_5.setObjectName(u"btn_file_5")
        sizePolicy1.setHeightForWidth(self.btn_file_5.sizePolicy().hasHeightForWidth())
        self.btn_file_5.setSizePolicy(sizePolicy1)
        self.btn_file_5.setMinimumSize(QSize(120, 120))
        self.btn_file_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_file_5.setIcon(icon)
        self.btn_file_5.setIconSize(QSize(60, 60))
        self.btn_file_5.setChecked(False)
        self.btn_file_5.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.files_lt.addWidget(self.btn_file_5)


        self.verticalLayout_3.addLayout(self.files_lt)


        self.left_lt.addWidget(self.files)

        self.tools = QFrame(self.main_frame_lt)
        self.tools.setObjectName(u"tools")
        sizePolicy.setHeightForWidth(self.tools.sizePolicy().hasHeightForWidth())
        self.tools.setSizePolicy(sizePolicy)
        self.tools.setStyleSheet(u"QFrame\n"
"{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 0;\n"
"}\n"
"\n"
"QLabel \n"
"{\n"
"	font-family: 'Inter';\n"
"	font-weight: 700;\n"
"	font-size: 32px;\n"
"	color: #000000;\n"
"	border: 0;\n"
"	text-align: left;\n"
"}")
        self.tools.setFrameShape(QFrame.StyledPanel)
        self.tools.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.tools)
        self.verticalLayout_6.setSpacing(15)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(15, 15, 15, 15)
        self.tools_title = QLabel(self.tools)
        self.tools_title.setObjectName(u"tools_title")

        self.verticalLayout_6.addWidget(self.tools_title)

        self.reg_merge_lt = QGridLayout()
        self.reg_merge_lt.setObjectName(u"reg_merge_lt")
        self.btn_merge = QToolButton(self.tools)
        self.btn_merge.setObjectName(u"btn_merge")
        sizePolicy1.setHeightForWidth(self.btn_merge.sizePolicy().hasHeightForWidth())
        self.btn_merge.setSizePolicy(sizePolicy1)
        self.btn_merge.setMinimumSize(QSize(150, 150))
        self.btn_merge.setMaximumSize(QSize(150, 150))
        self.btn_merge.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_merge.setStyleSheet(u"QToolButton\n"
"{\n"
"	padding: 0;\n"
"	font-family: 'Inter';\n"
"	font-weight: 400;\n"
"	font-size: 20px;\n"
"	color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(119, 164, 211, 255), stop:1 rgba(121, 201, 202, 255));\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(119, 164, 211, 35), stop:1 rgba(121, 201, 202, 35));\n"
"	border: 1px solid #C4C4C4;\n"
"	border-radius: 16px;\n"
"}\n"
"\n"
"QToolButton::hover\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(119, 164, 211, 50), stop:1 rgba(121, 201, 202, 50));\n"
"	border: 1px solid #C4C4C4;\n"
"}\n"
"\n"
"QToolButton::pressed\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(119, 164, 211, 70), stop:1 rgba(121, 201, 202, 70));\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/merge.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_merge.setIcon(icon1)
        self.btn_merge.setIconSize(QSize(100, 100))
        self.btn_merge.setChecked(False)
        self.btn_merge.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.reg_merge_lt.addWidget(self.btn_merge, 1, 1, 1, 1)

        self.reg_title = QLabel(self.tools)
        self.reg_title.setObjectName(u"reg_title")
        self.reg_title.setStyleSheet(u"QLabel \n"
"{\n"
"	font-family: 'Inter';\n"
"	font-weight: 400;\n"
"	font-size: 20px;\n"
"	color: #000000;\n"
"	border: 0;\n"
"	text-align: left;\n"
"}")

        self.reg_merge_lt.addWidget(self.reg_title, 0, 0, 1, 1)

        self.reg_list = QListWidget(self.tools)
        self.reg_list.setObjectName(u"reg_list")
        sizePolicy1.setHeightForWidth(self.reg_list.sizePolicy().hasHeightForWidth())
        self.reg_list.setSizePolicy(sizePolicy1)
        self.reg_list.setMinimumSize(QSize(0, 150))
        self.reg_list.setMaximumSize(QSize(16777215, 150))
        self.reg_list.setStyleSheet(u"QListWidget\n"
"{\n"
"	padding: 5px;\n"
"	font-family: 'JetBrains Mono';\n"
"	font-size: 16px;\n"
"	border: 1px solid #C4C4C4;\n"
"	border-radius: 16px;\n"
"}\n"
"\n"
"QListWidget::item\n"
"{\n"
"	border-bottom: 1px solid #C4C4C4;\n"
"	selection-color: rgb(7, 119, 164);\n"
"	selection-background-color: rgb(0, 0, 0);\n"
"}")
        self.reg_list.setDragDropMode(QAbstractItemView.InternalMove)

        self.reg_merge_lt.addWidget(self.reg_list, 1, 0, 1, 1)


        self.verticalLayout_6.addLayout(self.reg_merge_lt)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.btn_new_reg = QPushButton(self.tools)
        self.btn_new_reg.setObjectName(u"btn_new_reg")
        self.btn_new_reg.setMinimumSize(QSize(0, 45))
        self.btn_new_reg.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_new_reg.setStyleSheet(u"QPushButton\n"
"{\n"
"	font-family: 'Inter';\n"
"	font-weight: 400;\n"
"	font-size: 18px;\n"
"	background-color: #fff;\n"
"	border: 1px solid #C4C4C4;\n"
"	border-radius: 16px;\n"
"}\n"
"\n"
"QPushButton::hover\n"
"{\n"
"	background-color: rgba(196, 196, 196, 0.125);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"	background-color: rgba(196, 196, 196, 0.25);\n"
"}")
        self.btn_new_reg.setIconSize(QSize(50, 50))

        self.horizontalLayout.addWidget(self.btn_new_reg)

        self.btn_del = QPushButton(self.tools)
        self.btn_del.setObjectName(u"btn_del")
        self.btn_del.setEnabled(True)
        self.btn_del.setMinimumSize(QSize(0, 45))
        self.btn_del.setMaximumSize(QSize(16777215, 50))
        self.btn_del.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_del.setStyleSheet(u"QPushButton\n"
"{\n"
"	font-family: 'Inter';\n"
"	font-weight: 400;\n"
"	font-size: 18px;\n"
"	background-color: #fff;\n"
"	border: 1px solid #C4C4C4;\n"
"	border-radius: 16px;\n"
"}\n"
"\n"
"QPushButton::hover\n"
"{\n"
"	color: rgb(229, 46, 46);\n"
"	background-color: ;\n"
"	background-color: rgba(229, 46, 46, 0.1);\n"
"	border: 1px solid #C4C4C4;\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"	color: rgb(229, 46, 46);\n"
"	background-color: rgba(229, 46, 46, 0.15);\n"
"}")
        self.btn_del.setIconSize(QSize(50, 50))

        self.horizontalLayout.addWidget(self.btn_del)

        self.btn_exp_hex = QPushButton(self.tools)
        self.btn_exp_hex.setObjectName(u"btn_exp_hex")
        self.btn_exp_hex.setMinimumSize(QSize(0, 45))
        self.btn_exp_hex.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_exp_hex.setStyleSheet(u"QPushButton\n"
"{\n"
"	font-family: 'Inter';\n"
"	font-weight: 400;\n"
"	font-size: 18px;\n"
"	color: #77A4D3;\n"
"	background-color: rgba(119, 164, 211, 0.1);\n"
"	border: 1px solid #C4C4C4;\n"
"	border-radius: 16px;\n"
"	padding: 0 15px 0 15px;\n"
"}\n"
"\n"
"QPushButton::hover\n"
"{\n"
"	background-color: rgba(119, 164, 211, 0.2);\n"
"	border: 1px solid #C4C4C4;\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"	background-color: rgba(119, 164, 211, 0.3);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/0x0.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_exp_hex.setIcon(icon2)
        self.btn_exp_hex.setIconSize(QSize(40, 40))

        self.horizontalLayout.addWidget(self.btn_exp_hex)

        self.btn_exp_bin = QPushButton(self.tools)
        self.btn_exp_bin.setObjectName(u"btn_exp_bin")
        self.btn_exp_bin.setMinimumSize(QSize(0, 45))
        self.btn_exp_bin.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_exp_bin.setStyleSheet(u"QPushButton\n"
"{\n"
"	font-family: 'Inter';\n"
"	font-weight: 400;\n"
"	font-size: 18px;\n"
"	color: #79C9CA;\n"
"	background-color: rgba(121, 201, 202, 0.1);\n"
"	border: 1px solid #C4C4C4;\n"
"	border-radius: 16px;\n"
"	padding: 0 15px 0 15px;\n"
"}\n"
"\n"
"QPushButton::hover\n"
"{\n"
"	background-color: rgba(121, 201, 202, 0.2);\n"
"	border: 1px solid #C4C4C4;\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"	background-color: rgba(121, 201, 202, 0.3);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/101.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_exp_bin.setIcon(icon3)
        self.btn_exp_bin.setIconSize(QSize(40, 40))

        self.horizontalLayout.addWidget(self.btn_exp_bin)


        self.verticalLayout_6.addLayout(self.horizontalLayout)


        self.left_lt.addWidget(self.tools)

        self.message = QFrame(self.main_frame_lt)
        self.message.setObjectName(u"message")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.message.sizePolicy().hasHeightForWidth())
        self.message.setSizePolicy(sizePolicy2)
        self.message.setStyleSheet(u"QFrame\n"
"{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 0;\n"
"}")
        self.message.setFrameShape(QFrame.StyledPanel)
        self.message.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.message)
        self.verticalLayout_7.setSpacing(15)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(15, 15, 15, 15)
        self.message_title = QLabel(self.message)
        self.message_title.setObjectName(u"message_title")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.message_title.sizePolicy().hasHeightForWidth())
        self.message_title.setSizePolicy(sizePolicy3)
        self.message_title.setStyleSheet(u"QLabel \n"
"{\n"
"	font-family: 'Inter';\n"
"	font-weight: 700;\n"
"	font-size: 32px;\n"
"	color: #000000;\n"
"	border: 0;\n"
"	text-align: left;\n"
"}")

        self.verticalLayout_7.addWidget(self.message_title)

        self.message_label = QLabel(self.message)
        self.message_label.setObjectName(u"message_label")
        self.message_label.setStyleSheet(u"QLabel \n"
"{\n"
"	font-family: 'Inter';\n"
"	font-weight: 400;\n"
"	font-size: 20px;\n"
"	color: #000000;\n"
"	border: 0;\n"
"	text-align: left;\n"
"}")

        self.verticalLayout_7.addWidget(self.message_label, 0, Qt.AlignTop)


        self.left_lt.addWidget(self.message)


        self.horizontalLayout_3.addLayout(self.left_lt)

        self.right_lt = QVBoxLayout()
        self.right_lt.setSpacing(15)
        self.right_lt.setObjectName(u"right_lt")
        self.right_lt.setContentsMargins(0, 0, -1, -1)
        self.editor = QFrame(self.main_frame_lt)
        self.editor.setObjectName(u"editor")
        self.editor.setStyleSheet(u"QFrame\n"
"{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 0;\n"
"}")
        self.editor.setFrameShape(QFrame.StyledPanel)
        self.editor.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.editor)
        self.verticalLayout_4.setSpacing(15)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(15, 15, 15, 15)
        self.editor_title = QLabel(self.editor)
        self.editor_title.setObjectName(u"editor_title")
        sizePolicy.setHeightForWidth(self.editor_title.sizePolicy().hasHeightForWidth())
        self.editor_title.setSizePolicy(sizePolicy)
        self.editor_title.setStyleSheet(u"QLabel \n"
"{\n"
"	font-family: 'Inter';\n"
"	font-weight: 700;\n"
"	font-size: 32px;\n"
"	color: #000000;\n"
"	border: 0;\n"
"	text-align: left;\n"
"}")

        self.verticalLayout_4.addWidget(self.editor_title)

        self.save_del_lt = QHBoxLayout()
        self.save_del_lt.setSpacing(15)
        self.save_del_lt.setObjectName(u"save_del_lt")
        self.btn_save = QPushButton(self.editor)
        self.btn_save.setObjectName(u"btn_save")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.btn_save.sizePolicy().hasHeightForWidth())
        self.btn_save.setSizePolicy(sizePolicy4)
        self.btn_save.setMinimumSize(QSize(200, 45))
        self.btn_save.setMaximumSize(QSize(16777215, 50))
        self.btn_save.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_save.setStyleSheet(u"QPushButton\n"
"{\n"
"	font-family: 'Inter';\n"
"	font-weight: 400;\n"
"	font-size: 18px;\n"
"	background-color: #fff;\n"
"	border: 1px solid #C4C4C4;\n"
"	border-radius: 16px;\n"
"}\n"
"\n"
"QPushButton::hover\n"
"{\n"
"	background-color: rgba(196, 196, 196, 0.125);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"	background-color: rgba(196, 196, 196, 0.25);\n"
"}")
        self.btn_save.setIconSize(QSize(50, 50))

        self.save_del_lt.addWidget(self.btn_save)


        self.verticalLayout_4.addLayout(self.save_del_lt)

        self.tabWidget = QTabWidget(self.editor)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(500, 0))
        self.tabWidget.setCursor(QCursor(Qt.PointingHandCursor))
        self.tabWidget.setStyleSheet(u"QTabWiget\n"
"{\n"
"	font-family: 'Inter';\n"
"}\n"
"\n"
"QTabWidget::tab-bar\n"
"{\n"
"	min-width: 1000;\n"
"}\n"
"\n"
"QTabBar::tab\n"
"{\n"
"	font-family: 'Inter';\n"
"	font-size: 16px;\n"
"	color: rgb(7, 119, 164);\n"
"	height: 30px;\n"
"    border-radius: 16px;\n"
"	border: 1px solid #C4C4C4;\n"
"}\n"
"\n"
"QTabBar::tab:hover\n"
"{\n"
"	background-color: rgba(7, 119, 164, 0.1);\n"
"}\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"	background-color: rgba(7, 119, 164, 0.15);\n"
"}\n"
"\n"
"QTabWidget::pane\n"
"{ \n"
"	border: 0;\n"
"}\n"
"\n"
"")
        self.tab_hex = QWidget()
        self.tab_hex.setObjectName(u"tab_hex")
        self.tab_hex.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.tab_hex)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 15, 0, 0)
        self.text_ofs_reg = QPlainTextEdit(self.tab_hex)
        self.text_ofs_reg.setObjectName(u"text_ofs_reg")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.text_ofs_reg.sizePolicy().hasHeightForWidth())
        self.text_ofs_reg.setSizePolicy(sizePolicy5)
        self.text_ofs_reg.setMaximumSize(QSize(65, 35))
        self.text_ofs_reg.setStyleSheet(u"QPlainTextEdit\n"
"{\n"
"	font-family: 'JetBrains Mono';\n"
"	font-weight: 400;\n"
"	font-size: 18px;\n"
"	color: #77A4D3;\n"
"	border: 1px solid #C4C4C4;\n"
"	border-radius: 16px;\n"
"	background-color: rgba(119, 164, 211, 0.25);\n"
"	padding: 5px;\n"
"}")
        self.text_ofs_reg.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.text_ofs_reg.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.text_ofs_reg.setOverwriteMode(False)

        self.gridLayout.addWidget(self.text_ofs_reg, 0, 0, 1, 1)

        self.hex_data_plainTextEdit = QPlainTextEdit(self.tab_hex)
        self.hex_data_plainTextEdit.setObjectName(u"hex_data_plainTextEdit")
        self.hex_data_plainTextEdit.setMinimumSize(QSize(400, 0))
        self.hex_data_plainTextEdit.setStyleSheet(u"QPlainTextEdit\n"
"{\n"
"	font-family: 'JetBrains Mono';\n"
"	font-weight: 400;\n"
"	font-size: 18px;\n"
"	border: 1px solid #C4C4C4;\n"
"	border-radius: 16px;\n"
"	padding: 5px;\n"
"	background-color: #FAFAFA;\n"
"}")

        self.gridLayout.addWidget(self.hex_data_plainTextEdit, 1, 1, 1, 1)

        self.lable_ofs_and_file = QLabel(self.tab_hex)
        self.lable_ofs_and_file.setObjectName(u"lable_ofs_and_file")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.lable_ofs_and_file.sizePolicy().hasHeightForWidth())
        self.lable_ofs_and_file.setSizePolicy(sizePolicy6)
        self.lable_ofs_and_file.setStyleSheet(u"QLabel \n"
"{\n"
"	font-family: 'Inter';\n"
"	font-weight: 500;\n"
"	font-size: 16px;\n"
"	color: rgba(0, 0, 0, 50%);\n"
"	border: 0;\n"
"	text-align: left;\n"
"}")

        self.gridLayout.addWidget(self.lable_ofs_and_file, 0, 1, 1, 1)

        self.hex_adr_plainTextEdit = QPlainTextEdit(self.tab_hex)
        self.hex_adr_plainTextEdit.setObjectName(u"hex_adr_plainTextEdit")
        sizePolicy7 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.hex_adr_plainTextEdit.sizePolicy().hasHeightForWidth())
        self.hex_adr_plainTextEdit.setSizePolicy(sizePolicy7)
        self.hex_adr_plainTextEdit.setMinimumSize(QSize(65, 0))
        self.hex_adr_plainTextEdit.setMaximumSize(QSize(65, 16777215))
        self.hex_adr_plainTextEdit.setStyleSheet(u"QPlainTextEdit\n"
"{\n"
"	font-family: 'JetBrains Mono';\n"
"	font-weight: 400;\n"
"	font-size: 18px;\n"
"	color: #009C93;\n"
"	border: 1px solid #C4C4C4;\n"
"	border-radius: 16px;\n"
"	background-color: rgba(0, 156, 147, 0.1);\n"
"	padding: 5px;\n"
"}")
        self.hex_adr_plainTextEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.hex_adr_plainTextEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.gridLayout.addWidget(self.hex_adr_plainTextEdit, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab_hex, "")
        self.tab_bin = QWidget()
        self.tab_bin.setObjectName(u"tab_bin")
        self.tab_bin.setStyleSheet(u"")
        self.gridLayout_2 = QGridLayout(self.tab_bin)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 15, 0, 0)
        self.bin_plainTextEdit = QPlainTextEdit(self.tab_bin)
        self.bin_plainTextEdit.setObjectName(u"bin_plainTextEdit")
        self.bin_plainTextEdit.setStyleSheet(u"QPlainTextEdit\n"
"{\n"
"	font-family: 'JetBrains Mono';\n"
"	font-weight: 400;\n"
"	font-size: 18px;\n"
"	border: 1px solid #C4C4C4;\n"
"	border-radius: 16px;\n"
"	padding: 5px;\n"
"	background-color: #FAFAFA;\n"
"}")

        self.gridLayout_2.addWidget(self.bin_plainTextEdit, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_bin, "")

        self.verticalLayout_4.addWidget(self.tabWidget)


        self.right_lt.addWidget(self.editor)


        self.horizontalLayout_3.addLayout(self.right_lt)


        self.main_lt.addWidget(self.main_frame_lt)

        Main.setCentralWidget(self.centralwidget)

        self.retranslateUi(Main)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Main)
    # setupUi

    def retranslateUi(self, Main):
        Main.setWindowTitle(QCoreApplication.translate("Main", u"HEX files tools", None))
        self.name_prj.setText(QCoreApplication.translate("Main", u"\u0418\u043d\u0441\u0442\u0440\u0443\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439 \u0434\u043b\u044f \u0440\u0430\u0431\u043e\u0442\u044b \u0441 HEX-\u0444\u0430\u0439\u043b\u0430\u043c\u0438", None))
        self.files_title.setText(QCoreApplication.translate("Main", u"\u0424\u0430\u0439\u043b\u044b", None))
        self.btn_file_1.setText(QCoreApplication.translate("Main", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.btn_file_2.setText(QCoreApplication.translate("Main", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.btn_file_3.setText(QCoreApplication.translate("Main", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.btn_file_4.setText(QCoreApplication.translate("Main", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.btn_file_5.setText(QCoreApplication.translate("Main", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.tools_title.setText(QCoreApplication.translate("Main", u"\u0418\u043d\u0441\u0442\u0440\u0443\u043c\u0435\u043d\u0442\u044b", None))
        self.btn_merge.setText(QCoreApplication.translate("Main", u"\u041e\u0431\u044a\u0435\u0434\u0438\u043d\u0438\u0442\u044c", None))
#if QT_CONFIG(shortcut)
        self.btn_merge.setShortcut(QCoreApplication.translate("Main", u"Ctrl+M", None))
#endif // QT_CONFIG(shortcut)
        self.reg_title.setText(QCoreApplication.translate("Main", u"\u0420\u0435\u0433\u0438\u043e\u043d\u044b hex-\u0444\u0430\u0439\u043b\u043e\u0432", None))
        self.btn_new_reg.setText(QCoreApplication.translate("Main", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.btn_del.setText(QCoreApplication.translate("Main", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
#if QT_CONFIG(shortcut)
        self.btn_del.setShortcut(QCoreApplication.translate("Main", u"Ctrl+D", None))
#endif // QT_CONFIG(shortcut)
        self.btn_exp_hex.setText(QCoreApplication.translate("Main", u"\u0432 hex", None))
        self.btn_exp_bin.setText(QCoreApplication.translate("Main", u"\u0432 bin", None))
        self.message_title.setText(QCoreApplication.translate("Main", u"\u0421\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f", None))
        self.message_label.setText(QCoreApplication.translate("Main", u"\u0422\u0443\u0442 \u0431\u0443\u0434\u0443\u0442 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b \u0440\u0430\u0431\u043e\u0442\u044b", None))
        self.editor_title.setText(QCoreApplication.translate("Main", u"\u0420\u0435\u0434\u0430\u043a\u0442\u043e\u0440", None))
        self.btn_save.setText(QCoreApplication.translate("Main", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
#if QT_CONFIG(shortcut)
        self.btn_save.setShortcut(QCoreApplication.translate("Main", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.lable_ofs_and_file.setText(QCoreApplication.translate("Main", u"\u0421\u043c\u0435\u0449\u0435\u043d\u0438\u0435 \u0440\u0435\u0433\u0438\u043e\u043d\u0430, \u0444\u0430\u0439\u043b\u0430 ...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_hex), QCoreApplication.translate("Main", u"hex", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_bin), QCoreApplication.translate("Main", u"bin", None))
    # retranslateUi

