from reference_sequence_fetcher.fetcher import Fetcher, handle_error
import pytest
import json


class MockResponse(object):
    '''
    Mock object to test handle_error function in test_handle_error_function.
    It mocks the functionality of Response object from requests library
    '''
    def __init__(self, status_code, text=None):
        self.status_code = status_code
        self.text = text


def get_metadata(seq):
    '''Used to retrieve metadata of sequence object using checksum. Called from
    check_complete_metdata_response
    '''
    response = {
        "metadata": {
            "md5": seq.md5,
            "trunc512": seq.sha512,
            "length": seq.size,
            "aliases": []
        }
    }
    return json.dumps(response)


def check_complete_metdata_response(metadata, seq, checksum):
    '''check_complete_metdata_response is a utility function used by
    test_metadata function to remove duplication of code. It takes
    response seq object and checksum ID used to query as input parameter and
    assert for reponse header, status code and content
    '''

    assert metadata == get_metadata(seq)


def test_getter_setter_base_url_Fetcher():
    '''test all scenarios of the user putting in base_url along with str() on
    Fetcher object
    '''
    fetcher = Fetcher('111.11.1.0')
    assert fetcher.get_base_url() == 'http://111.11.1.0'

    fetcher.set_base_url('http://localhost')
    assert fetcher.get_base_url() == 'http://localhost'

    assert str(fetcher) == 'http://localhost'


def test_fetch_complete_sequence_retrieval(data, server):
    '''test the complete sequence retrieval
    '''
    fetcher = Fetcher(server)
    seq = data[0]
    assert fetcher.fetch_sequence(seq.md5) == seq.sequence
    assert Fetcher.sequence(server, seq.md5) == seq.sequence
    assert fetcher._Fetcher__cache is None


def test_fetch_sub_sequence_retrieval(data, server):
    '''test the sub sequence retrieval using start and end when end > start
    '''
    fetcher = Fetcher(server)
    seq = data[0]
    assert fetcher.fetch_sequence(seq.md5, start=0, end=10) \
        == seq.sequence[:10]
    assert fetcher.fetch_sequence(seq.md5, start=0, end=1) \
        == seq.sequence[:1]
    assert fetcher._Fetcher__cache is None


def test_fetch_sub_sequence_retrieval_one_parameter(data, server):
    '''test the sub sequence retrieval using start and end when only one of the
    start and end is given
    '''
    fetcher = Fetcher(server)
    seq = data[0]
    assert fetcher.fetch_sequence(seq.md5, end=5) == 'CCACA'
    assert fetcher._Fetcher__cache == \
        json.loads(get_metadata(seq))
    assert fetcher.fetch_sequence(seq.md5, start=0) == seq.sequence


def test_fetch_circular_sub_sequence_retrieval(data, server):
    '''test the sub sequence retrieval using start and end when end <= start
    '''
    fetcher = Fetcher(server)
    assert fetcher.fetch_sequence(data[2].md5, start=5374, end=5) == \
        'ATCCAACCTGCAGAGTT'
    assert fetcher._Fetcher__cache is None


@pytest.mark.parametrize("_input, _output", [
    (400, 'Check the parameters provided i.e start, end, fbs and lbs.'),
    (404, 'Checksum identifier provided can not be found.'),
    (415, 'Encoding is not supported by the server.'),
    (416, 'Range can not be satisfied.'),
    (500, 'There maybe some internal server error.')

])
def test_handle_error_function(server, _input, _output):
    '''Uses MockResponse object to test handle_error function
    '''
    with pytest.raises(Exception) as excinfo:
        handle_error(MockResponse(_input))
    assert str(excinfo.value) == _output


def test_warning_501_handle_error_function(server):
    '''Uses MockResponse object to test warning issued in case of 501 from
    handle_error function
    '''
    with pytest.warns(UserWarning, match='Circular support is not implemented in the server'):
        handle_error(MockResponse(501))


def test_metadata(server, data):
    '''Uses check_complete_metdata_response utility function to test metadata
    retrieval from fetch_metadata and Fetch.metadata using a mock server.
    '''
    seq = data[0]
    fetcher = Fetcher(server)
    check_complete_metdata_response(
        fetcher.fetch_metadata(seq.md5), seq, seq.md5)
    check_complete_metdata_response(
            Fetcher.metadata(server, seq.md5), seq, seq.md5)


def test_service_info(server, data):
    '''Test info retrieval from fetch_info and Fetch.info using a mock server.
    '''
    fetcher = Fetcher(server)
    info = fetcher.fetch_info()
    assert "circular_supported" in info
    assert "algorithms" in info
    assert "subsequence_limit" in info
    assert "supported_api_versions" in info
