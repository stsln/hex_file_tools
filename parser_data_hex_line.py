import binascii

RECORD_MARK = ":"

# Record type hex line
TYPE_DATA = "00"
TYPE_END_OF_FILE = "01"
TYPE_EXTENDED_SEGMENT_ADDRESS = "02"
TYPE_START_SEGMENT_ADDRESS = "03"
TYPE_EXTENDED_LINEAR_ADDRESS = "04"
TYPE_STARTING_LINEAR_ADDRESS = "05"


class ProcessingHexLine:
    """
    Class processing accepted hex line
    """

    def __init__(self, hex_line: str):
        """
        Function initialization that stores the value of the hex line for further calculation
        """
        self.line_hex_file = hex_line

    def get_crc_and_amount_data(self):
        """
        Function calculating and returning CRC hex line and amounts of data
        :return: number_calc_checksum: calculated CRC hex line
                 amount_data: amount of data hex line
        """
        calc_checksum = 0x0100  # Number calculate CRC
        sum_line = 0
        amount_data = 0

        for i in range(0, len(self.line_hex_file), 2):
            sum_line = 0xFF & (sum_line + int(self.line_hex_file[i:i + 2], 16))
            amount_data += 1

        calc_checksum = 0xFF & (calc_checksum - sum_line)
        amount_data -= 4

        return calc_checksum, amount_data

    def parsing(self):
        """
        Function hex line parsing
        :return: flag_return: True - successful parsing hex line,
                              False - corrupted hex line
                 type: record type
                 address: offset address
                 data: hex line data
                 amount_data: hex line amount of data
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


class Mem:
    """
    Class that stores the memory data, start and end address memory of a hex file section
    """

    start_rec_address = None
    end_rec_address = None
    bytes_data = None
    total_amount_data = None
    amount_hex_line_data = None

    flag_load = False

    def __init__(self):
        """
        Function initializing a new memory, with the creation of an empty data bytearray
        """
        self.bytes_data = bytearray()

    def is_load(self) -> bool:
        """
        Function check creating memory
        :return: True - memory created,
                 False - memory not created
        """
        return self.flag_load

    def complete(self):
        """
        Function completion of the current memory and calculating the total amount of data
        """
        if self.is_load():
            self.total_amount_data = len(self.bytes_data)

    def add_data(self, address: str, data: str):
        """
        Function adding data to current memory
        :param address: address offset load hex line data
        :param data: hex line data
        """
        if not self.is_load():
            self.start_rec_address = int(address, 16)
            self.amount_hex_line_data = int(len(data) / 2)
            self.flag_load = True
        for i in range(0, len(data), 2):
            self.bytes_data.append(int(data[i:i+2], 16) & 0xFF)
        self.end_rec_address = int(address, 16)

    def gen_hex_lines(self, start_load_offset: str = '0x0000', end_load_offset: str = '0xFFFF') -> str:
        """
        Function generates hex lines from memory
        :param start_load_offset: hex lines start address
        :param end_load_offset: hex lines end address
        :return: data of memory in hex lines
        """
        hex_lines_mem = ""
        memory_section_data = str(binascii.b2a_hex(self.bytes_data))[2:-1]

        for line_number in range(int(self.total_amount_data / self.amount_hex_line_data)):
            load_offset = hex(self.start_rec_address +
                              line_number * self.amount_hex_line_data)[2:].rjust(4, '0')
            if int(start_load_offset, 16) > int(load_offset, 16):
                continue
            elif int(end_load_offset, 16) < int(load_offset, 16):
                break
            data = memory_section_data[line_number * self.amount_hex_line_data * 2:
                                       (line_number + 1) * self.amount_hex_line_data * 2]
            hex_lines_mem += create_hex_line(self.amount_hex_line_data, TYPE_DATA, data, load_offset)
        hex_lines_mem = hex_lines_mem[:-1]

        return hex_lines_mem


class MemList:
    """
    Class that stores a list of memory with functions to work with them.
    If there are several items in the list, then these are sections
    """

    memList = None

    current_mem = None

    def __init__(self):
        """
        Function initializing an empty list of memory
        """
        self.memList = []
        self.current_mem = None

    def create_new_mem(self):
        """
        Function creating a new memory and adding to list of memory
        """
        self.current_mem = Mem()
        self.memList.append(self.current_mem)

    def gen_hex_lines(self):
        """
        Function generates hex lines of all memory list items
        :return: generated hex lines
        """
        hex_lines_mem_list = ""
        for mem_item in self.memList:
            hex_lines_mem_list += mem_item.gen_hex_lines() + "\n"
        return hex_lines_mem_list[:-1]


class SegmentList:
    """
    Class that stores a lists of memory data and start offset address with functions to work with them
    """

    start_ofs_address = None
    segList = None

    current_mem_list = None
    last_amount_data = None

    def __init__(self, ofs_address: str):
        """
        Function for initializing an empty list of segments with offset start address filling
        :param ofs_address: offset start address
        """
        self.segList = []
        self.start_ofs_address = int(ofs_address, 16)
        self.current_mem_list = None
        self.last_amount_data = None

    def create_new_mem_list(self):
        """
        Function creating a new memory list element and adding to list of segment
        """
        self.current_mem_list = MemList()
        self.segList.append(self.current_mem_list)

    def is_need_new_mem_list(self, current_amount_data: int) -> bool:
        """
        Function checks whether there is a need to create a new list of memory
        :param current_amount_data: current amount of data
        :return: True - amount of data is not the same (need a new list of memory),
                 False - amount of data is the same (don't need a list of memory)
        """
        if self.last_amount_data != current_amount_data and self.last_amount_data is not None:
            return True
        else:
            return False

    def add_data(self, address: str, data: str, current_amount_data: int):
        """
        Function of adding data to the list of memory
        :param address: address of the hex line data load
        :param data: hex line data
        :param current_amount_data: current amount of data in the hex line
        """
        if self.is_need_new_mem_list(current_amount_data):
            self.current_mem_list.current_mem.complete()
            self.create_new_mem_list()
            self.current_mem_list.create_new_mem()
            self.current_mem_list.current_mem.add_data(address, data)
        else:
            if self.current_mem_list.current_mem.end_rec_address and \
                    self.current_mem_list.current_mem.end_rec_address != int(address, 16) - current_amount_data:
                self.current_mem_list.current_mem.complete()
                self.current_mem_list.create_new_mem()
            self.current_mem_list.current_mem.add_data(address, data)
        self.last_amount_data = current_amount_data

    def gen_hex_lines(self):
        """
        Function generates hex lines of all segment memory lists
        :return: generated hex lines
        """
        hex_lines_mem_list = ""
        hex_lines_mem_list += create_hex_line(2, TYPE_EXTENDED_LINEAR_ADDRESS,
                                              self.start_ofs_address)
        for mem_list_item in self.segList:
            hex_lines_mem_list += mem_list_item.gen_hex_lines() + "\n"
        return hex_lines_mem_list[:-1]


class RegionsList:
    """
    Class that stores a lists of segment data memory and
    starting liner address data with functions to work with them
    """

    regList = None
    starting_liner_address_data = None

    def __init__(self):
        """
        Function initializing an empty list of segment
        """
        self.regList = []

    def create_new_seg(self, address: str) -> SegmentList:
        """
        Function of creating a new list of segments and adding to the list
        :param address: starting liner address data
        :return: new list of segments
        """
        tmp_seg = SegmentList(address)
        tmp_seg.create_new_mem_list()
        tmp_seg.current_mem_list.create_new_mem()
        self.regList.append(tmp_seg)
        return tmp_seg

    def create_starting_liner_address_data(self, data: str):
        """
        Function save starting liner address data as bytearray
        :param data: starting liner address data
        """
        self.starting_liner_address_data = bytearray()
        for i in range(0, len(data), 2):
            self.starting_liner_address_data.append(int(data[i:i+2], 16) & 0xFF)

    def gen_hex_lines(self):
        """
        Function generates hex lines of all region memory lists
        :return: generated hex lines
        """
        hex_lines_seg_list = ""

        for seg_list_item in self.regList:
            hex_lines_seg_list += seg_list_item.gen_hex_lines() + "\n"

        hex_lines_seg_list += create_hex_line(4, TYPE_STARTING_LINEAR_ADDRESS,
                                              self.starting_liner_address_data)
        hex_lines_seg_list += create_hex_line(0, TYPE_END_OF_FILE)
        return hex_lines_seg_list

    def gen_binary(self):
        pass


def create_hex_line(record_len: int, rec_typ: str, data=None, load_offset: str = '0000') -> str:
    """
    Function of creating a hex line from the received data
    :param record_len: number of bytes of data in the record
    :param rec_typ: hex line record type
    :param data: memory data or offset address
    :param load_offset: offset that defines the data load address (by default, 0000 is not load offset)
    :return: created hex line
    """
    if isinstance(data, int):
        data = hex(data)[2:].rjust(4, '0')
    elif isinstance(data, bytearray):
        data = str(binascii.b2a_hex(data))[2:-1]
    elif isinstance(data, type(None)):
        data = ""

    rec_len = str(hex(record_len)[2:]).rjust(2, '0')
    hex_line = rec_len + load_offset + rec_typ + data
    chk_sum = str(hex(ProcessingHexLine(hex_line).get_crc_and_amount_data()[0])[2:]).rjust(2, '0')
    hex_line = (RECORD_MARK + hex_line + chk_sum + "\n").upper()

    return hex_line
