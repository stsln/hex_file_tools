import parser_hex_files

print('HEX file tools\n')

name_hex_files = ['name_hex_file_1', 'name_hex_file_2', 'name_hex_file_3', 'common']
data_hex_files = parser_hex_files.ParserHex()
data_hex_files.processing(name_hex_files)
data_hex_files.hex_files_data_list['name_hex_file_2'].get_count_regions()
data_hex_files.hex_files_data_list['name_hex_file_1'].gen_hex(is_end=True)
data_hex_files.hex_files_data_list['name_hex_file_1'].reg_list['0810'].gen_hex_lines()

data_hex_files.merge()

reg_adr, load_offset_adr, reg_data = \
    data_hex_files.hex_files_data_list['name_hex_file_1'].reg_list['0810'].get_hex_editor()
data_hex_files.hex_files_data_list['name_hex_file_1'].save_hex_region('0810', reg_adr, load_offset_adr, reg_data)
data_hex_files.hex_files_data_list['name_hex_file_1'].delete('0811')
data_hex_files.hex_files_data_list['name_hex_file_1'].gen_hex(is_end=True, save=True)
