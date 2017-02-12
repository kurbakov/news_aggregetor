import unittest

from backend.classes import class_parser


class TestFoo(unittest.TestCase):

    # parse_string
    def test_read_file(self):
        self.assertDictEqual(class_parser.Parser.parse_string('{}'), dict())


suite = unittest.TestLoader().loadTestsFromTestCase(TestFoo)
unittest.TextTestRunner(verbosity=1).run(suite)
