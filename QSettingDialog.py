# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\res\authSetting.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from asn_help import str_to_asn1

class Ui_Dialog_Setting(object):
    def setupUi(self, Dialog_Setting):
        Dialog_Setting.setObjectName("Dialog_Setting")
        Dialog_Setting.resize(392, 147)
        self.formLayout = QtWidgets.QFormLayout(Dialog_Setting)
        self.formLayout.setObjectName("formLayout")
        self.label_FirmCode = QtWidgets.QLabel(Dialog_Setting)
        self.label_FirmCode.setObjectName("label_FirmCode")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_FirmCode)
        self.lineEdit_FirmCode = QtWidgets.QLineEdit(Dialog_Setting)
        self.lineEdit_FirmCode.setObjectName("lineEdit_FirmCode")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_FirmCode)
        self.label_SerialNumber = QtWidgets.QLabel(Dialog_Setting)
        self.label_SerialNumber.setObjectName("label_SerialNumber")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_SerialNumber)
        self.lineEdit_SerialNumber = QtWidgets.QLineEdit(Dialog_Setting)
        self.lineEdit_SerialNumber.setObjectName("lineEdit_SerialNumber")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_SerialNumber)
        self.label_PrivateKey = QtWidgets.QLabel(Dialog_Setting)
        self.label_PrivateKey.setObjectName("label_PrivateKey")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_PrivateKey)
        self.lineEdit_PrivateKey = QtWidgets.QLineEdit(Dialog_Setting)
        self.lineEdit_PrivateKey.setObjectName("lineEdit_PrivateKey")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_PrivateKey)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_Load = QtWidgets.QPushButton(Dialog_Setting)
        self.pushButton_Load.setObjectName("pushButton_Load")
        self.horizontalLayout.addWidget(self.pushButton_Load)
        self.pushButton_Ok = QtWidgets.QPushButton(Dialog_Setting)
        self.pushButton_Ok.setObjectName("pushButton_Ok")
        self.horizontalLayout.addWidget(self.pushButton_Ok)
        self.formLayout.setLayout(4, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.lineEdit_CmActId = QtWidgets.QLineEdit(Dialog_Setting)
        self.lineEdit_CmActId.setObjectName("lineEdit_CmActId")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_CmActId)
        self.label_CmActId = QtWidgets.QLabel(Dialog_Setting)
        self.label_CmActId.setObjectName("label_CmActId")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_CmActId)

        self.retranslateUi(Dialog_Setting)
        self.pushButton_Ok.clicked.connect(Dialog_Setting.okClicked)
        self.pushButton_Load.clicked.connect(Dialog_Setting.loadClicked)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Setting)

    def retranslateUi(self, Dialog_Setting):
        _translate = QtCore.QCoreApplication.translate
        Dialog_Setting.setWindowTitle(_translate("Dialog_Setting", "setting"))
        self.label_FirmCode.setText(_translate("Dialog_Setting", "FirmCode"))
        self.label_SerialNumber.setText(_translate("Dialog_Setting", "SerialNumber"))
        self.label_PrivateKey.setText(_translate("Dialog_Setting", "PrivateKey"))
        self.pushButton_Load.setText(_translate("Dialog_Setting", "Load"))
        self.pushButton_Ok.setText(_translate("Dialog_Setting", "OK"))
        self.label_CmActId.setText(_translate("Dialog_Setting", "CmActId"))
		
class QSettingDialog(QtWidgets.QDialog, Ui_Dialog_Setting):
    def __init__(self, parent=None, setting=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setting = setting
        self.init()
        self.setWindowModality(QtCore.Qt.ApplicationModal)
    
    def init(self):
        if(self.setting != None):
            if(self.setting.contains("FirmCode")):
                self.lineEdit_FirmCode.setText("%d" % self.setting.value("FirmCode"))
            if(self.setting.contains("SerialNumber")):
                self.lineEdit_SerialNumber.setText("%s" % self.setting.value("SerialNumber").hex())
            if(self.setting.contains("PrivateKey")):
                self.lineEdit_PrivateKey.setText("0x%X" % self.setting.value("PrivateKey"))
            if(self.setting.contains("CmActId")):
                self.lineEdit_CmActId.setText("%s" % self.setting.value("CmActId").hex())
    
    def loadConfig(self, file):
        cfg = QtCore.QSettings(file, QtCore.QSettings.IniFormat)
        if(cfg.contains("FirmCode")):
            self.lineEdit_FirmCode.setText(cfg.value("FirmCode"))
        if(cfg.contains("SerialNumber")):
            self.lineEdit_SerialNumber.setText(cfg.value("SerialNumber"))
        if(cfg.contains("PrivateKey")):
            self.lineEdit_PrivateKey.setText(cfg.value("PrivateKey"))
        if(cfg.contains("CmActId")):
            self.lineEdit_CmActId.setText(cfg.value("CmActId"))
        
        #[General]
        for key in cfg.childKeys():
            self.setting.setValue(key, cfg.value(key))
        
        #[Replace]
        if(cfg.contains("Replace/Number")):
            replace_num = int(cfg.value("Replace/Number"))
            self.setting.setValue("Replace/Number", replace_num)
            for i in range(replace_num):
                if(("Replace_%d" % i) in cfg.childGroups()):
                    asn_type = cfg.value("Replace_%d/AsnType" % i)
                    path = cfg.value("Replace_%d/Path" % i)
                    val = cfg.value("Replace_%d/Value" % i)
                    val_type = cfg.value("Replace_%d/Type" % i)
                    self.setting.setValue("Replace_%d/AsnType" % i, asn_type)
                    self.setting.setValue("Replace_%d/Path" % i, path)
                    if(val_type == "bytes"):
                        self.setting.setValue("Replace_%d/Value" % i, str_to_asn1(bytes, val))
                    elif(val_type == "int"):
                        self.setting.setValue("Replace_%d/Value" % i, str_to_asn1(int, val))
                    elif(val_type == "str"):
                        self.setting.setValue("Replace_%d/Value" % i, str_to_asn1(str, val))
                        
    def loadClicked(self):
        file, filetype = QtWidgets.QFileDialog.getOpenFileName(filter="config文件 (*.cfg);;所有文件 (*.*)")
        if(file != ""):
            self.loadConfig(file)
    
    def okClicked(self):
        self.setting.setValue("FirmCode", int(self.lineEdit_FirmCode.text(), 10))
        self.setting.setValue("SerialNumber", bytes.fromhex(self.lineEdit_SerialNumber.text()))
        self.setting.setValue("PrivateKey", int(self.lineEdit_PrivateKey.text(), 16))
        self.setting.setValue("CmActId", bytes.fromhex(self.lineEdit_CmActId.text()))
        self.close()
        
    