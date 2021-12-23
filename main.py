# import binascii

# Type record hex line
TYPE_DATA = 0
TYPE_END_OF_FILE = 1
TYPE_EXTENDED_SEGMENT_ADDRESS = 2
TYPE_START_SEGMENT_ADDRESS = 3
TYPE_EXTENDED_LINEAR_ADDRESS = 4
TYPE_STARTING_LINEAR_ADDRESS = 5


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

        for i in range(0, len(self.line_hex_file[:-3]), 2):
            sum_line = 0xFF & (sum_line + int(self.line_hex_file[:-3][i:i + 2], 16))
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
        check_sum_calc, amount_data = self.get_crc_and_amount_data()
        data = self.line_hex_file[8:8+amount_data*2]

        if check_sum_calc != check_sum or amount_data != rec_len:
            return not flag_return, 0, 0, 0, 0
        else:
            return flag_return, rec_typ, load_offset, data, amount_data


class RegionsList:
    regList = None

    def __init__(self):
        self.regList = []

    def create_new_region(self, address):
        tmp_reg = SegmentList(address)
        tmp_reg.create_new_seg()
        tmp_reg.current_sec.create_new_mem()
        self.regList.append(tmp_reg)
        return tmp_reg

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

    def create_new_seg(self):
        self.current_sec = SectionList()
        self.segList.append(self.current_sec)

    def is_need_new_seg(self, current_amount_data):
        if self.last_amount_data != current_amount_data and self.last_amount_data is not None:
            return True
        else:
            return False

    def add_data(self, address, data, current_amount_data):
        if self.is_need_new_seg(current_amount_data):
            self.current_sec.current_mem.complete()
            self.create_new_seg()
            self.current_sec.create_new_mem()
            self.current_sec.current_mem.add_data(address, data)
        else:
            if self.current_sec.current_mem.end_rec_address and \
                    self.current_sec.current_mem.end_rec_address != int(address, 16) - current_amount_data:
                self.current_sec.current_mem.complete()
                self.current_sec.create_new_mem()
            self.current_sec.current_mem.add_data(address, data)
        self.last_amount_data = current_amount_data


class SectionList:
    secList = None
    current_mem = None

    def __init__(self):
        self.secList = []
        self.current_mem = None

    def create_new_mem(self):
        self.current_mem = SectionMem()
        self.secList.append(self.current_mem)


class SectionMem:
    start_rec_address = None
    end_rec_address = None
    bytes_data = None
    size_mem = None
    flag_load = False

    def __init__(self):
        self.bytes_data = bytearray()

    def is_load(self):
        """
        Function check creating memory
        :return: True - memory created,
                 False - memory not created
        """
        return self.flag_load

    def complete(self):
        """
        Termination current memory and calculation data size
        :return:
        """
        if self.is_load():
            self.size_mem = self.bytes_data.__sizeof__()

    def add_data(self, address, data):
        """
        Adding data to current memory
        :param address:
        :param data:
        :return:
        """
        if not self.is_load():
            self.start_rec_address = int(address, 16)
            self.flag_load = True
        for i in range(0, len(data), 2):
            self.bytes_data.append(int(data[i:i+2], 16) & 0xFF)
        self.end_rec_address = int(address, 16)


class ParserHex:
    hexFilesList = []
    dataHexFiles = []

    def __init__(self, list_hex_files):
        self.hexFilesList = list_hex_files
        self.dataHexFiles = []

    def processing_files(self):
        for name_hex_file in self.hexFilesList:
            print('Processing file ' + name_hex_file + '.hex')
            try:
                data_hex_file = open(name_hex_file + '.hex', 'r')
                print('File has been successfully opened for processing')
                regions_hex = RegionsList()
                if self.processing_file_line_by_line(regions_hex, data_hex_file):
                    print('File has been processed successfully\n')
                    self.dataHexFiles.append(regions_hex)
                else:
                    print('Further processing of the file is impossible - the file is damaged!')
                data_hex_file.close()
            except FileNotFoundError:
                print('File not found\n')
                continue

    def processing_file_line_by_line(self, regions_hex_file, data_file):
        """
        Function hex file processing line by line
        :param regions_hex_file: list regions hex file
        :param data_file: data hex file
        :return: True - successful file processing,
                 False - file corrupted
        """
        current_seg = None

        for line_hex in data_file:
            is_good, type_rec, address, data, amount_data = ProcessingHexLine(line_hex[1:]).processing_line()
            if is_good:
                if TYPE_EXTENDED_LINEAR_ADDRESS == type_rec:
                    if current_seg:
                        current_seg.current_sec.current_mem.complete()
                    current_seg = regions_hex_file.create_new_region(data)
                elif TYPE_DATA == type_rec:
                    current_seg.add_data(address, data, amount_data)
                elif TYPE_STARTING_LINEAR_ADDRESS == type_rec:
                    continue
                elif TYPE_END_OF_FILE == type_rec:
                    if current_seg:
                        current_seg.current_sec.current_mem.complete()
                    return True
            else:
                return False

    def get_count_regions(self, number_hex_file):
        pass

    def get_region(self, number_hex_file, number_region):
        pass

    def gen_common_hex_file(self, number_hex_file, empty=0xFF):
        pass

    def gen_region_hex_file(self, data_region):
        pass

    def gen_hex_file(self, number_hex_file, empty=0xFF):
        pass


def main():
    print('Combining hex files into one\n')

    hexes = ParserHex(['name_hex_file_1', 'name_hex_file_2', 'name_hex_file_3'])

    hexes.processing_files()
    hexes.get_count_regions(number_hex_file=1)
    hexes.gen_common_hex_file(number_hex_file=2, empty=0xF0)
    hexes.gen_region_hex_file(hexes.get_region(number_hex_file=0, number_region=5))
    hexes.gen_hex_file(number_hex_file=2)


if __name__ == "__main__":
    main()
