import parser_hex_files

print('HEX file tools\n')

name_hex_files = ['name_hex_file_1', 'name_hex_file_2', 'name_hex_file_3']
data_hex = parser_hex_files.ParserHex()
data_hex.processing(name_hex_files)

"""
data_hex.data_hex_list['name_hex_file_2'].get_count_regions()

data_hex.data_hex_list['name_hex_file_1'].gen_hex(is_end=True)
data_hex.data_hex_list['name_hex_file_1'].reg_list['0810'].gen_hex()

reg_adr, load_ofs_adr, reg_data = data_hex.data_hex_list['name_hex_file_1'].reg_list['0810'].get_hex_editor()
data_hex.data_hex_list['name_hex_file_1'].save_hex_region('0810', reg_adr, load_ofs_adr, reg_data)

data_hex.data_hex_list['name_hex_file_1'].delete('0811')

data_hex.save_file('name_hex_file_1')

flag_merge, repeat_list = data_hex.merge()

adr_reg_list = data_hex.get_adr_reg()
"""
