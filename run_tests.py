#!/usr/bin/env python2

import sys
import unittest
from tests.TopicTest import TopicTestCase, TopicNotCreateTestCase
from tests.MainTest import MainTestCase


if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(MainTestCase),
        unittest.makeSuite(TopicTestCase),
        unittest.makeSuite(TopicNotCreateTestCase)
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
