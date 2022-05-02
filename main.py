import os
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QListWidgetItem, QPushButton, QToolButton
from PySide6 import QtCore, QtGui, QtWidgets

import parser_hex_files
from design import Ui_Main

hex_files = {}
data_hex = parser_hex_files.ParserHex()
select_file = {}


class ToolButtonFile(QtWidgets.QWidget):
    def __init__(self, obj_name, path_icon, parent=None):
        super(ToolButtonFile, self).__init__(parent)

        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)

        self.file_btn = QToolButton(parent)
        self.file_btn.setObjectName(obj_name)
        self.file_btn.setIcon(QtGui.QIcon(path_icon))
        self.file_btn.setIconSize(QtCore.QSize(60, 60))
        self.file_btn.setMinimumSize(QtCore.QSize(120, 120))
        self.file_btn.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.file_btn.setText('Добавить')
        self.file_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.file_btn.setChecked(False)
        self.file_btn.setSizePolicy(size_policy)
        size_policy.setHeightForWidth(self.file_btn.sizePolicy().hasHeightForWidth())

        lt = QtWidgets.QVBoxLayout(self)
        lt.setSpacing(0)
        lt.setContentsMargins(0, 0, 0, 0)
        lt.addWidget(self.file_btn)

    def mousePressEvent(self, event):
        btn = event.button()
        if btn == QtCore.Qt.RightButton and self.file_btn.text() != 'Добавить':
            if self.file_btn.objectName() in select_file.keys():
                self.setStyleSheet('QToolButton {border: 1px solid #C4C4C4;}')
                select_file.clear()
            else:
                if select_file.keys():
                    select_file_keys = []
                    for select_ks in select_file.keys():
                        select_vls = select_file.get(select_ks)
                        select_vls.setStyleSheet('QToolButton {border: 1px solid #C4C4C4;}')
                        select_file_keys.append(select_ks)
                    for _ in select_file_keys:
                        del select_file[_]

                self.setStyleSheet('QToolButton {border: 1px solid #2F8DEC;}')
                select_file[self.file_btn.objectName()] = self


class WidgetFile(QtWidgets.QWidget):
    def __init__(self, obj_name, parent=None):
        super(WidgetFile, self).__init__(parent)

        self.btn = ToolButtonFile(obj_name, 'icons/file_off.png', self)

        vtv = QtWidgets.QVBoxLayout(self)
        vtv.addWidget(self.btn)
        vtv.setSpacing(0)
        vtv.setContentsMargins(0, 0, 0, 0)
        vtv.addStretch()

        self.btn_cls = QPushButton('r', self.btn.file_btn)
        self.btn_cls.setMinimumSize(30, 30)
        self.btn_cls.setMaximumSize(30, 30)
        self.btn_cls.move(1, 1)
        self.btn_cls.hide()
        self.btn_cls.setObjectName('btn_cls')
        self.btn_cls.setStyleSheet('#btn_cls {font-family: "Webdings"; font-weight: 400;'
                                   'border-radius: 15px; border-color: #fff}'
                                   '#btn_cls:hover   {color: white; background: rgba(229, 46, 46, 0.6);}'
                                   '#btn_cls:pressed {color: white; background: rgba(229, 46, 46, 0.8);}')


class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.ui = Ui_Main()
        self.ui.setupUi(self)

        wgt_fl_1 = WidgetFile('btn_file_1')
        btn_fl_1 = wgt_fl_1.btn.file_btn
        btn_fl_1_cls = wgt_fl_1.btn_cls

        wgt_fl_2 = WidgetFile('btn_file_2')
        btn_fl_2 = wgt_fl_2.btn.file_btn
        btn_fl_2_cls = wgt_fl_2.btn_cls

        wgt_fl_3 = WidgetFile('btn_file_3')
        btn_fl_3 = wgt_fl_3.btn.file_btn
        btn_fl_3_cls = wgt_fl_3.btn_cls

        wgt_fl_4 = WidgetFile('btn_file_4')
        btn_fl_4 = wgt_fl_4.btn.file_btn
        btn_fl_4_cls = wgt_fl_4.btn_cls

        wgt_fl_5 = WidgetFile('btn_file_5')
        btn_fl_5 = wgt_fl_5.btn.file_btn
        btn_fl_5_cls = wgt_fl_5.btn_cls

        self.ui.files_lt.addWidget(wgt_fl_1)
        self.ui.files_lt.addWidget(wgt_fl_2)
        self.ui.files_lt.addWidget(wgt_fl_3)
        self.ui.files_lt.addWidget(wgt_fl_4)
        self.ui.files_lt.addWidget(wgt_fl_5)

        QtGui.QFontDatabase.addApplicationFont('fonts/Inter-Regular.ttf')
        QtGui.QFontDatabase.addApplicationFont('fonts/Inter-Bold.ttf')
        QtGui.QFontDatabase.addApplicationFont('fonts/JetBrainsMono-Regular.ttf')

        # buttons file
        btn_fl_1.clicked.connect(lambda: self.choose_file(wgt_fl_1, btn_fl_1, btn_fl_1_cls))
        btn_fl_2.clicked.connect(lambda: self.choose_file(wgt_fl_2, btn_fl_2, btn_fl_2_cls))
        btn_fl_3.clicked.connect(lambda: self.choose_file(wgt_fl_3, btn_fl_3, btn_fl_3_cls))
        btn_fl_4.clicked.connect(lambda: self.choose_file(wgt_fl_4, btn_fl_4, btn_fl_4_cls))
        btn_fl_5.clicked.connect(lambda: self.choose_file(wgt_fl_5, btn_fl_5, btn_fl_5_cls))

        # buttons close file
        btn_fl_1_cls.clicked.connect(lambda: self.close_file(wgt_fl_1, btn_fl_1, btn_fl_1_cls))
        btn_fl_2_cls.clicked.connect(lambda: self.close_file(wgt_fl_2, btn_fl_2, btn_fl_2_cls))
        btn_fl_3_cls.clicked.connect(lambda: self.close_file(wgt_fl_3, btn_fl_3, btn_fl_3_cls))
        btn_fl_4_cls.clicked.connect(lambda: self.close_file(wgt_fl_4, btn_fl_4, btn_fl_4_cls))
        btn_fl_5_cls.clicked.connect(lambda: self.close_file(wgt_fl_5, btn_fl_5, btn_fl_5_cls))

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

    def choose_file(self, wgt_fl, btn_fl, btn_fl_cls):
        file_path = QtWidgets.QFileDialog.getOpenFileName(self, 'Выберите файл для добавления в список', '',
                                                          'Hex Files (*.hex)')[0]
        file_name = os.path.basename(file_path)[0:-4]
        msg_box = QMessageBox()
        msg_box.setWindowTitle('Добавление файла')
        msg_box.setText('Ошибка добавления файла')
        msg_box.setIcon(QMessageBox.Critical)
        if file_name in hex_files.keys():
            msg_box.setInformativeText('Файл ' + file_name + ' уже добавлен')
            msg_box.setDefaultButton(QMessageBox.Ok)
            msg_box.exec()
        else:
            if file_name:
                hex_files[file_name] = file_path
                flag_err, mes_err = data_hex.processing(hex_files)
                if flag_err:
                    del hex_files[file_name]
                    msg_box.setInformativeText('Файл ' + file_name + mes_err)
                    msg_box.setDefaultButton(QMessageBox.Ok)
                    msg_box.exec()
                else:
                    if btn_fl.text() != 'Добавить':
                        del hex_files[btn_fl.text()]
                        del data_hex.data_hex_list[btn_fl.text()]
                        if btn_fl.objectName() in select_file.keys():
                            wgt_fl.btn.setStyleSheet('QToolButton {border: 1px solid #C4C4C4;}')
                            select_file.clear()
                    btn_fl.setText(file_name)
                    btn_fl.setIcon(QtGui.QIcon('icons/file_on.png'))
                    btn_fl_cls.show()
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
        msg_box.setText('Данное действие невозможно выполнить')
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
                msg_box = QMessageBox()
                msg_box.setWindowTitle('Инструменты')
                msg_box.setText('Экспорт')
                if data_hex.merge(reg_list):
                    msg_box.setIcon(QMessageBox.Information)
                    msg_box.setInformativeText('Успешный экспорт')
                else:
                    msg_box.setIcon(QMessageBox.Warning)
                    msg_box.setInformativeText('Ошибка экспорта')
                msg_box.setDefaultButton(QMessageBox.Ok)
                msg_box.exec()
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
            flag_err = data_hex.data_hex_list[hex_name].save_hex_region(old_reg_adr, new_reg_adr,
                                                                        load_ofs_adr, reg_data)
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

    def close_file(self, wgt_fl, btn_file, btn_close):
        text = btn_file.text()
        del hex_files[text]
        self.update_data()
        self.update_list_widget()
        btn_file.setText('Добавить')
        btn_file.setIcon(QtGui.QIcon('icons/file_off.png'))
        btn_close.hide()
        if btn_file.objectName() in select_file.keys():
            wgt_fl.btn.setStyleSheet('QToolButton {border: 1px solid #C4C4C4;}')
            select_file.clear()

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
