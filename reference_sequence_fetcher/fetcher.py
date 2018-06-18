class Fetcher(object):
    def __init__(self, base_url):
        self.__base_url = base_url

    def __str__(self):
        return self.__base_url

    def get_base_url(self):
        return self.__base_url

    def set_base_url(self, base_url):
        self.__base_url = base_url

    def fetch_sequence(self, checksum, **kwargs):
        pass

    def fetch_metadata(self, checksum, **kwargs):
        pass

    @classmethod
    def sequence(cls, base_url, checksum, **kwargs):
        pass

    @classmethod
    def metadata(cls, base_url, checksum, **kwargs):
        pass
