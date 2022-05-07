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
        flag_err, mes_err = False, ' обработан'

        for file_name, file_path in hex_files_list.items():
            try:
                data_hex_file = open(file_path, 'r')
                regions_hex_file = parser_data_hex_line.RegionsList()
                if processing_file_line_by_line(data_hex_file, regions_hex_file):
                    self.data_hex_list[file_name] = regions_hex_file
                else:
                    flag_err, mes_err = True, ' поврежден'
                data_hex_file.close()
            except FileNotFoundError:
                flag_err, mes_err = True, ' не найден'
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

    def save_file(self, name_file: str = '', file_path: str = '', file_text: str = '',
                  merge_file: bool = False, export_file: bool = False, export_to_bin: bool = False):
        """
        Function save modified hex file or hex or bin text to file
        :param name_file: name of the file to be saved
        :param file_path: file path to save
        :param merge_file: True - hex text of merge files
        :param export_file: True - hex or bin text of export files
        :param export_to_bin: True - export file to bin
        :param file_text: hex or bin text
        """
        if name_file in self.data_hex_list.keys():
            file_text = self.data_hex_list[name_file].gen_hex(is_end=True)
        elif merge_file:
            file_path = 'merge' + str(random.randrange(10000)) + '.hex'
        elif export_file:
            file_path = 'export' + str(random.randrange(10000))
            if export_to_bin:
                file_path += '.bin'
            else:
                file_path += '.hex'
        else:
            file_path = 'hex_file' + str(random.randrange(10000)) + '.hex'

        hex_file = open(file_path, 'w')
        hex_file.write(file_text)
        hex_file.close()

    def merge(self, reg_list: dict = None, in_bin: bool = False) -> bool:
        """
        Function merge all or part of the hex files data
        :param reg_list: regions that need to be merged
        :param in_bin: means that you need to save to a bin file
        :return: True - merge successful, False - merge not successful
        """
        if reg_list:
            try:
                text_file_export = self.gen_hex(reg_list)
                if in_bin:
                    text_file_export = self.gen_bin(text_file_export)
                self.save_file(export_file=True, file_text=text_file_export, export_to_bin=in_bin)
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
            self.save_file(merge_file=True, file_text=text_hex_file_merge)
            return True

    def gen_hex(self, reg_list: dict) -> str:
        """
        The function converts regions from a dictionary to hex
        :param reg_list: regions to convert to hex
        :return: hex lines
        """
        text_hex = ''
        for reg, name_hex in reg_list.items():
            text_hex += self.data_hex_list[name_hex].reg_list[reg].gen_hex() + '\n'
        text_hex += parser_data_hex_line.create_hex_line(0, parser_data_hex_line.TYPE_END_OF_FILE)

        return text_hex

    @staticmethod
    def gen_bin(hex_lines: str) -> str:
        """
        Function converts the received hex lines into bin text
        :param hex_lines: hex lines
        :return: bin text
        """
        text_bin = ''
        for hex_line in hex_lines.split():
            text_bin += bin(int(hex_line[1:], 16))[2:].zfill(165) + '\n'

        return text_bin
