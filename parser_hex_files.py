import parser_data_hex_line

# Record type hex line
TYPE_DATA = 0
TYPE_END_OF_FILE = 1
TYPE_EXTENDED_SEGMENT_ADDRESS = 2
TYPE_START_SEGMENT_ADDRESS = 3
TYPE_EXTENDED_LINEAR_ADDRESS = 4
TYPE_STARTING_LINEAR_ADDRESS = 5


def processing_file_line_by_line(data_file, regions_hex_file, current_seg=None) -> bool:
    """
    Function hex data processing line by line
    :param data_file: data hex file
    :param regions_hex_file: data hex file
    :param current_seg: current segment
    :return: True - successful file processing,
             False - file corrupted
    """
    if isinstance(data_file, str):
        data_file = data_file.split()

    for line_hex in data_file:
        is_good, type_rec, address, data, amount_data = parser_data_hex_line.ProcessingHexLine(line_hex[1:]).parsing()
        if is_good:
            if TYPE_EXTENDED_LINEAR_ADDRESS == type_rec:
                if current_seg:
                    current_seg.current_mem_list.current_mem.complete()
                current_seg = regions_hex_file.create_new_seg(data)
            elif TYPE_DATA == type_rec:
                current_seg.add_data(address, data, amount_data)
            elif TYPE_STARTING_LINEAR_ADDRESS == type_rec:
                regions_hex_file.create_start_liner_adr_data(data)
            elif TYPE_END_OF_FILE == type_rec:
                if current_seg:
                    current_seg.current_mem_list.current_mem.complete()
                return True
        else:
            return False


class ParserHex:
    """
    Class processing accepted hex files and type record hex line
    """

    hexFilesDataList = {}

    def __init__(self):
        self.hexFilesDataList = {}

    def processing_files(self, list_hex_files: list):
        """
        Function processing of hex files for availability and
        corruption or upon successful opening parsing data
        """
        self.hexFilesDataList.clear()

        for name_hex_file in list_hex_files:
            print('Processing file ' + name_hex_file + '.hex')
            try:
                data_hex_file = open(name_hex_file + '.hex', 'r')
                print('File has been successfully opened for processing')
                regions_hex_file = parser_data_hex_line.RegionsList()
                if processing_file_line_by_line(data_hex_file, regions_hex_file):
                    self.hexFilesDataList[name_hex_file] = regions_hex_file
                    print('File has been processed successfully\n')
                else:
                    print('Further processing of the file is impossible - the file is damaged!')
                data_hex_file.close()
            except FileNotFoundError:
                print('File not found\n')
                continue

    def merge(self, empty=0xFF):
        pass
