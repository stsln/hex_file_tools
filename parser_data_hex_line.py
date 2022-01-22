import binascii


class ProcessingHexLine:
    """
    Class processing accepted hex line
    """
    def __init__(self, line_hex):
        self.line_hex_file = line_hex

    def get_crc_and_amount_data(self):
        """
        Function calculating and returning CRC hex line and amounts of data
        :return: number_calc_checksum: calculated CRC hex line
                 amount_data: amount data hex line
        """
        number_calc_checksum = 0x0100  # Number calculate CRC
        sum_line = 0
        amount_data = 0

        for i in range(0, len(self.line_hex_file), 2):
            sum_line = 0xFF & (sum_line + int(self.line_hex_file[i:i + 2], 16))
            amount_data += 1

        number_calc_checksum = 0xFF & (number_calc_checksum - sum_line)
        amount_data -= 4

        return number_calc_checksum, amount_data

    def processing_line(self):
        """
        Function hex line processing
        :return: flag_return: True - successful processing hex line,
                              False - corrupted hex line
                 type: type record
                 address: offset address
                 data: data hex line
                 amount_data: amount data hex line
        """
        flag_return = True
        rec_len = int(self.line_hex_file[:2], 16)
        load_offset = self.line_hex_file[2:6]
        rec_typ = int(self.line_hex_file[6:8], 16)
        check_sum = int(self.line_hex_file[-3:], 16)
        self.line_hex_file = self.line_hex_file[:-3]
        check_sum_calc, amount_data = self.get_crc_and_amount_data()
        data = self.line_hex_file[8:]

        if check_sum_calc != check_sum or amount_data != rec_len:
            return not flag_return, 0, 0, 0, 0
        else:
            return flag_return, rec_typ, load_offset, data, amount_data


class RegionsList:
    regList = None
    data_starting_liner_address = None

    def __init__(self):
        self.regList = []

    def create_new_region(self, address):
        tmp_reg = SegmentList(address)
        tmp_reg.create_new_sec_list()
        tmp_reg.current_sec.create_new_mem_sec()
        self.regList.append(tmp_reg)
        return tmp_reg

    def create_data_starting_liner_address(self, data):
        self.data_starting_liner_address = bytearray()
        for i in range(0, len(data), 2):
            self.data_starting_liner_address.append(int(data[i:i+2], 16) & 0xFF)

    def get_binary(self, start_adr, end_adr):
        pass

    def gen_hex(self):
        pass

    def gen_binary(self, empty=0xFFFF):
        pass


class SegmentList:
    start_ofs_address = None

    segList = None
    current_sec = None
    last_amount_data = None

    def __init__(self, ofs_address):
        self.segList = []
        self.start_ofs_address = int(ofs_address, 16)
        self.current_sec = None
        self.last_amount_data = None

    def create_new_sec_list(self):
        """
        Creating a new section list and adding to segment list
        """
        self.current_sec = SectionList()
        self.segList.append(self.current_sec)

    def is_need_new_sec_list(self, current_amount_data: int) -> bool:
        """
        Function checks whether there is a need to create a new list of memory section
        :param current_amount_data: current data size
        :return: True - data size is not the same (need a new memory section list),
                 False - data size is the same (don't need a new memory section list)
        """
        if self.last_amount_data != current_amount_data and self.last_amount_data is not None:
            return True
        else:
            return False

    def add_data(self, address, data, current_amount_data):
        if self.is_need_new_sec_list(current_amount_data):
            self.current_sec.current_mem.complete()
            self.create_new_sec_list()
            self.current_sec.create_new_mem_sec()
            self.current_sec.current_mem.add_data(address, data)
        else:
            if self.current_sec.current_mem.end_rec_address and \
                    self.current_sec.current_mem.end_rec_address != int(address, 16) - current_amount_data:
                self.current_sec.current_mem.complete()
                self.current_sec.create_new_mem_sec()
            self.current_sec.current_mem.add_data(address, data)
        self.last_amount_data = current_amount_data


class SectionList:
    secList = None
    current_mem = None

    def __init__(self):
        """
        Function initializing an empty sections list
        """
        self.secList = []
        self.current_mem = None

    def create_new_mem_sec(self):
        """
        Function creating a new memory section and adding to section list
        """
        self.current_mem = SectionMem()
        self.secList.append(self.current_mem)


class SectionMem:
    start_rec_address = None
    end_rec_address = None
    bytes_data = None
    size_mem = None
    size_data = None
    flag_load = False

    def __init__(self):
        """
        Function initializing a new memory section, with the creation of an empty data bytearray
        """
        self.bytes_data = bytearray()

    def is_load(self) -> bool:
        """
        Function check creating memory section
        :return: True - memory section created,
                 False - memory section not created
        """
        return self.flag_load

    def complete(self):
        """
        Function completion of the current memory section and calculation of data length
        """
        if self.is_load():
            self.size_mem = len(self.bytes_data)

    def add_data(self, address: str, data: str):
        """
        Function adding data to current memory section
        :param address:
        :param data:
        :return:
        """
        if not self.is_load():
            self.start_rec_address = int(address, 16)
            self.size_data = int(len(data) / 2)
            self.flag_load = True
        for i in range(0, len(data), 2):
            self.bytes_data.append(int(data[i:i+2], 16) & 0xFF)
        self.end_rec_address = int(address, 16)

    def gen_hex_lines(self, start_load_offset: str = '0x0000', end_load_offset: str = '0xFFFF') -> str:
        """
        Function generates hex lines from memory section
        :param start_load_offset: address start hex lines
        :param end_load_offset: address end hex lines
        :return: data of memory section in hex lines
        """
        hex_lines = ""
        memory_section_data = str(binascii.b2a_hex(self.bytes_data))[2:-1]

        for line_number in range(int(self.size_mem / self.size_data)):
            rec_mark = ":"
            rec_len = str(hex(self.size_data)[2:]).rjust(2, '0')
            load_offset = hex(self.start_rec_address + line_number * self.size_data)[2:].rjust(4, '0')
            if int(start_load_offset, 16) > int(load_offset, 16):
                continue
            elif int(end_load_offset, 16) < int(load_offset, 16):
                break
            rec_typ = "00"
            data = memory_section_data[line_number * 32:(line_number + 1) * 32]
            hex_line = rec_len + load_offset + rec_typ + data
            chk_sum = str(hex(ProcessingHexLine(hex_line).get_crc_and_amount_data()[0])[2:]).rjust(2, '0')
            hex_lines += rec_mark + hex_line + chk_sum + "\n"
        hex_lines = hex_lines.upper()[:-1]
        return hex_lines
