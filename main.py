import os
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog, QListWidgetItem
from PySide6 import QtCore
from PySide6.QtGui import QFontDatabase

import parser_hex_files
from design import Ui_Main

hex_files = {}
data_hex = parser_hex_files.ParserHex()


class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.ui = Ui_Main()
        self.ui.setupUi(self)

        QFontDatabase.addApplicationFont('fonts/Inter-Regular.ttf')
        QFontDatabase.addApplicationFont('fonts/Inter-Bold.ttf')
        QFontDatabase.addApplicationFont('fonts/JetBrainsMono-Regular.ttf')

        # buttons file
        self.ui.btn_file_1.clicked.connect(lambda: self.choose_file(self.ui.btn_file_1))
        self.ui.btn_file_2.clicked.connect(lambda: self.choose_file(self.ui.btn_file_2))
        self.ui.btn_file_3.clicked.connect(lambda: self.choose_file(self.ui.btn_file_3))
        self.ui.btn_file_4.clicked.connect(lambda: self.choose_file(self.ui.btn_file_4))
        self.ui.btn_file_5.clicked.connect(lambda: self.choose_file(self.ui.btn_file_5))

        # button merge
        self.ui.btn_merge.clicked.connect(lambda: self.merge())

        # buttons export
        self.ui.btn_exp_hex.clicked.connect(lambda: self.export(in_hex=True))
        self.ui.btn_exp_bin.clicked.connect(lambda: self.export(in_bin=True))

        # button add, save, delete region
        self.ui.btn_new_reg.clicked.connect(lambda: self.add_new_reg())
        self.ui.btn_save.clicked.connect(lambda: self.save())
        self.ui.btn_del.clicked.connect(lambda: self.delete())

        # regions list
        self.ui.reg_list.clicked.connect(lambda: self.fill_editor())

        # checking for overflow text
        self.ui.text_ofs_reg.textChanged.connect(lambda: self.text_changed())

        # synchronized scrolling
        vs_adr = self.ui.hex_adr_plainTextEdit.verticalScrollBar()
        vs_data = self.ui.hex_data_plainTextEdit.verticalScrollBar()
        vs_adr.valueChanged.connect(lambda: self.change_scroll(vs_adr, vs_data))
        vs_data.valueChanged.connect(lambda: self.change_scroll(vs_data, vs_adr))

    def choose_file(self, btn_file):
        file_path = QFileDialog.getOpenFileName(self, 'Выберите файл для добавления в список', '',
                                                'Hex Files (*.hex)')[0]
        file_name = os.path.basename(file_path)[0:-4]
        if file_name in hex_files.keys():
            msg_box = QMessageBox()
            msg_box.setWindowTitle('Добавление файла')
            msg_box.setText('Ошибка добавления файла')
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setInformativeText('Файл ' + file_name + ' уже добавлен')
            msg_box.setDefaultButton(QMessageBox.Ok)
            msg_box.exec()
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
                    # изменить иконку кнопки
                    self.update_list_widget()

    def get_data_list_widget(self, check: bool = False):
        """
        :param check: regions that need to be merged
        """
        reg_list = {}
        flag_repeat = False
        for item_num in range(self.ui.reg_list.count()):
            item = self.ui.reg_list.item(item_num)
            if item.checkState() == QtCore.Qt.CheckState.Checked:
                reg_adr, hex_name = self.split_item_list_widget(item)
                if check:
                    if reg_adr in reg_list.keys():
                        flag_repeat = True
                        reg_list.clear()
                        break
                reg_list[reg_adr] = hex_name

        msg_box = QMessageBox()
        msg_box.setWindowTitle('Инструменты')
        msg_box.setText("Данное действие невозможно выполнить")
        msg_box.setIcon(QMessageBox.Warning)

        if flag_repeat:
            msg_box.setInformativeText('Выбраны одинаковые адреса регионов:\nизмените выбор или отредактируйте адреса')
            msg_box.setDefaultButton(QMessageBox.Ok)
            msg_box.exec()
        elif not reg_list:
            msg_box.setInformativeText('Не выбраны регионы для работы с ними')
            msg_box.setDefaultButton(QMessageBox.Ok)
            msg_box.exec()

        return reg_list

    def merge(self):
        msg_box = QMessageBox()
        msg_box.setWindowTitle('Инструменты')
        msg_box.setText('Объединение невозможно')
        msg_box.setIcon(QMessageBox.Warning)
        if self.has_files():
            if data_hex.merge():
                msg_box.setWindowTitle('Инструменты')
                msg_box.setText('Объединение')
                msg_box.setIcon(QMessageBox.Information)
                msg_box.setInformativeText('Успешное объединение')
            else:
                msg_box.setInformativeText('В файлах есть одинаковые адреса регионов: '
                                           'измените выбор или отредактируйте адреса')
            msg_box.setDefaultButton(QMessageBox.Ok)
            msg_box.exec()
        else:
            msg_box.setInformativeText('Добавьте файлы и повторите попытку')
            msg_box.setDefaultButton(QMessageBox.Ok)
            msg_box.exec()

    def delete(self):
        reg_list = self.get_data_list_widget()
        if reg_list:
            for reg_adr, name_file in reg_list.items():
                data_hex.data_hex_list[name_file].delete(reg_adr)
                data_hex.save_file(name_file, file_path=hex_files[name_file])
                self.update_data()
                self.update_list_widget()

    def export(self, in_hex=False, in_bin=False):
        if in_hex:
            reg_list = self.get_data_list_widget()
            if reg_list:
                if data_hex.merge(reg_list):
                    self.ui.message_label.setText('Успешное объединение')
                else:
                    self.ui.message_label.setText('Ошибка объединения')
        elif in_bin:
            # реализовать
            pass

    def add_new_reg(self):
        pass

    def save(self):
        if self.has_files():
            old_reg_adr, hex_name = self.split_item_list_widget(self.ui.reg_list.currentItem())
            new_reg_adr = self.ui.text_ofs_reg.toPlainText()
            load_ofs_adr = self.ui.hex_adr_plainTextEdit.toPlainText()
            reg_data = self.ui.hex_data_plainTextEdit.toPlainText()
            flag_err = data_hex.data_hex_list[hex_name].save_hex_region(old_reg_adr, new_reg_adr, load_ofs_adr, reg_data)
            msg_box = QMessageBox()
            msg_box.setWindowTitle('Инструменты')
            msg_box.setText('Сохранение')
            if flag_err:
                msg_box.setIcon(QMessageBox.Critical)
                msg_box.setInformativeText('В изменениях есть ошибки или \nадрес такого смещения уже существует')

            else:
                data_hex.save_file(hex_name, file_path=hex_files[hex_name])
                self.update_data()
                self.update_list_widget()
                msg_box.setIcon(QMessageBox.Information)
                msg_box.setInformativeText('Изменения были успешно сохранены')

            msg_box.setDefaultButton(QMessageBox.Ok)
            msg_box.exec()

    def fill_editor(self):
        if self.ui.reg_list.currentItem():
            reg_adr, hex_name = self.split_item_list_widget(self.ui.reg_list.currentItem())
            reg_adr, load_ofs_adr, reg_data = data_hex.data_hex_list[hex_name].reg_list[reg_adr].get_hex_editor()
            self.ui.text_ofs_reg.setPlainText(reg_adr)
            self.ui.hex_adr_plainTextEdit.setPlainText(load_ofs_adr)
            self.ui.hex_data_plainTextEdit.setPlainText(reg_data)
            self.ui.lable_ofs_and_file.setText('Смещение региона, файла ' + hex_name)
        else:
            self.ui.text_ofs_reg.setPlainText('')
            self.ui.hex_adr_plainTextEdit.setPlainText('')
            self.ui.hex_data_plainTextEdit.setPlainText('')
            self.ui.lable_ofs_and_file.setText('Смещение региона, файла ...')

    def update_list_widget(self):
        regs_list = data_hex.get_adr_reg()
        self.ui.reg_list.clear()
        for name_file, reg_list in regs_list.items():
            for reg_adr in reg_list:
                item_list = QListWidgetItem()
                item_list.setCheckState(QtCore.Qt.CheckState.Unchecked)
                item_list.setText(reg_adr + ' | ' + name_file)
                self.ui.reg_list.addItem(item_list)
        self.fill_editor()

    def text_changed(self):
        if len(self.ui.text_ofs_reg.toPlainText()) > 4:
            self.ui.text_ofs_reg.setPlainText(self.ui.text_ofs_reg.toPlainText()[0:4])

    @staticmethod
    def split_item_list_widget(item):
        if item:
            item_text = item.text()
            reg_adr, hex_name = item_text.split('|')
            return reg_adr[:-1], hex_name[1:]

    @staticmethod
    def update_data():
        return data_hex.processing(hex_files)

    @staticmethod
    def change_scroll(changed_scroll, change_scroll):
        change_scroll.setValue(changed_scroll.value())

    @staticmethod
    def has_files():
        if len(data_hex.data_hex_list) > 0:
            return True
        else:
            return False


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Main()
    window.show()

    sys.exit(app.exec())
