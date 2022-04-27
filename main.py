import os
import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QListWidgetItem
from PyQt6 import QtCore, uic
from PyQt6.QtGui import QFontDatabase

import parser_hex_files
from ui.design import Ui_Main

hex_files = {}
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
        self.ui.btn_file_1.clicked.connect(lambda: self.choose_file())
        self.ui.btn_file_2.clicked.connect(lambda: self.choose_file())
        self.ui.btn_file_3.clicked.connect(lambda: self.choose_file())
        self.ui.btn_file_4.clicked.connect(lambda: self.choose_file())
        self.ui.btn_file_5.clicked.connect(lambda: self.choose_file())

        # button merge
        self.ui.btn_merge.clicked.connect(lambda: self.merge())

        # buttons export
        self.ui.btn_exp_hex.clicked.connect(lambda: self.export())
        self.ui.btn_exp_bin.clicked.connect(lambda: self.export())

        # button add, save, delete region
        self.ui.btn_new_reg.clicked.connect(lambda: self.new_reg())
        self.ui.btn_save.clicked.connect(lambda: self.save())
        self.ui.btn_del.clicked.connect(lambda: self.delete())

        # regions list
        self.ui.reg_list.clicked.connect(lambda: self.edit_reg())

    def choose_file(self):
        object_name_btn = ['btn_file_1', 'btn_file_2', 'btn_file_3', 'btn_file_4', 'btn_file_5']
        btn_file = self.sender()

        if btn_file.objectName() in object_name_btn:
            file_path = QFileDialog.getOpenFileName(filter='*.hex')[0]
            file_name = os.path.basename(file_path)[0:-4]
            if file_name in hex_files.keys():
                self.ui.message_label.setText(file_name + ' уже добавлен')
            else:
                if file_name:
                    hex_files[file_name] = file_path

                    flag_err, mes_err = data_hex.processing(hex_files)
                    self.ui.message_label.setText(mes_err)
                    if flag_err:
                        del hex_files[file_name]
                    else:
                        if btn_file.text() != 'Добавить':
                            del hex_files[btn_file.text()]
                            del data_hex.data_hex_list[btn_file.text()]
                        btn_file.setText(file_name)
                        self.update_list_widget()

    def merge(self):
        pass

    def save(self):
        text = self.ui.hex_data_plainTextEdit.toPlainText()

    def delete(self):
        pass

    def export(self):
        pass

    def new_reg(self):
        pass

    def edit_reg(self):
        current_item = self.ui.reg_list.currentItem().text()
        if current_item:
            reg_adr, hex_name = current_item.split('|')
            reg_adr, load_ofs_adr, reg_data = data_hex.data_hex_list[hex_name[1:]].reg_list[reg_adr[:-1]].get_hex_editor()
            self.ui.text_ofs_reg.setPlainText(reg_adr)
            self.ui.hex_adr_plainTextEdit.setPlainText(load_ofs_adr)
            self.ui.hex_data_plainTextEdit.setPlainText(reg_data)
            self.ui.lable_ofs_and_file.setText('Смещение региона, файла ' + hex_name)

    def update_list_widget(self):
        regs_list = data_hex.get_adr_reg()
        self.ui.reg_list.clear()
        for name_file, reg_list in regs_list.items():
            for reg_adr in reg_list:
                item_list = QListWidgetItem()
                item_list.setCheckState(QtCore.Qt.CheckState.Unchecked)
                item_list.setText(reg_adr + ' | ' + name_file)
                self.ui.reg_list.addItem(item_list)

    @staticmethod
    def update_data():
        return data_hex.processing(hex_files)


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
