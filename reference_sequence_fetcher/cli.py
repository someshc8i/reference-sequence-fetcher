import click
try:
    from reference_sequence_fetcher.fetcher import Fetcher
except:
    from fetcher import Fetcher


@click.group()
def main():
    pass


@main.command(help='retrieve sequence using base_url and checksum')
@click.argument('base_url')
@click.argument('checksum')
@click.option('--start', '-s', default=None, type=int, help='first byte of the checksum. 0-start inclusive')
@click.option('--end', '-e', default=None, type=int, help='last byte of the checksum. 0-start exclusive')
@click.option('--encoding', '-en', default=None, help='encoding being requested. Defaults to text/plain')
def sequence(base_url, checksum, start, end, encoding):
    '''maps to class method Fetcher.sequence for sequence retrieval
    '''
    click.echo(
        Fetcher.sequence(
            base_url, checksum, start=start, end=end, encoding=encoding))


@main.command(help='retrieve metadata using base_url and checksum')
@click.argument('base_url')
@click.argument('checksum')
@click.option('--encoding', '-en', default=None, help='encoding being requested. Defaults to text/plain')
def metadata(base_url, checksum, encoding):
    '''maps to class method Fetcher.metadata for metadata retrieval
    '''
    click.echo(
        Fetcher.metadata(
            base_url, checksum, encoding=encoding))


if __name__ == "__main__":
    main()
