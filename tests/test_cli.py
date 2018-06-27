import json

from click.testing import CliRunner
from reference_sequence_fetcher.cli import sequence
# from tests.test_fetcher import get_metadata


def test_sequence(server, data):
    seq = data[0]
    runner = CliRunner()
    result = runner.invoke(sequence, [server, seq.md5])
    assert result.exit_code == 0
    assert seq.sequence in result.output

#
# def test_metadata(server, data):
#     seq = data[0]
#     runner = CliRunner()
#     result = runner.invoke(metadata, [server, seq.md5])
#     assert result.exit_code == 0
#     assert get_metadata(seq, seq.sequence) in json.dumps(result.output)
