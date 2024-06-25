#Authors:     Tom Ruiter, Norbert Riefler
#Affiliation: Leibniz Institute for Materials Engineering, IWT, Bremen
#Licence:     MIT
#Version 1.00
from fbs_runtime.application_context.PyQt5 import ApplicationContext

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import os
import os.path
try:
    from PyQt5 import sip
except ImportError:
    import sip

import datetime
import sys


class Ui_Dialog(QWidget):

    def setupUi(self, Dialog):
        '''
        Definition of the whole programm, each widget is defined with its 
        dimensions and orietation inside the window.
        Also defines what functions are called when a button is clicked.
        '''
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 484)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox()
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Open|QtWidgets.QDialogButtonBox.Reset|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 391, 1040))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 2, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_20.setObjectName("label_20")
        self.gridLayout_2.addWidget(self.label_20, 25, 0, 1, 1)
        self.textEdit_20 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit_20.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_20.setObjectName("textEdit_20")
        self.gridLayout_2.addWidget(self.textEdit_20, 23, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_17.setObjectName("label_17")
        self.gridLayout_2.addWidget(self.label_17, 22, 0, 1, 1)
        self.textEdit_21 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit_21.setObjectName("textEdit_21")
        self.gridLayout_2.addWidget(self.textEdit_21, 8, 1, 1, 1)
        self.textEdit_5 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit_5.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_5.setObjectName("textEdit_5")
        self.gridLayout_2.addWidget(self.textEdit_5, 14, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_18.setObjectName("label_18")
        self.gridLayout_2.addWidget(self.label_18, 23, 0, 1, 1)
        self.textEdit_25 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit_25.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_25.setObjectName("textEdit")
        self.gridLayout_2.addWidget(self.textEdit_25, 20, 1, 1, 1)
        self.textEdit_11 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit_11.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_11.setObjectName("textEdit_11")
        self.gridLayout_2.addWidget(self.textEdit_11, 5, 1, 1, 1)
        self.textEdit_8 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit_8.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_8.setObjectName("textEdit_8")
        self.gridLayout_2.addWidget(self.textEdit_8, 11, 1, 1, 1)
        self.textEdit_6 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit_6.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_6.setObjectName("textEdit_6")
        self.gridLayout_2.addWidget(self.textEdit_6, 13, 1, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_22.setObjectName("label_22")
        self.gridLayout_2.addWidget(self.label_22, 8, 0, 1, 1)
        self.textEdit_12 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit_12.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_12.setObjectName("textEdit_12")
        self.gridLayout_2.addWidget(self.textEdit_12, 1, 1, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_19.setObjectName("label_19")
        self.gridLayout_2.addWidget(self.label_19, 24, 0, 1, 1)
        self.textEdit_16 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit_16.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_16.setObjectName("textEdit_16")
        self.gridLayout_2.addWidget(self.textEdit_16, 22, 1, 1, 1)
        self.textEdit_26 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit_26.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_26.setObjectName("textEdit_26")
        self.gridLayout_2.addWidget(self.textEdit_26, 16, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 11, 0, 1, 1)
        self.textEdit_18 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit_18.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_18.setObjectName("textEdit_18")
        self.gridLayout_2.addWidget(self.textEdit_18, 25, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 14, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 4, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 16, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 12, 0, 1, 1)
        self.textEdit_19 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit_19.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_19.setObjectName("textEdit_19")
        self.gridLayout_2.addWidget(self.textEdit_19, 24, 1, 1, 1)
        self.textEdit_15 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit_15.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_15.setObjectName("textEdit_15")
        self.gridLayout_2.addWidget(self.textEdit_15, 21, 1, 1, 1)
        self.textEdit_2 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit_2.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_2.setObjectName("textEdit_2")
        self.gridLayout_2.addWidget(self.textEdit_2, 18, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 18, 0, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_21.setObjectName("label_21")
        self.gridLayout_2.addWidget(self.label_21, 26, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 5, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_16.setObjectName("label_16")
        self.gridLayout_2.addWidget(self.label_16, 21, 0, 1, 1)
        self.textEdit_1 = QTextEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_1.sizePolicy().hasHeightForWidth())
        self.textEdit_1.setSizePolicy(sizePolicy)
        self.textEdit_1.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_1.setObjectName("textEdit_1")
        self.gridLayout_2.addWidget(self.textEdit_1, 0, 1, 1, 1)
        self.mydate = datetime.date.today()
        self.dateEdit = QtWidgets.QDateEdit(self.scrollAreaWidgetContents)
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(self.mydate.year, self.mydate.month, self.mydate.day), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout_2.addWidget(self.dateEdit, 9, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 1, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 19, 0, 1, 1)
        self.textEdit_17 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit_17.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_17.setObjectName("textEdit_17")
        self.gridLayout_2.addWidget(self.textEdit_17, 26, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 9, 0, 1, 1)
        self.textEdit_9 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit_9.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_9.setObjectName("textEdit_9")
        self.gridLayout_2.addWidget(self.textEdit_9, 12, 1, 1, 1)
        self.textEdit_14 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit_14.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_14.setObjectName("textEdit_14")
        self.gridLayout_2.addWidget(self.textEdit_14, 19, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 13, 0, 1, 1)
        self.textEdit_7 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit_7.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_7.setObjectName("textEdit_7")
        self.gridLayout_2.addWidget(self.textEdit_7, 2, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 20, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.textEdit_4 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit_4.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_4.setObjectName("textEdit_4")
        self.gridLayout_2.addWidget(self.textEdit_4, 4, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 10, 0, 1, 1)
        self.textEdit_3 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit_3.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_3.setObjectName("textEdit_3")
        self.gridLayout_2.addWidget(self.textEdit_3, 10, 1, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 1, 0, 1, 2)
        self.label_hardware = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_hardware.setObjectName("label_x")
        self.gridLayout_2.addWidget(self.label_hardware, 6, 0, 1, 1)
        self.textEdit_hardware = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit_hardware.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_hardware.setObjectName("textEdit_hardware")
        self.gridLayout_2.addWidget(self.textEdit_hardware, 6, 1, 1, 1)
        self.label_serial = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_serial.setObjectName("label_x")
        self.gridLayout_2.addWidget(self.label_serial, 7, 0, 1, 1)
        self.textEdit_serial = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit_serial.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_serial.setObjectName("textEdit_serial")
        self.gridLayout_2.addWidget(self.textEdit_serial, 7, 1, 1, 1)

        """
        How to add a field: 
        step1: definde a new label and textedit 
        """
        ################################################
        self.label_x = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_x.setObjectName("label_x")
        self.gridLayout_2.addWidget(self.label_x,27, 0, 1, 1)

        self.textEdit_x = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit_x.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_x.setObjectName("textEdit_x")
        self.gridLayout_2.addWidget(self.textEdit_x,27, 1, 1, 1)
        ################################################




        self.textEdit_1.setTabChangesFocus(True)
        self.textEdit_2.setTabChangesFocus(True)
        self.textEdit_3.setTabChangesFocus(True)
        self.textEdit_4.setTabChangesFocus(True)
        self.textEdit_5.setTabChangesFocus(True)
        self.textEdit_6.setTabChangesFocus(True)
        self.textEdit_7.setTabChangesFocus(True)
        self.textEdit_8.setTabChangesFocus(True)
        self.textEdit_9.setTabChangesFocus(True)
        self.textEdit_11.setTabChangesFocus(True)
        self.textEdit_12.setTabChangesFocus(True)
        self.textEdit_14.setTabChangesFocus(True)
        self.textEdit_15.setTabChangesFocus(True)
        self.textEdit_16.setTabChangesFocus(True)
        self.textEdit_17.setTabChangesFocus(True)
        self.textEdit_18.setTabChangesFocus(True)
        self.textEdit_19.setTabChangesFocus(True)
        self.textEdit_20.setTabChangesFocus(True)
        self.textEdit_21.setTabChangesFocus(True)
        self.textEdit_25.setTabChangesFocus(True)
        self.textEdit_26.setTabChangesFocus(True)
        self.textEdit_hardware.setTabChangesFocus(True)
        self.textEdit_serial.setTabChangesFocus(True)

        #Step 2
        ################################################
        self.textEdit_x.setTabChangesFocus(True)
        ################################################
        self._fileDirSaving = None
        self._fileDirOpen = None
        self._openFileNameDialog = None
        self._saveFileDialog = None
        self._data = None

        ################################################
        #self._keys = [  'Folder', 'Creator', 'Identifier', 'Software', 'Software_Version', 'Hardware',
        #        'Serialnumber', 'Description', 'Date', 'Subject', 'Title', 'Publisher',
        #        'PublicationYear', 'ResourceType', 'Contributer',
        #        'RelatedIdentifier', 'GeoLocation', 'Language', 'AlternateIdentifier',
        #        'Size', 'Format', 'Version', 'Rights', 'FundingReference']

        #Step 3
        self._keys = [  'Folder', 'Creator', 'Identifier', 'Software', 'Software_Version', 'Hardware',
                'Serialnumber', 'Description', 'Date', 'Subject', 'Title', 'Publisher',
                'PublicationYear', 'ResourceType', 'Contributer',
                'RelatedIdentifier', 'GeoLocation', 'Language', 'AlternateIdentifier',
                'Size', 'Format', 'Version', 'Rights', 'FundingReference','NewEntry']
        ################################################


        self._path = None
        self._fixedDir = True
        self._getIniPath = None
        



        self.retranslateUi(Dialog)
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Save).clicked.connect(self.saving)
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Reset).clicked.connect(self.reset)
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Open).clicked.connect(self.open)
        QtCore.QMetaObject.connectSlotsByName(Dialog)



        Dialog.setTabOrder(self.textEdit_1, self.textEdit_12)       # folder > creator
        Dialog.setTabOrder(self.textEdit_12, self.textEdit_7)       # creator > ident
        Dialog.setTabOrder(self.textEdit_7, self.textEdit_4)        # identifier > Software
        Dialog.setTabOrder(self.textEdit_4, self.textEdit_11)           # Software > software-version
        Dialog.setTabOrder(self.textEdit_11, self.textEdit_hardware)    # software-version > hardware
        Dialog.setTabOrder(self.textEdit_hardware, self.textEdit_serial)  # hardware > serialnumber
        Dialog.setTabOrder(self.textEdit_serial, self.textEdit_21)      # serialnumber > description
        Dialog.setTabOrder(self.textEdit_21, self.dateEdit)         # description > date
        Dialog.setTabOrder(self.dateEdit, self.textEdit_3)          # date > subject
        Dialog.setTabOrder(self.textEdit_3, self.textEdit_8)        # subject > title
        Dialog.setTabOrder(self.textEdit_8, self.textEdit_9)        # title > publisher
        Dialog.setTabOrder(self.textEdit_9, self.textEdit_6)        # publisher > publicationyear 
        Dialog.setTabOrder(self.textEdit_6, self.textEdit_5)        # publicationyear > resourcetype
        Dialog.setTabOrder(self.textEdit_5, self.textEdit_26)       # resourcetype > contributer
        Dialog.setTabOrder(self.textEdit_26, self.textEdit_2)       # contributer > relatedItentifier
        Dialog.setTabOrder(self.textEdit_2, self.textEdit_14)       # relatedItentifier > Geolocation
        Dialog.setTabOrder(self.textEdit_14, self.textEdit_25)      # Geolocation > language
        Dialog.setTabOrder(self.textEdit_25, self.textEdit_15)      # language > AlternateIdentifier
        Dialog.setTabOrder(self.textEdit_15, self.textEdit_16)      # AlternateIdentifier > Size
        Dialog.setTabOrder(self.textEdit_16, self.textEdit_20)      # Size > Format
        Dialog.setTabOrder(self.textEdit_20, self.textEdit_19)      # Format > Version
        Dialog.setTabOrder(self.textEdit_19, self.textEdit_18)      # Version > Rights
        Dialog.setTabOrder(self.textEdit_18, self.textEdit_17)      # Rights > FundingReference
        
        #step 4: set the new tab order
        ################################################
        Dialog.setTabOrder(self.textEdit_17, self.textEdit_x)
        ################################################


    def reset(self):
        '''
        Function which clears every Text widget in the program.
        '''
        try:
            self.textEdit_1.clear()
            self.textEdit_1.repaint()
            self.textEdit_2.clear()
            self.textEdit_2.repaint()
            self.textEdit_3.clear()
            self.textEdit_3.repaint()
            self.textEdit_4.clear()
            self.textEdit_4.repaint()
            self.textEdit_5.clear()
            self.textEdit_5.repaint()
            self.textEdit_6.clear()
            self.textEdit_6.repaint()
            self.textEdit_7.clear()
            self.textEdit_7.repaint()
            self.textEdit_8.clear()
            self.textEdit_8.repaint()
            self.textEdit_9.clear()
            self.textEdit_9.repaint()
            self.textEdit_11.clear()
            self.textEdit_11.repaint()
            self.textEdit_12.clear()
            self.textEdit_12.repaint()
            self.textEdit_14.clear()
            self.textEdit_14.repaint()
            self.textEdit_15.clear()
            self.textEdit_15.repaint()
            self.textEdit_16.clear()
            self.textEdit_16.repaint()
            self.textEdit_17.clear()
            self.textEdit_17.repaint()
            self.textEdit_18.clear()
            self.textEdit_18.repaint()
            self.textEdit_19.clear()
            self.textEdit_19.repaint()
            self.textEdit_20.clear()
            self.textEdit_20.repaint()
            self.textEdit_21.clear()
            self.textEdit_21.repaint()
            self.textEdit_25.clear()
            self.textEdit_25.repaint()
            self.textEdit_26.clear()
            self.textEdit_26.repaint()
            self.textEdit_hardware.clear()
            self.textEdit_hardware.repaint()
            self.textEdit_serial.clear()
            self.textEdit_serial.repaint()

            #step5
            ################################################
            self.textEdit_x.clear()
            self.textEdit_x.repaint()
            ################################################

            self.dateEdit.clear()
            self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(self.mydate.year, self.mydate.month, self.mydate.day), QtCore.QTime(0, 0, 0)))
            self.dateEdit.repaint()
        except:
            print('Cant clear Widgets')

     
    def retranslateUi(self, Dialog):
        '''
        Sets the text of all the labels in the widget
        '''
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog",  "Readme File Creator"))
        self.label_7.setText(_translate("Dialog",   "Identifier (ID: 1)"))
        self.label_20.setText(_translate("Dialog",  "Rights (ID: 16)"))
        self.label_17.setText(_translate("Dialog",  "Size (ID: 13)"))
        self.label_18.setText(_translate("Dialog",  "Format (ID: 14)"))
        self.label_22.setText(_translate("Dialog",  "Description (ID: 17)"))
        self.label_19.setText(_translate("Dialog",  "Version (ID: 15)"))
        self.label_6.setText(_translate("Dialog",   "Title (ID: 3)"))
        self.label.setText(_translate("Dialog",     "ResourceType (ID: 10)"))
        self.label_10.setText(_translate("Dialog",  "Software"))
        self.label_12.setText(_translate("Dialog",  "Contributer (ID: 7)"))
        self.label_5.setText(_translate("Dialog",   "Publisher (ID: 4)"))
        self.label_13.setText(_translate("Dialog",  "RelatedIdentifier (ID: 12)"))
        self.label_21.setText(_translate("Dialog",  "FundingReference (ID: 19)"))
        self.label_8.setText(_translate("Dialog",   "Software Version"))
        self.label_16.setText(_translate("Dialog",  "AlternateIdentifier (ID: 11)"))
        self.label_11.setText(_translate("Dialog",  "Creator (ID: 2)"))
        self.label_14.setText(_translate("Dialog",  "GeoLocation (ID: 18)"))
        self.label_9.setText(_translate("Dialog",   "Date (ID: 8)"))
        self.label_3.setText(_translate("Dialog",   "PublicationYear (ID: 5)"))
        self.label_15.setText(_translate("Dialog",  "Language (ID: 9)"))
        self.label_2.setText(_translate("Dialog",   "Folder"))
        self.label_4.setText(_translate("Dialog",   "Subject (ID: 6)"))
        self.dateEdit.setDisplayFormat(_translate("Dialog", "dd.MM.yyyy"))
        self.label_hardware.setText(_translate("Dialog",   "Hardware (ID: X)"))
        self.label_serial.setText(_translate("Dialog",   "Serialnumber (ID: X)"))

        # step 6
        ################################################
        self.label_x.setText(_translate("Dialog",   "New Entry (ID: X)"))
        ################################################


    def saveFileDialog(self):
        '''
        Function, which is responsible for the save menu.
        It opens up the save menu.
        '''

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog

        if self._fixedDir == False:
            if self.path is None:
                self.path = os.getcwd()
        else:
            if self.path is None:
                self.setFixedWorkingDir()

        #This is the main line responseble for the save menu. 
        #The function works as followed: QFileDialog.getSaveFileName(self, Headline,file_name, file_type, options)
        self._saveFileDialog, _ = QFileDialog.getSaveFileName(self,"Saving file","*.json","Select readme files (*.json)", options=options)

    
    def openFileNameDialog(self):
        '''
        Function, which is responsible for the open menu.
        '''

        if self._fixedDir == False:
            if self.path is None:
                self.path = os.getcwd()
        else:
            if self.path is None:
                self.setFixedWorkingDir()

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog

        #This is the main line responseble for the open menu. 
        #The function works as followed: QFileDialog.getOpenFileName(self, Headline,path_to_opened_directorie, file_type, options)
        self._openFileNameDialog, _ = QFileDialog.getOpenFileName(self,"Opening existing file",self.path,"Select readme files (*.json)", options=options)


    def setFixedWorkingDir(self):
        '''
        The function setFicedWorkingDir changes the current working directorie to a desired one. For this to work the variable
        self._fixedDir must be set so 'True'. 
        '''
        try:
            if self._fixedDir == True:
                self._setFixedWorkingDir = self.getIniPath()
                os.chdir(self._setFixedWorkingDir)
                self.path = self._setFixedWorkingDir
        except:
            print('Cant change to the fixed workding dir')


    def getIniPath(self):
        '''
        The function getIniPath tries to read the textfile 'ini.txt' to get the desired path from that file. If the file doenst seem 
        to work or it cant be opened the programm will use the path to the source files of the programm. If no 'ini.txt' can be found a 
        new file will be created at the location of the other source files.
        '''
        if os.path.isfile("ini.txt"):
            
            try:
                with open('ini.txt', 'r') as f:
                    return f.read()
            except:
                print('Cant open Ini-file.')
            
        else:
            with open('ini.txt', 'w') as f:
                f.write(os.getcwd())

            return os.getcwd()

    @property
    def data(self):
        #Data storage as a dictionary
        #Initializing dictionary
        if self._data is None:
            self._data = {}
        return self._data

    @property
    def path(self):
        return self._path
    
    @path.setter 
    def path(self,directory):
        self._path = directory

    def changedDir(self,path):
        while path[-1:] != '/':
            path = path[:-1]
        path = path.replace(os.sep, '\\')

        self.path = path
        return self.path
    
    def open(self):
        #Function, which opens a text file, reads it and displays the content in the 
        #widget. 
        try:
            self.reset()
            self.openFileNameDialog()
        
            f = open(self._openFileNameDialog,"r")
            lines = f.readlines()
            f.close

            
            opened_data = []
            for lin in range(len(lines)-2): 
                opened_data.append(lines[lin+1].split(':'))

            for lin in range(len(opened_data)):
                if opened_data[lin][0] in self._keys:
                
                    if opened_data[lin][0] == 'Folder':
                        self.textEdit_1.setText(opened_data[lin][1][1:-3])
                    if opened_data[lin][0] == 'RelatedIdentifier':
                        self.textEdit_2.setText(opened_data[lin][1][1:-3])
                    if opened_data[lin][0] == 'Subject':
                        self.textEdit_3.setText(opened_data[lin][1][1:-3])
                    if opened_data[lin][0] == 'Software':
                        self.textEdit_4.setText(opened_data[lin][1][1:-3])
                    if opened_data[lin][0] == 'ResourceType':
                        self.textEdit_5.setText(opened_data[lin][1][1:-3])
                    if opened_data[lin][0] == 'PublicationYear':
                        self.textEdit_6.setText(opened_data[lin][1][1:-3])
                    if opened_data[lin][0] == 'Identifier':
                        self.textEdit_7.setText(opened_data[lin][1][1:-3])
                    if opened_data[lin][0] == 'Title':
                        self.textEdit_8.setText(opened_data[lin][1][1:-3])
                    if opened_data[lin][0] == 'Publisher':
                        self.textEdit_9.setText(opened_data[lin][1][1:-3])
                    if opened_data[lin][0] == 'Software_Version':
                        self.textEdit_11.setText(opened_data[lin][1][1:-3])
                    if opened_data[lin][0] == 'Creator':
                        self.textEdit_12.setText(opened_data[lin][1][1:-3])
                    if opened_data[lin][0] == 'GeoLocation':
                        self.textEdit_14.setText(opened_data[lin][1][1:-3])
                    if opened_data[lin][0] == 'AlternateIdentifier':
                        self.textEdit_15.setText(opened_data[lin][1][1:-3])
                    if opened_data[lin][0] == 'Size':
                        self.textEdit_16.setText(opened_data[lin][1][1:-3])
                    if opened_data[lin][0] == 'FundingReference':
                        self.textEdit_17.setText(opened_data[lin][1][1:-3])
                    if opened_data[lin][0] == 'Rights':
                        self.textEdit_18.setText(opened_data[lin][1][1:-3])
                    if opened_data[lin][0] == 'Version':
                        self.textEdit_19.setText(opened_data[lin][1][1:-3])
                    if opened_data[lin][0] == 'Format':
                        self.textEdit_20.setText(opened_data[lin][1][1:-3])
                    if opened_data[lin][0] == 'Description':
                        self.textEdit_21.setText(opened_data[lin][1][1:-3])
                    if opened_data[lin][0] == 'Language':
                        self.textEdit_25.setText(opened_data[lin][1][1:-3])
                    if opened_data[lin][0] == 'Contributer':
                        self.textEdit_26.setText(opened_data[lin][1][1:-3])
                    if opened_data[lin][0] == 'Date':
                        self.dateEdit.setDate(QDate(int(opened_data[lin][1][1:5]), int(opened_data[lin][1][7:8]), int(opened_data[lin][1][9:11])))
                    if opened_data[lin][0] == 'Hardware':
                        self.textEdit_hardware.setText(opened_data[lin][1][1:-3])
                    if opened_data[lin][0] == 'Serialnumber':
                        self.textEdit_serial.setText(opened_data[lin][1][1:-3])
                    #step 7:
                    ################################################
                    if opened_data[lin][0] == 'NewEntry':
                        self.textEdit_x.setText(opened_data[lin][1][1:-3])
                    ################################################


        except:
            print('Cant open file.')

    def collectdata(self):
        #Function, which is called to store the data written in the widgets in a specific 
        #data storage. 
        try:
    
            if not self.textEdit_25.toPlainText():
                None
            else:
                self.data['Language'] = self.textEdit_25.toPlainText().rstrip()

            if not self.textEdit_1.toPlainText():
                None
            else:
                self.data['Folder'] = self.textEdit_1.toPlainText().rstrip()

            if not self.textEdit_2.toPlainText():
                None
            else:
                self.data['RelatedIdentifier'] = self.textEdit_2.toPlainText().rstrip()

            if not self.textEdit_3.toPlainText():
                None
            else:
                self.data['Subject'] = self.textEdit_3.toPlainText().rstrip()

            if not self.textEdit_4.toPlainText():
                None
            else:
                self.data['Software'] = self.textEdit_4.toPlainText().rstrip()

            if not self.textEdit_5.toPlainText():
                None
            else:
                self.data['ResourceType'] = self.textEdit_5.toPlainText().rstrip()

            if not self.textEdit_6.toPlainText():
                None
            else:
                self.data['PublicationYear'] = self.textEdit_6.toPlainText().rstrip()
 
            if not self.textEdit_7.toPlainText():
                None
            else:
                self.data['Identifier'] = self.textEdit_7.toPlainText().rstrip()

            if not self.textEdit_8.toPlainText():
                None
            else:
                self.data['Title'] = self.textEdit_8.toPlainText().rstrip()

            if not self.textEdit_9.toPlainText():
                None
            else:
                self.data['Publisher'] = self.textEdit_9.toPlainText().rstrip()

            if not self.textEdit_11.toPlainText():
                None
            else:
                self.data['Software_Version'] = self.textEdit_11.toPlainText().rstrip()

            if not self.textEdit_12.toPlainText():
                None
            else:
                self.data['Creator'] = self.textEdit_12.toPlainText().rstrip()

            if not self.textEdit_14.toPlainText():
                None
            else:
                self.data['GeoLocation'] = self.textEdit_14.toPlainText().rstrip()

            if not self.textEdit_15.toPlainText():
                None
            else:
                self.data['AlternateIdentifier'] = self.textEdit_15.toPlainText().rstrip()

            if not self.textEdit_16.toPlainText():
                None
            else:
                self.data['Size'] = self.textEdit_16.toPlainText().rstrip()

            if not self.textEdit_17.toPlainText():
                None
            else:
                self.data['FundingReference'] = self.textEdit_17.toPlainText().rstrip()

            if not self.textEdit_18.toPlainText():
                None
            else:
                self.data['Rights'] = self.textEdit_18.toPlainText().rstrip()

            if not self.textEdit_19.toPlainText():
                None
            else:
                self.data['Version'] = self.textEdit_19.toPlainText().rstrip()

            if not self.textEdit_20.toPlainText():
                None
            else:
                self.data['Format'] = self.textEdit_20.toPlainText().rstrip()

            if not self.textEdit_21.toPlainText():
                None
            else:
                self.data['Description'] = self.textEdit_21.toPlainText().rstrip()

            if not self.textEdit_26.toPlainText():
                None
            else:
                self.data['Contributer'] = self.textEdit_26.toPlainText().rstrip()

            if not self.dateEdit.date():
                None
            else:
                self.data['Date'] = self.dateEdit.date().toPyDate().strftime('%Y-%m-%d')

            if not self.textEdit_hardware.toPlainText():
                None
            else:
                self.data['Hardware'] = self.textEdit_hardware.toPlainText().rstrip()

            if not self.textEdit_serial.toPlainText():
                None
            else:
                self.data['Serialnumber'] = self.textEdit_serial.toPlainText().rstrip()        

        #step 8
        ################################################
  
            if not self.textEdit_x.toPlainText():
                None
            else:
                self.data['NewEntry'] = self.textEdit_x.toPlainText().rstrip()
        ################################################

        except:
                print('Problem')  
        


    def saving(self):
        #Function, which creates a file with all the data written in the widget and saves it 
        # at a directory choosen by the user. 

        self.collectdata()
        try: 
            self.saveFileDialog()
            with open(self._saveFileDialog, 'w') as f:
                f.write('{\n')
                if 'Folder' in self.data:
                    f.write('Folder:' + '\"' + self.data['Folder'] + '\"' +',\n')
                if 'Creator' in self.data:
                    f.write('Creator:' + '\"' + self.data['Creator'] + '\"' +',\n')
                if 'Identifier' in self.data:
                    f.write('Identifier:' + '\"' + self.data['Identifier'] + '\"' +',\n')
                if 'Software' in self.data:
                    f.write('Software:' + '\"' + self.data['Software'] + '\"' +',\n')
                if 'Software_Version' in self.data:
                    f.write('Software_Version:' + '\"' + self.data['Software_Version'] + '\"' +',\n')
                if 'Hardware' in self.data:
                    f.write('Hardware:' + '\"' + self.data['Hardware'] + '\"' +',\n')
                if 'Serialnumber' in self.data:
                    f.write('Serialnumber:' + '\"' + self.data['Serialnumber'] + '\"' +',\n') 
                if 'Description' in self.data:
                    f.write('Description:' + '\"' + self.data['Description'] + '\"' + ',\n')
                if 'Date' in self.data:
                    f.write('Date:' + '\"' + self.data['Date'] + '\"' +',\n')
                if 'Subject' in self.data:
                    f.write('Subject:' + '\"' + self.data['Subject'] + '\"' +',\n')
                if 'Title' in self.data:
                    f.write('Title:' + '\"' + self.data['Title'] + '\"' +',\n')
                if 'Publisher' in self.data:
                    f.write('Publisher:' + '\"' + self.data['Publisher'] + '\"' +',\n')
                if 'PublicationYear' in self.data:
                    f.write('PublicationYear:' + '\"' + self.data['PublicationYear'] + '\"' +',\n')
                if 'ResourceType' in self.data:
                    f.write('ResourceType:' + '\"' + self.data['ResourceType'] + '\"' +',\n')
                if 'Contributer' in self.data:
                    f.write('Contributer:' + '\"' + self.data['Contributer'] + '\"' +',\n')
                if 'RelatedIdentifier' in self.data:
                    f.write('RelatedIdentifier:' + '\"' + self.data['RelatedIdentifier'] + '\"' +',\n')
                if 'GeoLocation' in self.data:
                    f.write('GeoLocation:' + '\"' + self.data['GeoLocation'] + '\"' +',\n')
                if 'Language' in self.data:
                    f.write('Language:' + '\"' + self.data['Language'] + '\"' +',\n')
                if 'AlternateIdentifier' in self.data:
                    f.write('AlternateIdentifier:' + '\"' + self.data['AlternateIdentifier'] + '\"' +',\n')
                if 'Size' in self.data:
                    f.write('Size:' + '\"' + self.data['Size'] + '\"' +',\n')
                if 'Format' in self.data:
                    f.write('Format:' + '\"' + self.data['Format'] + '\"' +',\n')
                if 'Version' in self.data:
                    f.write('Version:' + '\"' + self.data['Version'] + '\"' +',\n')
                if 'Rights' in self.data:
                    f.write('Rights:' + '\"' + self.data['Rights'] + '\"' +',\n')
                if 'FundingReference' in self.data:
                    f.write('FundingReference:' + '\"' + self.data['FundingReference'] + '\"' +',\n')
           
                #step9
                ################################################
                if 'NewEntry' in self.data:
                    f.write('NewEntry:' + '\"' + self.data['NewEntry'] + '\"' +',\n')                
                ################################################


                f.write('}\n')
            print(os.getcwd())
            os.chdir(str(self.changedDir(self._saveFileDialog)))
            print(os.getcwd())

        except: 
            print('Cant save')

        




if __name__ == "__main__":
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    app = QtWidgets.QApplication(sys.argv)

    ex = Ui_Dialog()
    w = QtWidgets.QDialog()
    ex.setupUi(w)
    w.show()
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)

