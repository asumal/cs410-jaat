import pylintanalzyer as PLA
import unittest

class Test_PylintAnalzyer(unittest.TestCase):
    def setup():
        pass

    def test_parse_pylint_line_00(self):
        """ Check that output is what is expected """
        actual_result = PLA.parse_pylint_line("34:F")
        self.assertEqual(actual_result, (34,"F"))

    def test_parse_pylint_line_01(self):
        """ Check that Value Error exception is raised """
        self.assertRaises(ValueError, PLA.parse_pylint_line, "asdf")

    def test_parse_pylint_output_00(self):
        """ Check output for a sample file """
        sample_input = ['************* Module test', '11:C', '1:W','4:C','5:E','6:R']
        actual_output = PLA.parse_pylint_output(sample_input)
        self.assertEqual(actual_output[11]['category'], 'C')
        print actual_output
        self.assertEqual(len(actual_output), 7)

    def test_pylint_analzyer_00(self):
        """ """

    def test_get_pylint_analysis_00(self):
        """ """

if __name__ == '__main__':
    # http://www.openp2p.com/pub/a/python/2004/12/02/tdd_pyunit.html#getting-started
    suite = unittest.TestLoader().loadTestsFromTestCase(Test_PylintAnalzyer)
    unittest.TextTestRunner(verbosity=2).run(suite)
