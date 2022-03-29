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

    hexFilesNameList = []
    hexFilesDataList = []

    def __init__(self, list_hex_files: list):
        self.hexFilesNameList = list_hex_files
        self.hexFilesDataList = []

    def processing_files(self):
        """
        Function processing of hex files for availability and
        corruption or upon successful opening parsing data
        """
        for name_hex_file in self.hexFilesNameList:
            print('Processing file ' + name_hex_file + '.hex')
            try:
                data_hex_file = open(name_hex_file + '.hex', 'r')
                print('File has been successfully opened for processing')
                if self.processing_file_line_by_line(name_hex_file, data_hex_file):
                    print('File has been processed successfully\n')
                else:
                    print('Further processing of the file is impossible - the file is damaged!')
                data_hex_file.close()
            except FileNotFoundError:
                print('File not found\n')
                continue

    def processing_file_line_by_line(self, name_hex_file, data_file) -> bool:
        """
        Function hex file processing line by line
        :param name_hex_file: name hex file
        :param data_file: data hex file
        :return: True - successful file processing,
                 False - file corrupted
        """
        current_seg = None
        regions_hex_file = parser_data_hex_line.RegionsList()
        regions_hex_file.name_hex_file = name_hex_file

        for line_hex in data_file:
            is_good, type_rec, address, \
                data, amount_data = parser_data_hex_line.ProcessingHexLine(line_hex[1:]).parsing()
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
                    self.hexFilesDataList.append(regions_hex_file)
                    return True
            else:
                return False

    def get_count_regions(self, number_hex_file: int) -> int:
        """
        Function returns the number of regions in the hex file
        :param number_hex_file: number hex file
        :return: count regions hex file
        """

        return len(self.hexFilesDataList[number_hex_file].regList)

    def gen_region_hex_file(self, number_hex_file, number_region):
        pass

    def gen_hex_file(self, number_hex_file, empty=0xFF):
        pass

    def gen_common_hex_file(self, number_hex_file, empty=0xFF):
        pass
