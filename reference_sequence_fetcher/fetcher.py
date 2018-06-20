import requests
import warnings


def handle_error(response):
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
    def __init__(self, base_url):
        base_url = str(base_url)
        if '://' in base_url:
            self.__base_url = base_url
        else:
            self.__base_url = 'http://' + base_url

    def __str__(self):
        return self.__base_url

    def get_base_url(self):
        return self.__base_url

    def set_base_url(self, base_url):
        self.__base_url = 'http://' + str(base_url)

    def fetch_sequence(self, checksum, **kwargs):
        API = '/sequence/'
        url = self.get_base_url() + API + str(checksum)

        if 'start' or 'end' in kwargs:
            url = url + '?'
        if 'start' in kwargs:
            url = url + 'start=' + str(kwargs['start']) + '&'
        if 'end' in kwargs:
            url = url + 'end=' + str(kwargs['end'])

        headers = {}
        if 'fbs' and 'lbs' in kwargs:
            headers['Range'] = \
                'bytes=' + str(kwargs['fbs']) + '-' + str(kwargs['lbs'])
        if 'encoding' in kwargs:
            headers['Accept'] = str(kwargs['encoding'])

        response = handle_error(requests.get(url, headers=headers))
        return response.text

    def fetch_metadata(self, checksum, **kwargs):
        API = '/sequence/'
        url = self.get_base_url() + API + str(checksum) + '/metadata'
        headers = {}
        if 'encoding' in kwargs:
            headers['Accept'] = str(kwargs['encoding'])
        response = handle_error(requests.get(url, headers=headers))
        return response.text

    @classmethod
    def sequence(cls, base_url, checksum, **kwargs):
        fetcher = cls(base_url)
        return fetcher.fetch_sequence(checksum, **kwargs)

    @classmethod
    def metadata(cls, base_url, checksum, **kwargs):
        fetcher = cls(base_url)
        return fetcher.fetch_metadata(checksum, **kwargs)
