import parser_hex_files

print('Combining hex files into one\n')

data_hex_files = parser_hex_files.ParserHex(['name_hex_file_1', 'name_hex_file_2', 'name_hex_file_3'])
data_hex_files.processing_files()
data_hex_files.get_count_regions(number_hex_file=1)
data_hex_files.gen_common_hex_file(number_hex_file=0, empty=0xF0)
data_hex_files.gen_region_hex_file(number_hex_file=0, number_region=0)
data_hex_files.gen_hex_file(number_hex_file=2)

region_adr, load_offset_adr, region_data = data_hex_files.hexFilesDataList[0].regList[2].get_text_hex_editor()
test = data_hex_files.hexFilesDataList[0].regList[2].gen_hex_lines()
