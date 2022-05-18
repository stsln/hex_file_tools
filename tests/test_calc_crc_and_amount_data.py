import pytest

from parser_data_hex_line import ProcessingHexLine


@pytest.mark.parametrize('line, good_crc, good_amount_data', [('1000000088660010753A10081513100829131008', 151, 16),
                                                              ('08029000E13A1008E13A1008', 0, 8),
                                                              ('0400000508103A75', 48, 4),
                                                              ('020000040810', 226, 2),
                                                              ('00000001', 255, 0)])
def test_calc_crc_and_amount_data(line, good_crc, good_amount_data):
    assert ProcessingHexLine(line).get_crc_and_amount_data() == (good_crc, good_amount_data)
