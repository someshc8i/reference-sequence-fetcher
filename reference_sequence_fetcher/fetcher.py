import requests


def handle_error():
    pass


class Fetcher(object):
    def __init__(self, base_url):
        self.__base_url = 'http://' + base_url

    def __str__(self):
        return self.__base_url

    def get_base_url(self):
        return self.__base_url

    def set_base_url(self, base_url):
        self.__base_url = 'http://' + base_url

    def fetch_sequence(self, checksum, **kwargs):
        API = '/sequence/'
        url = self.get_base_url() + API + checksum
        if 'start' or 'end' in kwargs:
            url = url + '?'
        if 'start' in kwargs:
            url = url + 'start=' + str(kwargs['start']) + '&'
        if 'end' in kwargs:
            url = url + 'end=' + str(kwargs['end'])

        headers = {}
        if 'accept' in kwargs:
            headers['Accept'] = kwargs['accept']
        if 'encoding' in kwargs:
            headers['encoding'] = kwargs['encoding']
        response = requests.get(url, headers=headers)
        if response.status_code == 415:
            print('Unsupported Media type')
            raise
        handle_error(response)
        return response.text

    def fetch_metadata(self, checksum, **kwargs):
        pass

    @classmethod
    def sequence(cls, base_url, checksum, **kwargs):
        fetcher = cls(base_url)
        return fetcher.fetch_sequence(checksum, **kwargs)

    @classmethod
    def metadata(cls, base_url, checksum, **kwargs):
        fetcher = cls(base_url)
        return fetcher.fetch_metadata(checksum, **kwargs)
