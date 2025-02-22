#!/usr/bin/env python
# coding: utf-8

from testing_config import BaseTestConfig
from unittest.mock import Mock, patch

import xumm

class TestXapp(BaseTestConfig):

    token: str = ''

    @classmethod
    def setUp(cls):
        xumm.api_key = cls.json_fixtures['api']['key']
        xumm.api_secret = cls.json_fixtures['api']['secret']
        cls.sdk = xumm.XummSdk()
    
    @patch('xumm.client.requests.get')
    def test_xapp_ott(cls, mock_get):
        print('should get xapp ott')

        mock_get.return_value = Mock(status_code=200)
        mock_get.return_value.json.return_value = cls.json_fixtures['xApp']['get']
        cls.assertEqual(cls.sdk.xapp.ott(cls.token).to_dict(), cls.json_fixtures['xApp']['get'])
