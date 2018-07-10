import requests
import warnings
import json
from urllib.parse import urlparse


def handle_error(response):
    '''
    args:
        reponse - Response object from requests library. Called from
        fetch_sequence and fetch_metadata methods of Fetcher

    objective:
        handle_error function is used to raise exception is case of status
        codes other than 200, 206 or 302.
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
    information refer
    '''

    def __init__(self, base_url):
        '''
        args:
            base_url - server's base url which will be used to query sequences
            or metdata from methods defined below
        objective:
            Works as a Factory class, Sets __cache to None
        '''

        self.set_base_url(base_url)
        self.__cache = None

    def __str__(self):
        '''
        objective:
            To get base url by doing str(<Fetcher object>) or it can be used to
            store fetcher objects in a dict as well
        '''
        return self.get_base_url()

    def get_base_url(self):
        '''
        objective:
            gets the __base_url of Fetcher object
        '''
        return self.__base_url

    def set_base_url(self, base_url):
        '''
        args:
            base_url - server's base url which will be used to query sequences
            or metdata from methods defined below
        objective:
            Sets the __base_url of the Fetcher object. Used to change the
            __base_url in already instantiated object. Url scheme stores the
            name of protocol (http or https) if provided otherwise if its empty
            string it adds http://
        '''
        url = urlparse(base_url)
        if url.scheme == '':
            self.__base_url = 'http://' + url.path
        else:
            self.__base_url = url.scheme + '://' + url.netloc + url.path
        self.__base_url = self.__base_url[:-1] if self.__base_url[-1] == '/' else self.__base_url

    def __set_cache(self, checksum):
        '''
        args:
            self - Object reference
            checksum - Checksum of the sequence to be retrieved.
        objective:
            Called from fetch_sequence in the condition of only one of the
            start and end is provided. Makes a call to metadata endpoint and
            stores in __cache mainly to have length only if __cache is already
            populated with the metadata of same sequence
        '''
        if self.__cache is None or (self.__cache['metadata']['md5'] != checksum and self.__cache['metadata']['trunc512'] != checksum):
            API = '/sequence/'
            url = self.get_base_url() + API + str(checksum) + '/metadata'
            self.__cache = json.loads(handle_error(requests.get(url)).text)

    def fetch_sequence(self, checksum, **kwargs):
        '''
        args:
            checksum - Checksum of the sequence to be retrieved.
        optional args:
            start - first byte
            end - last byte
            encoding - Accept header value
        objective:
            Used as the factory method to retrieve sequence. start and end are
            translated into Range header. If only one of start and end is given
            other parameter is filled using metadata-cache system. If it's a
            circular query start and end are passed as url params.
        '''

        API = '/sequence/'
        url = self.get_base_url() + API + str(checksum)

        start = int(kwargs.get('start')) if kwargs.get('start') is not None else None
        end = int(kwargs.get('end')) if kwargs.get('end') is not None else None
        # encoding = kwargs.get('encoding')

        headers = {}
        if start is not None and end is not None and end >= start:
            headers['Range'] = 'bytes=' + str(start) + '-' + str(end - 1)

        elif (start is not None and end is None) or (start is None and end is not None):
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
        '''
        args:
            checksum - Checksum of the sequence to be retrieved.
        optional args:
            encoding - Accept header value
        objective:
            Used as the factory method to retrieve metadata.
        '''

        API = '/sequence/'
        url = self.get_base_url() + API + str(checksum) + '/metadata'
        # headers = {}
        # if 'encoding' in kwargs:
        #     headers['Accept'] = str(kwargs['encoding'])
        response = handle_error(requests.get(url))
        return response.text

    def fetch_info(self):
        '''
        objective:
            Used to retrieve service info of the base_url
        '''

        API = '/sequence/service-info'
        url = self.get_base_url() + API
        # headers = {}
        # if 'encoding' in kwargs:
        #     headers['Accept'] = str(kwargs['encoding'])
        response = handle_error(requests.get(url))
        return response.text

    @classmethod
    def sequence(cls, base_url, checksum, **kwargs):
        '''
        args:
            base_url - server's base url which will be used to query sequences
            or metdata from methods defined below
            checksum - Checksum of the sequence to be retrieved.
        optional args:
            start - first byte
            end - last byte
            encoding - Accept header value
        objective:
            Used as the shortcut method to retrieve sequence and internally
            calls fetch_sequence.
        '''
        fetcher = cls(base_url)
        return fetcher.fetch_sequence(checksum, **kwargs)

    @classmethod
    def metadata(cls, base_url, checksum, **kwargs):
        '''
        args:
            base_url - server's base url which will be used to query sequences
            or metdata from methods defined below
            checksum - Checksum of the sequence to be retrieved.
        optional args:
            encoding - Accept header value
        objective:
            Used as the shortcut method to retrieve metadata and internally
            calls fetch_metadata.
        '''
        fetcher = cls(base_url)
        return fetcher.fetch_metadata(checksum, **kwargs)

    @classmethod
    def info(cls, base_url):
        '''
        objective:
            Used as the shortcut method to retrieve service info and internally
            calls fetch_info.
        '''
        fetcher = cls(base_url)
        return fetcher.fetch_info()
