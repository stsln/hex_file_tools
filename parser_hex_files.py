import random
from collections import Counter

import parser_data_hex_line

# Record type hex line
TYPE_DATA = 0
TYPE_END_OF_FILE = 1
TYPE_EXTENDED_SEGMENT_ADDRESS = 2
TYPE_START_SEGMENT_ADDRESS = 3
TYPE_EXTENDED_LINEAR_ADDRESS = 4
TYPE_STARTING_LINEAR_ADDRESS = 5


def processing_file_line_by_line(data_file, reg_hex_file, current_reg=None) -> bool:
    """
    Function hex data processing line by line
    :param data_file: data hex file
    :param reg_hex_file: data hex file
    :param current_reg: current region
    :return: True - successful file processing,
             False - file corrupted
    """
    if isinstance(data_file, str):
        data_file = data_file.split()

    for line_hex in data_file:
        is_good, type_rec, address, data, amount_data = parser_data_hex_line.ProcessingHexLine(line_hex[1:]).parsing()
        if is_good:
            if TYPE_EXTENDED_LINEAR_ADDRESS == type_rec:
                if current_reg:
                    current_reg.current_seg.current_mem.complete()
                current_reg = reg_hex_file.create_new_reg(data)
            elif TYPE_DATA == type_rec:
                current_reg.add_data(address, data, amount_data)
            elif TYPE_STARTING_LINEAR_ADDRESS == type_rec:
                reg_hex_file.create_start_liner_adr_data(data)
            elif TYPE_END_OF_FILE == type_rec:
                if current_reg:
                    current_reg.current_seg.current_mem.complete()
                return True
        else:
            return False


class ParserHex:
    """
    Class processing accepted hex files
    """

    data_hex_list = {}

    def __init__(self):
        self.data_hex_list = {}

    def processing(self, hex_files_list: dict) -> tuple[bool, str]:
        """
        Function processing of hex files for availability and
        corruption or upon successful opening parsing data
        :param hex_files_list: list of files with name and path
        :return: flag_err: True - files successful, False - saving error
                 mes_err: error message
        """
        self.data_hex_list.clear()
        flag_err, mes_err = False, 'Файл обработан'

        for file_name, file_path in hex_files_list.items():
            try:
                data_hex_file = open(file_path, 'r')
                regions_hex_file = parser_data_hex_line.RegionsList()
                if processing_file_line_by_line(data_hex_file, regions_hex_file):
                    self.data_hex_list[file_name] = regions_hex_file
                else:
                    flag_err, mes = True, 'Файл поврежден'
                data_hex_file.close()
            except FileNotFoundError:
                flag_err, mes = True, 'Файл не найден'
                continue

        return flag_err, mes_err

    def get_adr_reg(self) -> dict:
        """
        Function for quickly getting all the offsets of file regions
        :return: hex_files_adr_reg_dict - dictionary, where the key is the name of the file,
                                          and the value is a list of addresses of offsets of regions
        """
        hex_files_adr_reg_dict = {}
        for name_hex_file, reg_list in self.data_hex_list.items():
            hex_files_adr_reg_dict[name_hex_file] = []
            for ofs_adr in reg_list.reg_list:
                hex_files_adr_reg_dict[name_hex_file].append(ofs_adr)

        return hex_files_adr_reg_dict

    def save_file(self, name_file: str = '', file_path: str = '', hex_file_text: str = '',
                  merge_file: bool = False, export_file: bool = False):
        """
        Function save modified hex file or hex text to file
        :param name_file: name of the file to be saved
        :param file_path: file path to save
        :param merge_file: True - hex text of merge files
        :param export_file: True - hex text of export files
        :param hex_file_text: hex text
        """
        if name_file in self.data_hex_list.keys():
            hex_file_text = self.data_hex_list[name_file].gen_hex(is_end=True)
        elif merge_file:
            file_path = 'merge' + str(random.randrange(10000)) + '.hex'
        elif export_file:
            file_path = 'export' + str(random.randrange(10000)) + '.hex'
        else:
            file_path = 'hex_file' + str(random.randrange(10000)) + '.hex'

        hex_file = open(file_path, 'w')
        hex_file.write(hex_file_text)
        hex_file.close()

    def merge(self, reg_list: dict = None) -> bool:
        """
        Function merge all or part of the hex files data
        :param reg_list: regions that need to be merged
        :return: True - merge successful, False - merge not successful
        """
        if reg_list:
            try:
                text_hex_file_merge = ''
                for reg, name_hex in reg_list.items():
                    text_hex_file_merge += self.data_hex_list[name_hex].reg_list[reg].gen_hex() + '\n'
                text_hex_file_merge += parser_data_hex_line.create_hex_line(0, parser_data_hex_line.TYPE_END_OF_FILE)
                self.save_file(export_file=True, hex_file_text=text_hex_file_merge)
                return True
            except FileNotFoundError:
                return False
        else:
            ofs_adr_list = []
            for _, reg_list in self.data_hex_list.items():
                for ofs_adr in reg_list.reg_list:
                    ofs_adr_list.append(ofs_adr)
            for ofs_adr, num_identical in Counter(ofs_adr_list).items():
                if num_identical > 1:
                    return False
            text_hex_file_merge = ''
            for _, reg_list in self.data_hex_list.items():
                text_hex_file_merge += reg_list.gen_hex()
            text_hex_file_merge += parser_data_hex_line.create_hex_line(0, parser_data_hex_line.TYPE_END_OF_FILE)
            self.save_file(merge_file=True, hex_file_text=text_hex_file_merge)
            return True
