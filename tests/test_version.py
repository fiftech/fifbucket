from fifbucket import version
import re


def test_version():
    result = version.__version__
    assert re.match(r'^\d+\.\d+(\.\d+)$', result)
    assert isinstance(result, str), 'wrong type!'
    assert not isinstance(result, int), 'wrong type!'
