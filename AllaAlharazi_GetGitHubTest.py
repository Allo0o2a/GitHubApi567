#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 20:32:15 2018

@author: allo0o2a
"""

import unittest

from AllaAlharazi_GetGitHub import get_info


class TestGetInfo(unittest.TestCase):
    
    def testValidUser(self):
        self.assertEqual(get_info('allo0o2a'), [('AllaAlharazi_SSW467', 0), ('GitHubApi567', 19), ('Triangle567', 6)])

    def testInvalidUser(self):
        self.assertEqual(get_info('jsbfjejknejk'), 'Invalid GitHub Username')
        self.assertEqual(get_info(' '), 'Invalid GitHub Username')


if __name__ == '__main__':
    unittest.main()
