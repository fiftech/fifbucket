from fifbucket.client import url_plus_query


def test_url_plus_query():
    url = 'http://www.google.cl/'
    query = 'query_string'
    result = url_plus_query(url=url, query=query, page=2)
    assert result == 'http://www.google.cl/?pagelen=100&q=query_string&page=2'
    assert result != 'http://www.google.cl/'
    assert isinstance(result, str), 'wrong type!'
    assert not isinstance(result, int), 'wrong type!'
