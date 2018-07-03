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
def sequence(base_url, checksum, start, end):
    '''maps to class method Fetcher.sequence for sequence retrieval
    '''
    click.echo(Fetcher.sequence(base_url, checksum, start=start, end=end))


@main.command(help='retrieve metadata using base_url and checksum')
@click.argument('base_url')
@click.argument('checksum')
def metadata(base_url, checksum, encoding):
    '''maps to class method Fetcher.metadata for metadata retrieval
    '''
    click.echo(Fetcher.metadata(base_url, checksum))


@main.command(help='retrieve service info using base_url')
@click.argument('base_url')
def info(base_url):
    '''maps to class method Fetcher.info for service info retrieval
    '''
    click.echo(Fetcher.info(base_url))


if __name__ == "__main__":
    main()
