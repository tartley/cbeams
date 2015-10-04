from unittest import TestCase
from unittest.mock import patch

from ..cmdline import parse


def get_expected_options():
    return {
        '--help': False,
        '--version': False,
    }


class CmdlineTest(TestCase):

    def test_no_args(self):
        self.assertEqual(parse([]), get_expected_options())

    def test_unrecognized(self):
        with self.assertRaises(SystemExit):
            parse(['--unrecognized'])

    def test_help(self):
        with patch('sys.stdout'):
            with self.assertRaises(SystemExit):
                parse(['--help'])

    def test_version(self):
        with patch('sys.stdout'):
            with self.assertRaises(SystemExit):
                parse(['--version'])

