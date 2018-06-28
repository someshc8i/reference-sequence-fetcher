import json
import pytest

from click.testing import CliRunner
from reference_sequence_fetcher.cli import sequence, metadata
from tests.test_fetcher import get_metadata


def test_sequence(server, data):
    '''Test case to test sequence function of cli
    '''
    seq = data[0]
    runner = CliRunner()
    result = runner.invoke(sequence, [server, seq.md5])
    assert result.exit_code == 0
    assert seq.sequence in result.output


@pytest.mark.skip
def test_metadata(server, data):
    '''Test case to test metadata function of cli.
    '''
    seq = data[0]
    runner = CliRunner()
    result = runner.invoke(metadata, [server, seq.md5])
    assert result.exit_code == 0
    assert get_metadata(seq, seq.sequence) in json.dumps(result.output)
