import os
import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QListWidgetItem
from PyQt6 import QtCore
from PyQt6.QtGui import QFontDatabase

import parser_hex_files
from ui.design import Ui_Main

name_hex_files = []
data_hex = parser_hex_files.ParserHex()


class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.ui = Ui_Main()
        self.ui.setupUi(self)

        QFontDatabase.addApplicationFont('ui/fonts/Inter-Regular.ttf')
        QFontDatabase.addApplicationFont('ui/fonts/Inter-Bold.ttf')
        QFontDatabase.addApplicationFont('ui/fonts/JetBrainsMono-Regular.ttf')

        # buttons file
        self.ui.btn_file_1.clicked.connect(lambda: self.add_file())
        self.ui.btn_file_2.clicked.connect(lambda: self.add_file())
        self.ui.btn_file_3.clicked.connect(lambda: self.add_file())
        self.ui.btn_file_4.clicked.connect(lambda: self.add_file())
        self.ui.btn_file_5.clicked.connect(lambda: self.add_file())

        # button merge
        self.ui.btn_merge.clicked.connect(lambda: self.merge())

        # buttons export
        self.ui.btn_exp_hex.clicked.connect(lambda: self.export())
        self.ui.btn_exp_bin.clicked.connect(lambda: self.export())

        # button add, save, delete region
        self.ui.btn_new_reg.clicked.connect(lambda: self.new_reg())
        self.ui.btn_save.clicked.connect(lambda: self.save())
        self.ui.btn_del.clicked.connect(lambda: self.delete())

    def add_file(self):
        name_btn_file = ['btn_file_1', 'btn_file_2', 'btn_file_3', 'btn_file_4', 'btn_file_5']
        btn_file = self.sender()

        if btn_file.objectName() in name_btn_file:
            file_name = os.path.basename(QFileDialog.getOpenFileName(filter='*.hex')[0])[0:-4]
            if file_name in name_hex_files:
                self.ui.message_label.setText(file_name + ' уже добавлен.')
            else:
                if file_name:
                    if btn_file.text() != 'Добавить':
                        name_hex_files.remove(btn_file.text())
                    name_hex_files.append(file_name)
                    btn_file.setText(file_name)
                    self.ui.message_label.setText(file_name + ' успешно добавлен.')
                else:
                    self.ui.message_label.setText('Отмена добавления')

        data_hex.processing(name_hex_files)
        reg_list = data_hex.get_adr_reg()
        for key, list in reg_list.items():
            for item in list:
                self.ui.reg_list.addItem(item + ' | ' + key)

    def merge(self):
        pass

    @staticmethod
    def processing(self):
        data_hex.processing(name_hex_files)

    def save(self):
        text = self.ui.hex_data_plainTextEdit.toPlainText()

    def delete(self):
        pass

    def export(self):
        pass

    def new_reg(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Main()
    window.show()

    sys.exit(app.exec())


"""
data_hex.data_hex_list['name_hex_file_2'].get_count_regions()

data_hex.data_hex_list['name_hex_file_1'].gen_hex(is_end=True)
data_hex.data_hex_list['name_hex_file_1'].reg_list['0810'].gen_hex()

reg_adr, load_ofs_adr, reg_data = data_hex.data_hex_list['name_hex_file_1'].reg_list['0810'].get_hex_editor()
data_hex.data_hex_list['name_hex_file_1'].save_hex_region('0810', reg_adr, load_ofs_adr, reg_data)

data_hex.data_hex_list['name_hex_file_1'].delete('0811')

data_hex.save_file('name_hex_file_1')

flag_merge, repeat_list = data_hex.merge()

adr_reg_list = data_hex.get_adr_reg()
"""
