import requests
import warnings
import json
from urllib.parse import urlparse


def handle_error(response):
    ''' handle_error function is used to raise exception is case of status codes
    other than 200, 206 or 302.
    '''

    if response.status_code == 400:
        raise Exception(
            'Check the parameters provided i.e start, end, fbs and lbs.')
    if response.status_code == 404:
        raise Exception('Checksum identifier provided can not be found.')
    if response.status_code == 415:
        raise Exception('Encoding is not supported by the server.')
    if response.status_code == 416:
        raise Exception('Range can not be satisfied.')
    if response.status_code == 500:
        raise Exception('There maybe some internal server error.')
    if response.status_code == 501:
        warnings.warn(
            'Circular support is not implemented in the server', UserWarning)
        return response
    return response


class Fetcher(object):
    '''Act as a Factory class to retrieve sequences and metadata. For more
    information refer :
    https://reference-sequence-fetcher.readthedocs.io/en/latest/api_documentation.html
    '''

    def __init__(self, base_url):
        self.set_base_url(base_url)
        self.__cache = None

    def __str__(self):
        return self.get_base_url()

    def get_base_url(self):
        return self.__base_url

    def set_base_url(self, base_url):
        url = urlparse(base_url)
        if url.scheme == '':
            self.__base_url = 'http://' + url.path
        else:
            self.__base_url = url.scheme + '://' + url.netloc

    def __set_cache(self, checksum):
        if self.__cache is None or \
                self.__cache['metadata']['checksum'] != checksum:
            API = '/sequence/'
            url = self.get_base_url() + API + str(checksum) + '/metadata'
            self.__cache = json.loads(handle_error(requests.get(url)).text)

    def fetch_sequence(self, checksum, **kwargs):
        API = '/sequence/'
        url = self.get_base_url() + API + str(checksum)

        start = kwargs.get('start')
        end = kwargs.get('end')
        # encoding = kwargs.get('encoding')

        headers = {}
        if start is not None and end is not None and end >= start:
            headers['Range'] = 'bytes=' + str(start) + '-' + str(end - 1)

        elif (start and end is None) or (start is None and end):
            self.__set_cache(checksum)
            length = self.__cache['metadata']['length']
            if start is None:
                start = 0
            if end is None:
                end = length
            headers['Range'] = 'bytes=' + str(start) + '-' + str(end - 1)

        elif start and end and end < start:
            url = url + '?start=' + str(start) + '&' + 'end=' + str(end)

        # if encoding:
        #     headers['Accept'] = encoding

        response = handle_error(requests.get(url, headers=headers))
        return response.text

    def fetch_metadata(self, checksum, **kwargs):
        API = '/sequence/'
        url = self.get_base_url() + API + str(checksum) + '/metadata'
        # headers = {}
        # if 'encoding' in kwargs:
        #     headers['Accept'] = str(kwargs['encoding'])
        response = handle_error(requests.get(url))
        return response.text

    @classmethod
    def sequence(cls, base_url, checksum, **kwargs):
        fetcher = cls(base_url)
        return fetcher.fetch_sequence(checksum, **kwargs)

    @classmethod
    def metadata(cls, base_url, checksum, **kwargs):
        fetcher = cls(base_url)
        return fetcher.fetch_metadata(checksum, **kwargs)
