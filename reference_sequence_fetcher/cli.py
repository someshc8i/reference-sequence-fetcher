import click
try:
    from reference_sequence_fetcher.fetcher import Fetcher
except:
    from fetcher import Fetcher


@click.group()
def main():
    pass


@main.command()
@click.argument('base_url')
@click.argument('checksum')
@click.option('--start', '-s', default=None)
@click.option('--end', '-e', default=None)
@click.option('--encoding', '-en', default=None)
def sequence(base_url, checksum, start, end, encoding):
    click.echo(
        Fetcher.sequence(
            base_url, checksum, start=start, end=end, encoding=encoding))


@main.command()
@click.argument('base_url')
@click.argument('checksum')
@click.option('--encoding', '-en', default=None)
def metadata(base_url, checksum, encoding):
    click.echo(
        Fetcher.metadata(
            base_url, checksum, encoding=encoding))


if __name__ == "__main__":
    main()
