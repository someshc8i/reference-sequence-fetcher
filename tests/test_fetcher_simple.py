from reference_sequence_fetcher import Fetcher


def test_getter_setter_base_url_Fetcher():
    fetcher = Fetcher('111.11.1.0')
    assert fetcher.get_base_url() == '111.11.1.0'

    fetcher.set_base_url('localhost')
    assert fetcher.get_base_url() == 'localhost'
