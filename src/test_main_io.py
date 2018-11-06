import unittest
from main_io import get_relevant_data_from_file, get_stats, sort_and_print

# ? Use hypothesis for testing
# TODO Build acutally useful tests

class test_io(unittest.TestCase):
    def test_read_file_unit(self):
        pass

    def test_get_stats_unit(self):
        pass

    def test_print_file_unit(self):
        pass

    def test_successful_read_known_data(self):
        tmp = get_stats(get_relevant_data_from_file("../insight_testsuite/tests/test_1/input/h1b_input.csv")[1])
        assert tmp["CA"] == 10.0, "insight test; state CA percentage" + str(tmp["CA"]) + " invalid"



    def test_successful_read_known_big_data(self):
        tmp = get_stats(get_relevant_data_from_file("../input/H1B_FY_2016.csv")[1])
        assert f'{tmp["CA"]:.1f}' == "18.2", "insight test; state CA percentage" + str(tmp["CA"]) + " invalid"



    def test_estimate_scaling(self):
        pass


    def test_decimal_numbers_in_percent_display(self):
        pass