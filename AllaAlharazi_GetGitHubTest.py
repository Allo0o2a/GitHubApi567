#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 20:32:15 2018

@author: allo0o2a
"""

import unittest
from unittest import mock
from AllaAlharazi_GetGitHub import get_info


class TestGetInfo(unittest.TestCase):
    @mock.patch('AllaAlharazi_GetGitHub.get_info')
    def testValidUser(self, mockedReq):
        mockedReq.return_value = [('AllaAlharazi_SSW467', 0), ('GitHubApi567', 27), ('Triangle567', 6)]
        self.assertEqual(get_info('allo0o2a'), [('AllaAlharazi_SSW467', 0), ('GitHubApi567', 27), ('Triangle567', 6)])
        mockedReq.return_value =  [('autobahn-js-built', 18), ('iot', 30), ('kevinwlu.github.io', 0), ('mpl_finance', 14)]
        self.assertEqual(get_info("kevinwlu"), [('autobahn-js-built', 18), ('iot', 30), ('kevinwlu.github.io', 0), ('mpl_finance', 14)])

    @mock.patch('AllaAlharazi_GetGitHub.get_info')    
    def testInvalidUser(self, mockedReq):
        mockedReq.return_value = 'Invalid GitHub Username'
        self.assertEqual(get_info('jsbfjejknejk'), 'Invalid GitHub Username')
        self.assertEqual(get_info(' '), 'Invalid GitHub Username')


if __name__ == '__main__':
    unittest.main()
