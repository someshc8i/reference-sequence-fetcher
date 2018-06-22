from reference_sequence_fetcher.fetcher import Fetcher, handle_error
import pytest
import json


class MockResponse(object):
    def __init__(self, status_code, text=None):
        self.status_code = status_code
        self.text = text


def get_metadata(seq, checksum):
    response = {
        "metadata": {
            "id": checksum,
            "length": seq.size,
            "alias": []
        }
    }
    response["metadata"]["alias"].append({"alias": seq.md5})
    response["metadata"]["alias"].append({"alias": seq.sha512})
    return json.dumps(response)


def check_complete_metdata_response(metadata, seq, checksum):
    '''check_complete_metdata_response is a utility function used by
    test_complete_metadata function to remove duplication of code. It takes
    response se,q object and checksum ID used to query as input parameter and
    assert for reponse header, status code and content
    '''

    assert metadata == get_metadata(seq, checksum)


def test_getter_setter_base_url_Fetcher():
    fetcher = Fetcher('111.11.1.0')
    assert fetcher.get_base_url() == 'http://111.11.1.0'

    fetcher.set_base_url('localhost')
    assert fetcher.get_base_url() == 'http://localhost'

    assert str(fetcher) == 'http://localhost'


def test_fetch_sequence_full_sequence_retrieval(data, server):
    fetcher = Fetcher(server)
    for seq in data:
        assert fetcher.fetch_sequence(seq.md5) == seq.sequence
        assert Fetcher.sequence(server, seq.md5) == seq.sequence


def test_fetch_sequence_start_end_sequence_retrieval(data, server):
    fetcher = Fetcher(server)
    for seq in data:
        assert fetcher.fetch_sequence(seq.md5, start=0, end=10) \
            == seq.sequence[:10]


def test_fetch_sequence_range_sequence_retrieval(data, server):
    fetcher = Fetcher(server)
    for seq in data:
        assert fetcher.fetch_sequence(seq.md5, fbs=0, lbs=10) \
            == seq.sequence[:11]


@pytest.mark.parametrize("_input, _output", [
    (400, 'Check the parameters provided i.e start, end, fbs and lbs.'),
    (404, 'Checksum identifier provided can not be found.'),
    (415, 'Encoding is not supported by the server.'),
    (416, 'Range can not be satisfied.'),

])
def test_handle_error_function(server, _input, _output):
    with pytest.raises(Exception) as excinfo:
        handle_error(MockResponse(_input))
    assert str(excinfo.value) == _output


def test_warning_501_handle_error_function(server):
    with pytest.warns(UserWarning, match='Circular support is not implemented in the server'):
        handle_error(MockResponse(501))


def test_metadata(server, data):
    fetcher = Fetcher(server)
    for seq in data:
        check_complete_metdata_response(
            fetcher.fetch_metadata(seq.md5), seq, seq.md5)
        check_complete_metdata_response(
            Fetcher.metadata(server, seq.md5), seq, seq.md5)
