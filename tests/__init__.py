import unittest
from .test_views import TestViews
from .test_ibeacons import TestIBeacon


def suite():
    """
    Define suite
    """
    test_suite = unittest.TestSuite()
    test_suite.addTests([
        unittest.TestLoader().loadTestsFromTestCase(TestViews),
        unittest.TestLoader().loadTestsFromTestCase(TestIBeacon),
    ])
    return test_suite


if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
