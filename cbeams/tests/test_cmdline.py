from unittest.mock import patch

import pytest

from ..cmdline import parse


def test_no_args():
    assert parse([]) == \
        {'--help': False, '--version': False, '--overwrite': False}

def test_unrecognized():
    with pytest.raises(SystemExit):
        parse(['--unrecognized'])

def test_help():
    with patch('sys.stdout'):
        with pytest.raises(SystemExit):
            parse(['--help'])

def test_version():
    with patch('sys.stdout'):
        with pytest.raises(SystemExit):
            parse(['--version'])

