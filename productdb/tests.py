import unittest
from testing import suite

if __name__ == '__main__':
    suite = suite()
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    #result = xmlrunner.XMLTestRunner(output='./metrics/tests/').run(suite)