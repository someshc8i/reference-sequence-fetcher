from click.testing import CliRunner
from reference_sequence_fetcher.cli import sequence, metadata, info
from tests.test_fetcher import get_metadata


def test_sequence(server, data):
    '''Test case to test sequence function of cli
    '''
    seq = data[0]
    runner = CliRunner()
    result = runner.invoke(sequence, [server, seq.md5])
    assert result.exit_code == 0
    assert seq.sequence in result.output


def test_metadata(server, data):
    '''Test case to test metadata function of cli.
    '''
    seq = data[0]
    runner = CliRunner()
    result = runner.invoke(metadata, [server, seq.md5])
    assert result.exit_code == 0
    assert get_metadata(seq) in result.output


def test_info(server, data):
    '''Test case to test metadata function of cli.
    '''
    runner = CliRunner()
    result = runner.invoke(info, [server])
    assert result.exit_code == 0
    assert 'circular_supported' in result.output
    assert 'algorithms' in result.output
    assert 'subsequence_limit' in result.output
    assert 'supported_api_versions' in result.output
