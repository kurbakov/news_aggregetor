import unittest

if __name__ == '__main__':
    testsuite = unittest.TestLoader().discover('./all_tests_files')
    unittest.TextTestRunner(verbosity=1).run(testsuite)
