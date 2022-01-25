import parser_data_hex_line

# Record type hex line
TYPE_DATA = 0
TYPE_END_OF_FILE = 1
TYPE_EXTENDED_SEGMENT_ADDRESS = 2
TYPE_START_SEGMENT_ADDRESS = 3
TYPE_EXTENDED_LINEAR_ADDRESS = 4
TYPE_STARTING_LINEAR_ADDRESS = 5


class ParserHex:
    """
    Class processing accepted hex files and type record hex line
    """
    hexFilesList = []  # List of accepted names hex files
    dataHexFiles = []  # Data processed hex files

    def __init__(self, list_hex_files):
        self.hexFilesList = list_hex_files
        self.dataHexFiles = []

    def processing_files(self):
        """
        Function processing of hex files for availability and corruption or upon successful opening parsing data
        """
        for name_hex_file in self.hexFilesList:
            print('Processing file ' + name_hex_file + '.hex')
            try:
                data_hex_file = open(name_hex_file + '.hex', 'r')
                print('File has been successfully opened for processing')
                if self.processing_file_line_by_line(data_hex_file):
                    print('File has been processed successfully\n')
                else:
                    print('Further processing of the file is impossible - the file is damaged!')
                data_hex_file.close()
            except FileNotFoundError:
                print('File not found\n')
                continue

    def processing_file_line_by_line(self, data_file):
        """
        Function hex file processing line by line
        :param data_file: data hex file
        :return: True - successful file processing,
                 False - file corrupted
        """
        current_seg = None
        regions_hex_file = parser_data_hex_line.RegionsList()

        for line_hex in data_file:
            is_good, type_rec, address, \
                data, amount_data = parser_data_hex_line.ProcessingHexLine(line_hex[1:]).processing_line()
            if is_good:
                if TYPE_EXTENDED_LINEAR_ADDRESS == type_rec:
                    if current_seg:
                        current_seg.current_mem_list.current_mem.complete()
                    current_seg = regions_hex_file.create_new_seg(data)
                elif TYPE_DATA == type_rec:
                    current_seg.add_data(address, data, amount_data)
                elif TYPE_STARTING_LINEAR_ADDRESS == type_rec:
                    regions_hex_file.create_starting_liner_address_data(data)
                elif TYPE_END_OF_FILE == type_rec:
                    if current_seg:
                        current_seg.current_mem_list.current_mem.complete()
                    self.dataHexFiles.append(regions_hex_file)
                    return True
            else:
                return False

    def get_count_regions(self, number_hex_file: int) -> int:
        """
        Function returns the number of regions in the hex file
        :param number_hex_file: number hex file
        :return: count regions hex file
        """
        return len(self.dataHexFiles[number_hex_file].regList)

    def gen_region_hex_file(self, number_hex_file, number_region):
        pass

    def gen_hex_file(self, number_hex_file, empty=0xFF):
        pass

    def gen_common_hex_file(self, number_hex_file, empty=0xFF):
        pass
