import unittest
from unittests import getTestCases

def suite():
    loader = unittest.TestLoader()

    cases_list = []
    for test_class in getTestCases():
        case = loader.loadTestsFromTestCase(test_class)
        cases_list.append(case)

    suite = unittest.TestSuite(cases_list)
    return suite



