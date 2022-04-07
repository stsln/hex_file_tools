import parser_hex_files

print('HEX file tools\n')

data_hex_files = parser_hex_files.ParserHex()
data_hex_files.processing_files(['name_hex_file_1', 'name_hex_file_2', 'name_hex_file_3', 'common'])
data_hex_files.hexFilesDataList['name_hex_file_2'].get_count_regions()
data_hex_files.hexFilesDataList['name_hex_file_1'].gen_hex_lines()

data_hex_files.merge(empty=0xFF)

test1 = data_hex_files.hexFilesDataList['name_hex_file_1'].regList[0].gen_hex_lines()
region_adr, load_offset_adr, region_data = \
    data_hex_files.hexFilesDataList['name_hex_file_1'].regList[0].get_text_hex_editor()
flag = data_hex_files.hexFilesDataList['name_hex_file_1'].regList[0].\
    save_hex_region(region_adr, load_offset_adr, region_data)
test2 = data_hex_files.hexFilesDataList['name_hex_file_1'].regList[0].gen_hex_lines()
