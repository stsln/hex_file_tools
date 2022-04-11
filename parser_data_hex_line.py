import binascii

RECORD_MARK = ':'

# Record type hex line
TYPE_DATA = '00'
TYPE_END_OF_FILE = '01'
TYPE_EXTENDED_SEGMENT_ADDRESS = '02'
TYPE_START_SEGMENT_ADDRESS = '03'
TYPE_EXTENDED_LINEAR_ADDRESS = '04'
TYPE_STARTING_LINEAR_ADDRESS = '05'


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
    Class that stores the memory data, start and end address memory of a hex file
    """

    start_rec_adr = None
    end_rec_adr = None
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
            self.start_rec_adr = int(address, 16)
            self.amount_hex_line_data = int(len(data) / 2)
            self.flag_load = True
        for i in range(0, len(data), 2):
            self.bytes_data.append(int(data[i:i+2], 16) & 0xFF)
        self.end_rec_adr = int(address, 16)

    def gen_hex_lines(self,
                      start_load_offset: str = '0x0000', end_load_offset: str = '0xFFFF',
                      is_editor: bool = False) -> tuple[str, str]:
        """
        Function generates hex lines from memory to create or edit a file
        :param start_load_offset: hex lines start address
        :param end_load_offset: hex lines end address
        :param is_editor: means the text is intended for the editor
        :return: data of memory in hex lines or only data hex line and load offset address
        """
        load_offset_adr, hex_lines_mem = '', ''
        memory_data = str(binascii.b2a_hex(self.bytes_data))[2:-1]

        for line_number in range(int(self.total_amount_data / self.amount_hex_line_data)):
            load_offset = hex(self.start_rec_adr +
                              line_number * self.amount_hex_line_data)[2:].rjust(4, '0')
            if int(start_load_offset, 16) > int(load_offset, 16):
                continue
            elif int(end_load_offset, 16) < int(load_offset, 16):
                break
            data = memory_data[line_number * self.amount_hex_line_data * 2:
                               (line_number + 1) * self.amount_hex_line_data * 2]
            if is_editor:
                load_offset_adr += load_offset + '\n'
                hex_lines_mem += data + '\n'
            else:
                hex_lines_mem += create_hex_line(self.amount_hex_line_data, TYPE_DATA, data, load_offset)
        hex_lines_mem = hex_lines_mem[:-1]

        return load_offset_adr, hex_lines_mem


class MemList:
    """
    Class that stores a list of memory with functions to work with them
    """

    mem_list = None

    current_mem = None

    def __init__(self):
        """
        Function initializing an empty list of memory
        """
        self.mem_list = []
        self.current_mem = None

    def create_new_mem(self):
        """
        Function creating a new memory and adding to list of memory
        """
        self.current_mem = Mem()
        self.mem_list.append(self.current_mem)

    def gen_hex_lines(self):
        """
        Function generates hex lines of all memory list items
        :return: generated hex lines
        """
        hex_lines_mem_list = ''
        for mem_item in self.mem_list:
            hex_lines_mem_list += mem_item.gen_hex_lines()[1] + '\n'
        return hex_lines_mem_list[:-1]

    def get_hex_editor(self):
        """
        Function returns the disassembled memory list of the hex file in the form of two lines:
        the addresses of the memory list items data and the memory list items data
        :return: the addresses of the memory list items data and the memory list items data
        """
        load_offset_adr, region_data = '', ''
        for mem_list_item in self.mem_list:
            result_data = mem_list_item.gen_hex_lines(is_editor=True)
            load_offset_adr += result_data[0]
            region_data += result_data[1] + '\n'

        return load_offset_adr, region_data


class SegmentList:
    """
    Class that stores a lists of memory data and start offset address with functions to work with them
    """

    start_ofs_adr = None
    seg_list = None

    current_seg = None
    last_amount_data = None

    def __init__(self, ofs_adr: str):
        """
        Function for initializing an empty list of segments with offset start address filling
        :param ofs_adr: offset start address
        """
        self.seg_list = []
        self.start_ofs_adr = int(ofs_adr, 16)
        self.current_seg = None
        self.last_amount_data = None

    def create_new_seg(self):
        """
        Function creating a new memory list element and adding to list of segment
        """
        self.current_seg = MemList()
        self.seg_list.append(self.current_seg)

    def is_need_new_seg(self, current_amount_data: int) -> bool:
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
        if self.is_need_new_seg(current_amount_data):
            self.current_seg.current_mem.complete()
            self.create_new_seg()
            self.current_seg.create_new_mem()
            self.current_seg.current_mem.add_data(address, data)
        else:
            if self.current_seg.current_mem.end_rec_adr and \
                    self.current_seg.current_mem.end_rec_adr != int(address, 16) - current_amount_data:
                self.current_seg.current_mem.complete()
                self.current_seg.create_new_mem()
            self.current_seg.current_mem.add_data(address, data)
        self.last_amount_data = current_amount_data

    def gen_hex_lines(self):
        """
        Function generates hex lines of all segment memory lists
        :return: generated hex lines
        """
        hex_lines_mem_list = ''
        hex_lines_mem_list += create_hex_line(2, TYPE_EXTENDED_LINEAR_ADDRESS,
                                              self.start_ofs_adr)
        for mem_list_item in self.seg_list:
            hex_lines_mem_list += mem_list_item.gen_hex_lines() + '\n'
        return hex_lines_mem_list[:-1]

    def get_hex_editor(self):
        """
        Function returns the disassembled region of the hex file in the
        form of three lines: the initial offset of the region,
        the addresses of the region data and the region data for further
        work with them in the editor
        :return: the initial offset of the region, the addresses of the region data and the region data
        """
        region_adr = hex(self.start_ofs_adr)[2:].rjust(4, '0')
        load_offset_adr, region_data = '', ''
        for seg_item in self.seg_list:
            result_data = seg_item.get_hex_editor()
            load_offset_adr += result_data[0]
            region_data += result_data[1]

        return region_adr, load_offset_adr, region_data

    def save_hex_region(self, region_adr, load_offset_adr, region_data):
        """
        Функция сохраняет hex-регион, если произошли правки в редакторе
        """
        self.start_ofs_adr = int(region_adr, 16)
        self.seg_list.clear()
        self.last_amount_data = 0

        offset_adr, data = load_offset_adr.split(), region_data.split()

        flag_processing = True
        if len(offset_adr) == len(data):
            for i in range(len(data)):
                line_hex = create_hex_line(int(len(data[i]) / 2), TYPE_DATA, data[i], offset_adr[i])
                if not ProcessingHexLine(line_hex[1:]).parsing():
                    flag_processing = False
                    break
                self.add_data(offset_adr[i], data[i], int(len(data[i]) / 2))
        else:
            flag_processing = False

        if flag_processing:
            self.current_seg.current_mem.complete()

        return flag_processing


class RegionsList:
    """
    Class that stores lists of region data and
    starting liner address data with functions to work with them
    """

    reg_list = None
    start_liner_adr_data = None

    def __init__(self):
        """
        Function initializing an empty dictionary of hex file regions
        """
        self.reg_list = {}

    def create_new_reg(self, address: str) -> SegmentList:
        """
        Function of creating a new list of segments and adding to the list
        :param address: starting liner address data
        :return: new list of segments
        """
        tmp_reg = SegmentList(address)
        tmp_reg.create_new_seg()
        tmp_reg.current_seg.create_new_mem()
        self.reg_list[address] = tmp_reg
        return tmp_reg

    def create_start_liner_adr_data(self, data: str):
        """
        Function save starting liner address data as bytearray
        :param data: starting liner address data
        """
        self.start_liner_adr_data = bytearray()
        for i in range(0, len(data), 2):
            self.start_liner_adr_data.append(int(data[i:i+2], 16) & 0xFF)

    def get_count_regions(self) -> int:
        """
        Function returns the number of regions in the hex file
        :return: count regions hex file
        """
        return len(self.reg_list)

    def gen_hex(self, is_end: bool = False, save: bool = False,
                start_ofs_adr: str = '0x0000', end_ofs_adr: str = '0xFFFF'):
        """
        Function generates hex lines of all region memory lists
        :return: generated hex lines
        """
        hex_lines_seg_list = ''

        for reg_item, data_item in self.reg_list.items():
            if data_item.start_ofs_adr < int(start_ofs_adr, 16):
                continue
            elif data_item.start_ofs_adr <= int(end_ofs_adr, 16):
                hex_lines_seg_list += data_item.gen_hex_lines() + '\n'

        if is_end:
            hex_lines_seg_list += create_hex_line(4, TYPE_STARTING_LINEAR_ADDRESS, self.start_liner_adr_data)
            hex_lines_seg_list += create_hex_line(0, TYPE_END_OF_FILE)

        return hex_lines_seg_list

    def gen_bin(self):
        pass

    def save_hex_region(self, old_reg_adr, new_reg_adr, load_offset_adr, reg_data):
        """
        Функция сохраняет hex-регион, если произошли правки в редакторе и они без ошибок
        """
        reg_list_copy = self.reg_list.copy()
        flag_err = False
        reg_data = '5456'

        if new_reg_adr not in self.reg_list.keys() or new_reg_adr == old_reg_adr:
            if self.reg_list[old_reg_adr].save_hex_region(new_reg_adr, load_offset_adr, reg_data):
                if new_reg_adr != old_reg_adr:
                    self.reg_list[new_reg_adr] = self.reg_list.pop(old_reg_adr)
            else:
                self.reg_list = reg_list_copy.copy()
                flag_err = True
        else:
            flag_err = True

        if flag_err:
            print('There are errors in the edits made or the address of such an offset already exists!')
        else:
            print('The edits made have been saved successfully')


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
        data = ''

    rec_len = str(hex(record_len)[2:]).rjust(2, '0')
    hex_line = rec_len + load_offset + rec_typ + data
    chk_sum = str(hex(ProcessingHexLine(hex_line).get_crc_and_amount_data()[0])[2:]).rjust(2, '0')
    hex_line = (RECORD_MARK + hex_line + chk_sum + '\n').upper()
    return hex_line
