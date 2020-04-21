from subprocess import PIPE, Popen

from cbeams import __version__


def call_process(command, expected_out=(), expected_err=()):
    process = Popen(command, shell=True, stdout=PIPE, stderr=PIPE)
    out, err = process.communicate()
    out = out.decode('unicode_escape')
    err = err.decode('unicode_escape')
    assert process.returncode == 0, '\nERR:%s\nOUT:%s' % (err, out)
    return out, err


def test_help():
    out, err = call_process('cbeams --help')
    assert 'cbeams v{}'.format(__version__) in out
    assert 'Usage:' in out

def test_version():
    out, _ = call_process('cbeams --version')
    assert __version__ in out

